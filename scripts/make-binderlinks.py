#!/usr/bin/env python3
"""Make links for BinderHubs."""
import re
import urllib.parse
from pathlib import Path
from typing import Optional, Sequence

repo = "tueda/PS2022SS"


def make_link(string: str, branch: str, notebook: str, use_extension: bool) -> str:
    """Return the string with BinderHub links for the notebook."""
    filepath = urllib.parse.quote(notebook)
    filename = Path(notebook).name

    download_alt = "Download ipynb"
    binder_alt = "Launch Binder"
    colab_alt = "Open In Colab"

    download_image = (
        "https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter"
    )
    binder_image = "https://mybinder.org/badge_logo.svg"
    colab_image = "https://colab.research.google.com/assets/colab-badge.svg"

    preview_url = f"https://nbviewer.jupyter.org/github/{repo}/blob/{branch}/{filepath}"
    download_url = filepath  # relative URL
    binder_url = f"https://mybinder.org/v2/gh/{repo}/{branch}?filepath={filepath}"
    colab_url = (
        f"https://colab.research.google.com/github/"
        f"{repo}/blob/{branch}/{filepath}?hl=ja"
    )

    download_attr = f"{{: download={filename}}}" if use_extension else ""

    if use_extension:
        # HACK: for blob/gh-pages/index.md
        preview_url = f"previews/{Path(notebook).stem}.html"

    if not use_extension:
        # HACK: for blob/develop/notebooks/index.md
        # TODO: clicking this URL doesn't start downloading, just shows the raw content.
        download_url = (
            f"https://raw.githubusercontent.com/{repo}/{branch}/{download_url}"
        )

    return (
        f"[{string}]({preview_url})"
        f" [![{download_alt}]({download_image})]({download_url}){download_attr}"
        f" [![{binder_alt}]({binder_image})]({binder_url})"
        f" [![{colab_alt}]({colab_image})]({colab_url})"
    )


def make_contents(
    input_lines: Sequence[str],
    branch: str,
    notebook_src_dir: str,
    notebook_dest_dir: str,
    use_extension: bool = True,
) -> Sequence[str]:
    """Make page contents."""
    # List notebook files.
    notebooks = sorted(
        f"{notebook_dest_dir}/{f.name}"
        for f in Path(notebook_src_dir).iterdir()
        if f.suffix.lower() == ".ipynb"
    )
    # dict for TITLE -> DESTDIR/NN_TITLE.ipynb
    notebook_links = {re.sub(r"^.*_|\.ipynb$", "", f): f for f in notebooks}

    output_lines = []
    for line in input_lines:
        # Find bullet/numbered list items.
        m = re.match(r"^(-|\*|\d+\.)\s+\[(\S+)\]", line)
        if not m:
            m = re.match(r"^(-|\*|\d+\.)\s+(\S+)", line)
        if m:
            prelude = m.group(1)
            title = m.group(2)
            # Make a link, if the target exists.
            if title in notebook_links:
                linked_title = make_link(
                    title, branch, notebook_links[title], use_extension
                )
                line = f"{prelude} {linked_title}"

        output_lines.append(line)
    return output_lines


def process_file(
    md_filename: str,
    branch: str,
    notebook_src_dir: str,
    notebook_dest_dir: Optional[str] = None,
    use_extension: bool = False,
) -> None:
    """Process the specified Markdown file."""
    if notebook_dest_dir is None:
        notebook_dest_dir = notebook_src_dir

    path = Path(md_filename)
    input_lines = path.read_text().splitlines()
    output_lines = make_contents(
        input_lines, branch, notebook_src_dir, notebook_dest_dir, use_extension
    )

    if input_lines != output_lines:
        print(f"patch {path}")
        path.write_text("\n".join(output_lines) + "\n")


def main() -> None:
    """Entry point."""
    process_file("DEVELOPMENT.md", "develop", "notebooks")
    process_file(
        "docs/index.md", "gh-pages", "docs/notebooks", "notebooks", use_extension=True
    )


if __name__ == "__main__":
    main()
