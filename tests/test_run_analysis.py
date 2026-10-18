"""The runner's input handling, exercised against real preparation output.

No API calls: these stop at the point where the request would be sent. The
runner is a script rather than a module, so it is loaded by file path the same
way the preparation tests load theirs.
"""

import importlib.util
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType

import pytest

from hitl_research_agent.analysis import AnalysisError, AttemptRecord, AttemptUsage

sys.path.insert(0, str(Path(__file__).parent / "preparation"))
from pdf_fixtures import make_table_pdf, make_text_pdf  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER = REPO_ROOT / "scripts" / "run_analysis.py"
PREPARE = REPO_ROOT / "scripts" / "prepare_sources.py"


@pytest.fixture(scope="session")
def runner() -> ModuleType:
    spec = importlib.util.spec_from_file_location("run_analysis", RUNNER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["run_analysis"] = module
    spec.loader.exec_module(module)
    return module


PLAIN_PAGES = [
    [
        "Data centers withdraw water for evaporative cooling, and the volume "
        "depends on climate, workload, and the cooling technology chosen.",
        "This fixture carries no figures, equations, or multi-level table "
        "headers, so preparation has nothing it cannot represent in text.",
    ]
]


def _prepare(tmp_path: Path, slug: str, make_pdf: object) -> Path:
    """Run the real preparation script and return its output directory."""
    pdf = tmp_path / f"{slug}.pdf"
    if make_pdf is make_text_pdf:
        make_text_pdf(pdf, PLAIN_PAGES)
    else:
        make_pdf(pdf)  # type: ignore[operator]
    manifest = tmp_path / "sources.yaml"
    manifest.write_text(
        f"""sources:
  - slug: {slug}
    pdf: {pdf}
    source_title: "A Fixture Paper"
    source_authors: [Someone]
    publication_date: "2026-01-02"
    source_type: other
    doi: 10.1000/fixture
    retrieved_at: "2026-10-15T00:00:00+00:00"
"""
    )
    out = tmp_path / "prepared"
    subprocess.run(
        [
            sys.executable,
            str(PREPARE),
            "prepare",
            "--slug",
            slug,
            "--manifest",
            str(manifest),
            "--output-root",
            str(out),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return out / slug


def test_a_prepared_source_loads_with_its_confirmed_provenance_and_crops(
    runner: ModuleType, tmp_path: Path
) -> None:
    """The run record's provenance has to be the owner-confirmed manifest data,
    not values invented at runtime."""
    prep_dir = _prepare(tmp_path, "withtable", make_table_pdf)
    source, crops = runner.load_prepared_source(prep_dir)

    assert source.provenance.source_title == "A Fixture Paper"
    assert source.provenance.source_authors == ["Someone"]
    assert source.provenance.retrieved_at.isoformat() == "2026-10-15T00:00:00+00:00"
    assert source.preparation_gaps, "a table fixture should declare at least one gap"
    assert len(crops) == len([g for g in source.preparation_gaps if g.image])
    for crop, gap in zip(crops, source.preparation_gaps, strict=True):
        assert crop.record.gap_id == gap.id
        assert crop.record.byte_size > 0


def test_an_article_with_no_crops_still_loads(runner: ModuleType, tmp_path: Path) -> None:
    """No figures, equations, or multi-level headers is a successful
    preparation, not a failure: the arm is simply prepared text."""
    prep_dir = _prepare(tmp_path, "plain", make_text_pdf)
    record = json.loads((prep_dir / "prep_record.json").read_text())
    assert record["annotations"] == [], "the text fixture should declare no gaps"

    source, crops = runner.load_prepared_source(prep_dir)
    assert crops == []
    assert source.preparation_gaps == []
    assert source.text  # the prepared text is still there to analyze


def test_a_no_crop_cell_is_recorded_as_prepared_text(runner: ModuleType) -> None:
    """The matrix still needs the cell, and the record has to say that the
    model received text only, so Phase 2 does not read it as crops-versus-PDF."""
    assert runner.INPUT_MODES["text_crops"] == "prepared_text_and_crops"
    assert runner.INPUT_MODES["text"] == "prepared_text"
    # The config slug names the arm, which is what keeps the matrix complete.
    assert runner.config_slug("text_crops", "gpt-6-astra", "low") == "text_crops__gpt-6-astra-low"


def test_a_missing_preparation_directory_says_what_to_run(
    runner: ModuleType, tmp_path: Path
) -> None:
    with pytest.raises(SystemExit, match="prepare_sources.py"):
        runner.load_prepared_source(tmp_path / "nothing")


def test_a_pdf_source_takes_its_provenance_from_the_manifest(
    runner: ModuleType, tmp_path: Path
) -> None:
    """The PDF arm reads the owner-confirmed manifest, not the PDF's own
    metadata or a value typed at the command line."""
    _prepare(tmp_path, "plain", make_text_pdf)
    provenance = runner.manifest_provenance(tmp_path / "sources.yaml", "plain")
    source = runner.load_pdf_source(tmp_path / "plain.pdf", "plain.pdf", provenance)

    assert source.provenance.source_title == "A Fixture Paper"
    assert source.provenance.source_authors == ["Someone"]
    assert source.provenance.source_type == "other"
    assert source.provenance.doi == "10.1000/fixture"
    assert source.provenance.publication_date.isoformat() == "2026-01-02"
    assert source.provenance.retrieved_at.isoformat() == "2026-10-15T00:00:00+00:00"


def test_both_arms_give_the_model_the_same_provenance(runner: ModuleType, tmp_path: Path) -> None:
    """The title and source type are in the prompt, so the two arms of one
    article must carry the same provenance for the prompt to be held constant,
    and the same source_id so their analyses are recognized as one source's."""
    prep_dir = _prepare(tmp_path, "plain", make_text_pdf)
    prepared, _ = runner.load_prepared_source(prep_dir)
    from_manifest = runner.manifest_provenance(tmp_path / "sources.yaml", "plain")

    assert prepared.provenance == from_manifest


def test_a_pdf_with_no_manifest_entry_is_refused(runner: ModuleType, tmp_path: Path) -> None:
    _prepare(tmp_path, "plain", make_text_pdf)
    with pytest.raises(SystemExit, match="No entry for unlisted"):
        runner.manifest_provenance(tmp_path / "sources.yaml", "unlisted")


def _attempt(number: int, outcome: str, usage: dict[str, int | None] | None) -> AttemptRecord:
    moment = datetime(2026, 10, 17, tzinfo=UTC)
    return AttemptRecord(
        attempt_number=number,
        outcome=outcome,  # type: ignore[arg-type]
        started_at=moment,
        ended_at=moment,
        elapsed_seconds=1.0,
        usage=AttemptUsage(**usage) if usage else None,  # type: ignore[arg-type]
    )


def _run_pdf_cell(
    runner: ModuleType,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    analyze: object,
) -> tuple[int, Path]:
    """Run main() on a fixture PDF cell with the model call replaced."""
    _prepare(tmp_path, "plain", make_text_pdf)
    monkeypatch.setenv("OPENAI_API_KEY", "test-key-not-used")
    monkeypatch.setattr(runner, "analyze_source", analyze)
    out = tmp_path / "out"
    code = runner.main(
        [
            "--pdf",
            str(tmp_path / "plain.pdf"),
            "--input",
            "pdf",
            "--model",
            "gpt-6.1-sol",
            "--effort",
            "high",
            "--manifest",
            str(tmp_path / "sources.yaml"),
            "--out",
            str(out),
            "--confirm-paid",
        ]
    )
    return code, out / "plain" / "pdf__gpt-6.1-sol-high"


def test_a_failed_cell_records_every_attempt_s_tokens_and_cost(
    runner: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A schema miss followed by a refusal: the error carries only the second
    response's tokens, but both responses were billed."""

    def analyze(*args: object, **kwargs: object) -> None:
        error = AnalysisError("refused", kind="refused", input_tokens=1_100, output_tokens=60)
        error.attempts = [
            _attempt(
                1,
                "parse_error",
                {"input_tokens": 1_000, "output_tokens": 500, "reasoning_tokens": 200},
            ),
            _attempt(
                2,
                "refused",
                {"input_tokens": 1_100, "output_tokens": 60, "reasoning_tokens": 30},
            ),
        ]
        raise error

    code, cell = _run_pdf_cell(runner, tmp_path, monkeypatch, analyze)

    assert code == 1
    assert not (cell / "analysis.json").exists()
    record = json.loads((cell / "run_record.json").read_text())
    assert record["outcome"] == "failed: refused"
    assert record["model"] == "gpt-6.1-sol"
    assert record["reasoning_effort"] == "high"
    assert record["openai_max_retries"] == 0
    assert record["usage"] == {
        "input_tokens": 2_100,
        "output_tokens": 560,
        "reasoning_tokens": 230,
        "cached_input_tokens": 0,
    }
    assert record["calculated_cost"]["input_tokens"] == 2_100
    assert record["calculated_cost"]["output_tokens"] == 560


def test_every_cell_records_the_same_prompt_and_schema_fingerprints(
    runner: ModuleType,
) -> None:
    """The system prompt and schema are held constant across arms; only the
    format-specific instructions differ, and the record shows which."""
    pdf, crops, text = (
        runner.fingerprints(mode) for mode in ("pdf", "prepared_text_and_crops", "prepared_text")
    )
    for key in ("system_prompt_sha256", "output_schema_sha256", "git_commit"):
        assert pdf[key] == crops[key] == text[key]
        assert pdf[key]
    assert pdf["input_mode_instructions_sha256"] != crops["input_mode_instructions_sha256"]
    assert text["input_mode_instructions_sha256"] is None


def test_a_cell_that_holds_an_analysis_is_not_rerun(
    runner: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A paid result is never overwritten, and a failed rerun can never sit
    beside an earlier analysis it does not describe."""
    cell = tmp_path / "out" / "plain" / "pdf__gpt-6.1-sol-high"
    cell.mkdir(parents=True)
    (cell / "analysis.json").write_text("{}\n")

    def analyze(*args: object, **kwargs: object) -> None:
        raise AssertionError("the model must not be called")

    code, _ = _run_pdf_cell(runner, tmp_path, monkeypatch, analyze)
    assert code == 2
    assert (cell / "analysis.json").read_text() == "{}\n"
    assert not (cell / "run_record.json").exists()


def test_a_crash_before_the_call_leaves_no_cell_directory(
    runner: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def analyze(*args: object, **kwargs: object) -> None:
        raise ValueError("input_mode 'pdf' requires exactly one pdf attachment")

    with pytest.raises(ValueError):
        _run_pdf_cell(runner, tmp_path, monkeypatch, analyze)
    assert not (tmp_path / "out" / "plain").exists()


def test_reasoning_total_is_unknown_when_a_response_did_not_report_it(
    runner: ModuleType,
) -> None:
    totals = runner.usage_totals(
        [
            _attempt(1, "parse_error", {"input_tokens": 10, "output_tokens": 5}),
            _attempt(2, "valid", {"input_tokens": 10, "output_tokens": 5, "reasoning_tokens": 2}),
        ]
    )
    assert totals["reasoning_tokens"] is None
    assert totals["output_tokens"] == 10
    assert runner.usage_totals([])["reasoning_tokens"] is None


def test_rerunning_a_failed_cell_keeps_the_failed_run_s_record(
    runner: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A failed run's tokens were billed, so its record survives the rerun."""
    tokens = iter([100, 200])

    def analyze(*args: object, **kwargs: object) -> None:
        error = AnalysisError("refused", kind="refused")
        error.attempts = [
            _attempt(1, "refused", {"input_tokens": next(tokens), "output_tokens": 1})
        ]
        raise error

    _run_pdf_cell(runner, tmp_path, monkeypatch, analyze)
    _, cell = _run_pdf_cell(runner, tmp_path, monkeypatch, analyze)

    kept = json.loads((cell / "failed_run_1.json").read_text())
    latest = json.loads((cell / "run_record.json").read_text())
    assert kept["usage"]["input_tokens"] == 100
    assert latest["usage"]["input_tokens"] == 200
