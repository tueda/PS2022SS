"""Convert notebooks into different formats."""

import logging
import time
from pathlib import Path
from typing import Any

import joblib
import nbconvert
import nbformat

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

memory = joblib.Memory(".cache", verbose=0)


@memory.cache  # type: ignore[misc]
def convert_notebook(title: str, contents: str, fmt: str) -> str:
    """Convert a notebook into another format."""
    nb = nbformat.reads(contents, as_version=4)
    nb.metadata["title"] = title

    if fmt == "html":
        html_exporter = nbconvert.HTMLExporter()
        html_exporter.template_name = "lab"
        html_body, html_resources = html_exporter.from_notebook_node(nb)
        return html_body  # type: ignore[no-any-return]

    if fmt == "md":
        md_exporter = nbconvert.MarkdownExporter()
        md_body, md_resources = md_exporter.from_notebook_node(nb)
        return md_body  # type: ignore[no-any-return]

    raise ValueError(f"format {fmt} unsupported")


def convert(notebook_dir: Path, dest_dir: Path, fmt: str, clear: bool = True) -> None:
    """Convert notebooks into another format."""
    n_jobs = 1  # seems be fast enough for now

    if fmt == "html":
        fmt_name = "HTML"
    elif fmt == "md":
        fmt_name = "Markdown"
    else:
        raise ValueError(f"format {fmt} unsupported")

    t1 = time.time()

    if clear:
        # Clear the destination directory.
        dest_dir.mkdir(exist_ok=True)
        for child in dest_dir.glob("*"):
            if child.is_file():
                child.unlink()

    # Collect .ipynb files to be converted.

    target_files = []

    for child in notebook_dir.glob("*"):
        if child.is_file() and child.suffix == ".ipynb":
            target_files.append(child)

    # Convert the .ipynb files.

    def run(target: Path) -> None:
        result = convert_notebook(target.stem, target.read_text(), fmt)
        dest_file = dest_dir / target.with_suffix("." + fmt).name
        if dest_file.is_file() and dest_file.read_text() == result:
            return
        dest_file.write_text(result)

    if target_files:
        dest_dir.mkdir(exist_ok=True)
        joblib.Parallel(n_jobs=n_jobs)(joblib.delayed(run)(f) for f in target_files)

    t2 = time.time()

    logger.info(f"Notebooks converted to {fmt_name} in {t2 - t1:.3f} seconds")


def nb2html(*args: Any, **kwargs: Any) -> None:
    """Generate HTML files from notebooks for previews."""
    docs_dir = Path(kwargs["config"]["docs_dir"])

    notebook_dir = docs_dir / "notebooks"
    preview_dir = docs_dir / "previews"

    convert(notebook_dir, preview_dir, "html", clear=True)


def nb2md() -> None:
    """Generate Markdown files from notebooks for textlint."""
    root_dir = Path(".")

    notebook_dir = root_dir / "notebooks"
    dest_dir = root_dir / ".converted"

    convert(notebook_dir, dest_dir, "md", clear=False)
