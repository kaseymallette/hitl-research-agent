"""The primer script, offline: it writes a labelled primer and its record."""

import importlib.util
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType

import pytest

from hitl_research_agent.analysis import AnalysisError, AttemptRecord, AttemptUsage, PrimerResult
from hitl_research_agent.models import Primer

sys.path.insert(0, str(Path(__file__).parent / "preparation"))
from pdf_fixtures import make_text_pdf  # noqa: E402

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "write_primer.py"


@pytest.fixture(scope="module")
def primer_script() -> ModuleType:
    spec = importlib.util.spec_from_file_location("write_primer", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["write_primer"] = module
    spec.loader.exec_module(module)
    return module


def _attempt() -> AttemptRecord:
    moment = datetime(2026, 10, 24, tzinfo=UTC)
    return AttemptRecord(
        attempt_number=1,
        outcome="valid",
        started_at=moment,
        ended_at=moment,
        elapsed_seconds=1.0,
        usage=AttemptUsage(input_tokens=900, output_tokens=700),
    )


def _run(
    script: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, primer: object
) -> tuple[int, Path]:
    pdf = tmp_path / "plain.pdf"
    make_text_pdf(pdf, [["A short fixture article about cooling water."]])
    (tmp_path / "sources.yaml").write_text(
        f"""sources:
  - slug: plain
    pdf: {pdf}
    source_title: "A Fixture Paper"
    source_type: other
    retrieved_at: "2026-10-15T00:00:00+00:00"
"""
    )
    monkeypatch.setenv("OPENAI_API_KEY", "test-key-not-used")
    monkeypatch.setattr(script, "write_primer", primer)
    out = tmp_path / "primers"
    code = script.main(
        [
            "--pdf",
            str(pdf),
            "--manifest",
            str(tmp_path / "sources.yaml"),
            "--out",
            str(out),
            "--confirm-paid",
        ]
    )
    return code, out / "plain"


def test_a_primer_is_written_labelled_as_background_with_its_cost(
    primer_script: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def primer(*args: object, **kwargs: object) -> PrimerResult:
        return PrimerResult(
            primer=Primer(primer="Exergy is the useful part of energy."),
            model="gpt-6.1-sol",
            input_tokens=900,
            output_tokens=700,
            attempt_count=1,
            attempts=[_attempt()],
        )

    code, folder = _run(primer_script, tmp_path, monkeypatch, primer)

    assert code == 0
    text = (folder / "primer.md").read_text()
    assert text.startswith("# Primer — A Fixture Paper")
    assert "not a reading of the article" in text
    assert "Exergy is the useful part of energy." in text
    record = json.loads((folder / "primer_record.json").read_text())
    assert record["outcome"] == "primer returned"
    assert record["usage"]["input_tokens"] == 900
    assert record["calculated_cost"]["total_usd"] > 0


def test_a_failed_primer_leaves_a_record_and_no_primer(
    primer_script: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def primer(*args: object, **kwargs: object) -> None:
        error = AnalysisError("refused", kind="refused")
        error.attempts = [_attempt()]
        raise error

    code, folder = _run(primer_script, tmp_path, monkeypatch, primer)

    assert code == 1
    assert not (folder / "primer.md").exists()
    assert json.loads((folder / "primer_record.json").read_text())["outcome"] == "failed: refused"
