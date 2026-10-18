"""The runner's input handling, exercised against real preparation output.

No API calls: these stop at the point where the request would be sent. The
runner is a script rather than a module, so it is loaded by file path the same
way the preparation tests load theirs.
"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from types import ModuleType

import pytest

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
