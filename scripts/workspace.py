"""Load one source into the evaluations workspace, and save its results back.

The workspace is built from evaluations/ in a folder outside the repository,
so a Codex session working there cannot read other sources' runs or judgments.
Beside article.pdf, load writes the PDF's text (article.txt) and an image of
each page (pages/), so a session needs no PDF tools of its own.

    uv run python scripts/workspace.py load <slug>
    uv run python scripts/workspace.py save
"""

import argparse
import shutil
import sys
from pathlib import Path
from typing import Any

import pymupdf
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORKSPACE = Path.home() / "sor-workspace"
CORPORA = ("scholarly", "popular-press", "legislation")
# The fields the prompts read from source.yaml.
PROMPT_FIELDS = ("source_title", "source_type", "publisher", "doi")
# What save copies to outputs/<corpus>/<slug>/.
RESULTS = ("run", "references", "judgments", "scores.md")
# Written by load, read by save: which source the workspace holds.
LOADED = "loaded.yaml"
# Per corpus: workspace path -> repository file laid over the evaluations/
# template (None removes the template's file). Corpora not listed use the
# template as it is.
OVERLAYS: dict[str, dict[str, str | None]] = {
    "legislation": {
        "README.md": "prompts/legislation/README.md",
        "RUBRIC.md": "docs/RUBRIC_LEGISLATION.md",
        "CODEBOOK.md": "docs/CODEBOOK.md",
        "scores.md": "prompts/legislation/scores.md",
        "prompts/close-reading.md": "prompts/legislation/close-reading.md",
        "prompts/discourse-analysis.md": "prompts/legislation/discourse-analysis.md",
        "prompts/evaluate-argument.md": None,
    },
}
# Resolution of the page images: enough to read small print and see
# underlining and strikethrough.
PAGE_DPI = 150


class WorkspaceError(Exception):
    """A load or save that cannot go ahead; the message says why."""


def find_source(data_dir: Path, slug: str) -> tuple[str, dict[str, Any]]:
    """The corpus and sources.yaml entry for `slug`, which must be unique across corpora."""
    matches = []
    for corpus in CORPORA:
        text = (data_dir / corpus / "sources.yaml").read_text(encoding="utf-8")
        for entry in yaml.safe_load(text)["sources"]:
            if entry["slug"] == slug:
                matches.append((corpus, entry))
    if not matches:
        raise WorkspaceError(f"no source with slug {slug!r} in data/*/sources.yaml")
    if len(matches) > 1:
        corpora = ", ".join(corpus for corpus, _ in matches)
        raise WorkspaceError(f"slug {slug!r} appears in more than one entry: {corpora}")
    return matches[0]


def load(repo: Path, workspace: Path, slug: str) -> None:
    """Build the workspace from evaluations/ and put the source's PDF and details in it."""
    if workspace.exists():
        raise WorkspaceError(
            f"{workspace} already exists; save it (or remove it) before loading another source"
        )
    corpus, entry = find_source(repo / "data", slug)
    pdf = repo / entry["pdf"]
    if not pdf.is_file():
        raise WorkspaceError(f"{entry['pdf']} not found")
    try:
        document = pymupdf.open(pdf)
    except pymupdf.FileDataError as error:
        raise WorkspaceError(f"{entry['pdf']} could not be read as a PDF: {error}") from error

    with document:
        shutil.copytree(repo / "evaluations", workspace)
        for target, source in OVERLAYS.get(corpus, {}).items():
            if source is None:
                (workspace / target).unlink()
            else:
                shutil.copyfile(repo / source, workspace / target)
        shutil.copyfile(pdf, workspace / "article.pdf")
        write_text_and_pages(document, workspace)
    fields = {name: entry[name] for name in PROMPT_FIELDS}
    (workspace / "source.yaml").write_text(
        f"# The source in this workspace, from data/{corpus}/sources.yaml; the prompts read it.\n"
        + yaml.safe_dump(fields, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    (workspace / LOADED).write_text(
        yaml.safe_dump({"corpus": corpus, "slug": slug}, sort_keys=False), encoding="utf-8"
    )


def write_text_and_pages(document: pymupdf.Document, workspace: Path) -> None:
    """article.txt with each page's text under a page marker, and pages/page-N.png.

    Page numbers are zero-padded to the page count's width so the images sort in order.
    """
    width = len(str(document.page_count))
    pages_dir = workspace / "pages"
    pages_dir.mkdir()
    text = []
    for number, page in enumerate(document, start=1):
        text.append(f"--- page {number} ---\n{page.get_text()}")
        page.get_pixmap(dpi=PAGE_DPI).save(pages_dir / f"page-{number:0{width}d}.png")
    (workspace / "article.txt").write_text("\n".join(text), encoding="utf-8")


def save(repo: Path, workspace: Path) -> Path:
    """Copy the workspace's results to outputs/<corpus>/<slug>/, then remove the workspace."""
    marker = workspace / LOADED
    if not marker.is_file():
        raise WorkspaceError(f"no source is loaded in {workspace}")
    loaded = yaml.safe_load(marker.read_text(encoding="utf-8"))
    dest = repo / "outputs" / loaded["corpus"] / loaded["slug"]
    if dest.exists():
        raise WorkspaceError(f"{dest.relative_to(repo)} already exists; not overwriting it")

    dest.mkdir(parents=True)
    for name in RESULTS:
        source = workspace / name
        if source.is_dir():
            shutil.copytree(source, dest / name, ignore=shutil.ignore_patterns(".gitkeep"))
        else:
            shutil.copyfile(source, dest / name)
    shutil.rmtree(workspace)
    return dest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--workspace",
        type=Path,
        default=DEFAULT_WORKSPACE,
        help=f"where the workspace lives (default: {DEFAULT_WORKSPACE})",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    load_parser = commands.add_parser("load", help="put one source into the workspace")
    load_parser.add_argument("slug", help="the source's slug in data/<corpus>/sources.yaml")
    commands.add_parser("save", help="copy the results to outputs/ and remove the workspace")
    args = parser.parse_args(argv)

    try:
        if args.command == "load":
            load(REPO_ROOT, args.workspace, args.slug)
            print(f"Loaded {args.slug} into {args.workspace}")
        else:
            dest = save(REPO_ROOT, args.workspace)
            print(f"Saved to {dest.relative_to(REPO_ROOT)} and removed {args.workspace}")
    except WorkspaceError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
