"""scripts/workspace.py: loading a source into the workspace and saving its results.

The script is not a package module, so it is loaded by file path.
"""

import importlib.util
import shutil
from pathlib import Path
from types import ModuleType
from typing import Any

import pymupdf
import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "workspace.py"


def load_script() -> ModuleType:
    spec = importlib.util.spec_from_file_location("workspace", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ws = load_script()


def entry(slug: str, corpus: str, **overrides: Any) -> dict[str, Any]:
    data: dict[str, Any] = dict(
        slug=slug,
        pdf=f"data/{corpus}/{slug}.pdf",
        source_title=f"Title of {slug}",
        source_type="peer_reviewed_paper",
        publisher="A Publisher",
        doi=None,
    )
    data.update(overrides)
    return data


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A repository with the real evaluations/ template and empty corpora."""
    root = tmp_path / "repo"
    shutil.copytree(REPO_ROOT / "evaluations", root / "evaluations")
    for overlay in ws.OVERLAYS.values():
        for source in filter(None, overlay.values()):
            (root / source).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO_ROOT / source, root / source)
    for corpus in ws.CORPORA:
        (root / "data" / corpus).mkdir(parents=True)
        write_sources(root, corpus, [])
    return root


def write_sources(repo: Path, corpus: str, entries: list[dict[str, Any]], pages: int = 1) -> None:
    """Write sources.yaml and, for each entry, a PDF whose page N reads '<slug> page N'."""
    text = yaml.safe_dump({"sources": entries}, sort_keys=False)
    (repo / "data" / corpus / "sources.yaml").write_text(text, encoding="utf-8")
    for item in entries:
        with pymupdf.open() as doc:
            for number in range(1, pages + 1):
                doc.new_page().insert_text((72, 72), f"{item['slug']} page {number}")
            doc.save(repo / item["pdf"])


def test_load_puts_the_source_and_its_details_in_a_fresh_workspace(
    repo: Path, tmp_path: Path
) -> None:
    write_sources(repo, "popular-press", [entry("hanford_2022", "popular-press", doi="10.1/x")])
    workspace = tmp_path / "workspace"

    ws.load(repo, workspace, "hanford_2022")

    source_pdf = repo / "data" / "popular-press" / "hanford_2022.pdf"
    assert (workspace / "article.pdf").read_bytes() == source_pdf.read_bytes()
    assert yaml.safe_load((workspace / "source.yaml").read_text()) == {
        "source_title": "Title of hanford_2022",
        "source_type": "peer_reviewed_paper",
        "publisher": "A Publisher",
        "doi": "10.1/x",
    }
    assert (workspace / "prompts" / "close-reading.md").is_file()
    assert (workspace / "RUBRIC.md").is_file()
    loaded = yaml.safe_load((workspace / ws.LOADED).read_text())
    assert loaded == {"corpus": "popular-press", "slug": "hanford_2022"}


def test_load_writes_the_text_and_an_image_of_each_page_in_order(
    repo: Path, tmp_path: Path
) -> None:
    write_sources(repo, "legislation", [entry("long", "legislation")], pages=10)
    workspace = tmp_path / "workspace"

    ws.load(repo, workspace, "long")

    text = (workspace / "article.txt").read_text()
    assert text.index("--- page 1 ---") < text.index("long page 1") < text.index("--- page 2 ---")
    assert "long page 10" in text
    images = sorted(p.name for p in (workspace / "pages").iterdir())
    assert images == [f"page-{n:02d}.png" for n in range(1, 11)]
    with pymupdf.open(workspace / "pages" / "page-01.png") as image:
        assert image.page_count == 1


def test_load_removes_zero_width_spaces_from_the_text(repo: Path, tmp_path: Path) -> None:
    write_sources(repo, "legislation", [entry("mn", "legislation")])
    with pymupdf.open() as doc:
        doc.new_page().insert_text((72, 72), "Read​ Act", fontname="china-s")
        doc.save(repo / "data" / "legislation" / "mn.pdf")
    workspace = tmp_path / "workspace"

    ws.load(repo, workspace, "mn")

    text = (workspace / "article.txt").read_text()
    assert "Read Act" in text
    assert "​" not in text


def test_load_refuses_a_file_that_is_not_a_pdf_and_creates_nothing(
    repo: Path, tmp_path: Path
) -> None:
    write_sources(repo, "scholarly", [entry("bad", "scholarly")])
    (repo / "data" / "scholarly" / "bad.pdf").write_bytes(b"not a pdf")
    workspace = tmp_path / "workspace"
    with pytest.raises(ws.WorkspaceError, match="could not be read as a PDF"):
        ws.load(repo, workspace, "bad")
    assert not workspace.exists()


def test_load_gives_legislation_its_own_prompts_rubric_and_codebook(
    repo: Path, tmp_path: Path
) -> None:
    write_sources(repo, "legislation", [entry("ca_2025", "legislation")])
    workspace = tmp_path / "workspace"

    ws.load(repo, workspace, "ca_2025")

    for target, source in ws.OVERLAYS["legislation"].items():
        if source is None:
            assert not (workspace / target).exists()
        else:
            assert (workspace / target).read_bytes() == (repo / source).read_bytes()


def test_load_leaves_other_corpora_on_the_article_template(repo: Path, tmp_path: Path) -> None:
    write_sources(repo, "scholarly", [entry("a", "scholarly")])
    workspace = tmp_path / "workspace"

    ws.load(repo, workspace, "a")

    assert (workspace / "RUBRIC.md").read_bytes() == (repo / "evaluations/RUBRIC.md").read_bytes()
    assert (workspace / "prompts" / "evaluate-argument.md").is_file()
    assert not (workspace / "CODEBOOK.md").exists()


def test_load_refuses_an_unknown_slug_and_creates_nothing(repo: Path, tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    with pytest.raises(ws.WorkspaceError, match="no source with slug"):
        ws.load(repo, workspace, "missing")
    assert not workspace.exists()


def test_load_refuses_a_slug_used_in_two_corpora(repo: Path, tmp_path: Path) -> None:
    write_sources(repo, "scholarly", [entry("dup", "scholarly")])
    write_sources(repo, "legislation", [entry("dup", "legislation")])
    with pytest.raises(ws.WorkspaceError, match="scholarly, legislation"):
        ws.load(repo, tmp_path / "workspace", "dup")


def test_load_refuses_a_missing_pdf_and_creates_nothing(repo: Path, tmp_path: Path) -> None:
    write_sources(repo, "scholarly", [entry("gone", "scholarly")])
    (repo / "data" / "scholarly" / "gone.pdf").unlink()
    workspace = tmp_path / "workspace"
    with pytest.raises(ws.WorkspaceError, match="not found"):
        ws.load(repo, workspace, "gone")
    assert not workspace.exists()


def test_load_leaves_an_existing_workspace_untouched(repo: Path, tmp_path: Path) -> None:
    write_sources(repo, "scholarly", [entry("a", "scholarly"), entry("b", "scholarly")])
    workspace = tmp_path / "workspace"
    ws.load(repo, workspace, "a")
    with pytest.raises(ws.WorkspaceError, match="already exists"):
        ws.load(repo, workspace, "b")
    source_pdf = repo / "data" / "scholarly" / "a.pdf"
    assert (workspace / "article.pdf").read_bytes() == source_pdf.read_bytes()


def test_save_copies_the_results_and_removes_the_workspace(repo: Path, tmp_path: Path) -> None:
    write_sources(repo, "legislation", [entry("az_2022", "legislation")])
    workspace = tmp_path / "workspace"
    ws.load(repo, workspace, "az_2022")
    (workspace / "run" / "analysis.json").write_text("{}")
    (workspace / "judgments" / "close_reading.md").write_text("judged")
    (workspace / "scores.md").write_text("scores")

    dest = ws.save(repo, workspace)

    assert dest == repo / "outputs" / "legislation" / "az_2022"
    assert (dest / "run" / "analysis.json").read_text() == "{}"
    assert (dest / "judgments" / "close_reading.md").read_text() == "judged"
    assert (dest / "scores.md").read_text() == "scores"
    assert (dest / "references").is_dir()
    assert not list(dest.rglob(".gitkeep"))
    assert not (dest / "article.pdf").exists()
    assert not workspace.exists()


def test_save_will_not_overwrite_earlier_results(repo: Path, tmp_path: Path) -> None:
    write_sources(repo, "scholarly", [entry("a", "scholarly")])
    workspace = tmp_path / "workspace"
    (repo / "outputs" / "scholarly" / "a").mkdir(parents=True)
    ws.load(repo, workspace, "a")
    with pytest.raises(ws.WorkspaceError, match="already exists"):
        ws.save(repo, workspace)
    assert workspace.exists()


def test_save_refuses_when_nothing_is_loaded(repo: Path, tmp_path: Path) -> None:
    with pytest.raises(ws.WorkspaceError, match="no source is loaded"):
        ws.save(repo, tmp_path / "workspace")


def test_the_repository_sources_files_are_readable() -> None:
    with pytest.raises(ws.WorkspaceError, match="no source with slug"):
        ws.find_source(REPO_ROOT / "data", "no_such_slug")
