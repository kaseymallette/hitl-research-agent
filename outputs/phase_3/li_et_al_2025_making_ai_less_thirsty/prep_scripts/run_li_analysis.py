"""One-off pilot run: analyze the prepared Li et al. (2025) source with the unchanged pipeline.
Usage: python -I run_li_analysis.py OUT_DIR PDF_PATH [--dry]
Never prints or stores the API key."""
import json, sys, time, traceback
from datetime import UTC, datetime
from pathlib import Path

from hitl_research_agent.config import Settings
from hitl_research_agent.extraction import pipeline
from hitl_research_agent.extraction.errors import SourceAnalysisError
from hitl_research_agent.extraction.prompts import build_messages
from hitl_research_agent.extraction.schemas import SourceDocument
from hitl_research_agent.models.provenance import Provenance

OUT, PDF = Path(sys.argv[1]), Path(sys.argv[2])
DRY = "--dry" in sys.argv
RATE_IN, RATE_OUT = 10.00, 50.00  # USD per 1M tokens, gpt-6-astra standard (<=272K input), per OpenAI pricing page

settings = Settings()
text = (OUT / "source.md").read_text(encoding="utf-8")
rec = json.loads((OUT / "prep_record.json").read_text())
mtime = datetime.fromtimestamp(PDF.stat().st_mtime, tz=UTC)
prov = Provenance(
    source_title="Making AI Less 'Thirsty': Uncovering and addressing the secret water footprint of AI models",
    source_authors=["Pengfei Li", "Jianyi Yang", "Mohammad A. Islam", "Shaolei Ren"],
    source_type="other",
    doi="10.1145/3724499",
    publisher="Communications of the ACM (ACM)",
    retrieved_at=mtime,
)
source = SourceDocument(text=text, provenance=prov)
size_ok = len(source.text) <= settings.max_source_characters
msgs = build_messages(source)
system_text = str(msgs[0].content).lower()
leak = [w for w in ("freshwater", "desalination", "alternative cooling", "water supplies") if w in system_text]
print(json.dumps({
    "model": settings.openai_model, "reasoning_effort": settings.openai_reasoning_effort,
    "api_key_present": bool(settings.openai_api_key), "source_characters": len(source.text),
    "limit": settings.max_source_characters, "size_ok": size_ok, "system_prompt_question_terms": leak,
    "retrieved_at_proxy": mtime.isoformat()}, indent=1))
rec["size_check"] = {"characters": len(source.text), "limit": settings.max_source_characters, "within_limit": size_ok,
                     "checked_at_utc": datetime.now(UTC).isoformat()}
(OUT / "prep_record.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
(OUT / "provenance.json").write_text(prov.model_dump_json(indent=2), encoding="utf-8")
if DRY or not size_ok or leak or not settings.openai_api_key:
    print("DRY/ABORT: no API call made"); sys.exit(0)

class Recorder:
    """Wraps the pipeline's own default model to capture response ids/metadata. Does not alter the call."""
    def __init__(self, inner): self.inner, self.calls = inner, []
    def invoke(self, input):
        entry = {"started_at_utc": datetime.now(UTC).isoformat()}
        self.calls.append(entry)
        t0 = time.monotonic()
        try:
            res = self.inner.invoke(input)
        except Exception as exc:
            entry.update(error=f"{type(exc).__name__}: {exc}", elapsed_s=round(time.monotonic() - t0, 2),
                         ended_at_utc=datetime.now(UTC).isoformat())
            raise
        raw = res.get("raw")
        entry.update(ended_at_utc=datetime.now(UTC).isoformat(), elapsed_s=round(time.monotonic() - t0, 2),
                     response_id=getattr(raw, "id", None),
                     response_metadata=json.loads(json.dumps(getattr(raw, "response_metadata", {}), default=str)),
                     usage_metadata=json.loads(json.dumps(getattr(raw, "usage_metadata", None), default=str)),
                     parsing_error=str(res.get("parsing_error")) if res.get("parsing_error") else None)
        return res

recorder = Recorder(pipeline._build_default_model(settings))
run = {"run_started_at_utc": datetime.now(UTC).isoformat(), "model_setting": settings.openai_model,
       "reasoning_effort_setting": settings.openai_reasoning_effort, "source_characters": len(source.text),
       "prepared_source_sha256": rec["prepared_source_sha256"]}
try:
    result = pipeline.analyze_source(source, model=recorder, settings=settings)
    run["outcome"] = "success"
    (OUT / "analysis_result.json").write_text(result.model_dump_json(indent=2), encoding="utf-8")
    inp, outp = result.input_tokens, result.output_tokens
    run.update(attempt_count=result.attempt_count, reported_model_field=result.model, input_tokens=inp, output_tokens=outp)
except SourceAnalysisError as exc:
    run["outcome"] = f"failure: {type(exc).__name__}"
    run["error"] = str(exc)[:4000]
    inp = getattr(exc, "input_tokens", None); outp = getattr(exc, "output_tokens", None)
    run.update(input_tokens=inp, output_tokens=outp, attempt_count=getattr(exc, "attempt_count", None))
    run["traceback"] = traceback.format_exc()[-3000:]
except Exception as exc:  # unexpected
    run["outcome"] = f"failure: {type(exc).__name__}"; run["error"] = str(exc)[:4000]
    run["traceback"] = traceback.format_exc()[-3000:]; inp = outp = None
run["run_ended_at_utc"] = datetime.now(UTC).isoformat()
run["calls_observed_by_recorder"] = recorder.calls
if inp is not None and outp is not None:
    run["calculated_cost_usd"] = {
        "status": "CALCULATED from reported token counts; NOT confirmed billing",
        "rates_usd_per_1M_tokens": {"input": RATE_IN, "output_including_reasoning": RATE_OUT, "source": "gpt-6-astra standard tier, <=272K input, OpenAI pricing page as read on 2026-10-13"},
        "input_cost": round(inp * RATE_IN / 1e6, 4), "output_cost": round(outp * RATE_OUT / 1e6, 4),
        "total": round((inp * RATE_IN + outp * RATE_OUT) / 1e6, 4),
        "note": "output_tokens already include reasoning tokens; reasoning is not added again"}
(OUT / "run_record.json").write_text(json.dumps(run, indent=2, default=str), encoding="utf-8")
print(json.dumps({k: run.get(k) for k in ("outcome", "attempt_count", "input_tokens", "output_tokens", "calculated_cost_usd")}, indent=1, default=str))
