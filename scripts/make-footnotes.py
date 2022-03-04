#!/usr/bin/env python3
"""Make footnotes in Jupyter notebook files."""
import re
from pathlib import Path
from typing import Match, Sequence


def make_footnotes(input_lines: Sequence[str]) -> Sequence[str]:
    """Make footnotes in Markdown."""
    # Translation to HTML footnotes.
    # See https://github.com/jupyter/notebook/issues/1287.
    # We need to handle, for example,
    #   This is a footnote[^1].
    #   [^1]: The footnote text.
    output_lines = []
    for line in input_lines:
        line = re.sub(
            r"(?<!`)\[\^([^\]]+)\]\s*:",
            r'<span id=\\"cite_note-\1\\">\1.</span> [^](#cite_ref-\1)',
            line,
        )
        line = re.sub(
            r"(?<!`)\[\^([^\]]+)\]",
            r'[<sup id=\\"cite_ref-\1\\">[\1]</sup>](#cite_note-\1)',
            line,
        )
        output_lines.append(line)

    input_lines = output_lines

    # Relabel footnotes.
    n = 1
    relabeling = {}
    for line in input_lines:
        labels = re.findall(
            r'<sup id=\\"cite_ref-([^\\]+)\\">\[\1\]</sup>\]\(#cite_note-\1\)', line
        )
        for i in labels:
            relabeling[i] = str(n)
            n += 1

    if relabeling:

        def f1(m: Match[str]) -> str:
            n = relabeling[m.group(1)]
            return rf"<sup id=\"cite_ref-{n}\">[{n}]</sup>](#cite_note-{n})"

        def f2(m: Match[str]) -> str:
            n = relabeling[m.group(1)]
            return rf"<span id=\"cite_note-{n}\">{n}.</span> [^](#cite_ref-{n})"

        output_lines = []
        for line in input_lines:
            line = re.sub(
                r'<sup id=\\"cite_ref-([^\\]+)\\">\[\1\]</sup>\]\(#cite_note-\1\)',
                f1,
                line,
            )
            line = re.sub(
                r'<span id=\\"cite_note-([^\\]+)\\">\1\.\s*</span>\s*'
                + r"\[\^\]\(#cite_ref-\1\)",
                f2,
                line,
            )
            output_lines.append(line)

    return output_lines


def process_file(path: Path) -> None:
    """Process the specified file."""
    input_lines = path.read_text().splitlines()
    output_lines = make_footnotes(input_lines)
    if input_lines != output_lines:
        print(f"patch {path}")
        path.write_text("\n".join(output_lines) + "\n")


def main() -> None:
    """Entry point."""
    for path in Path("notebooks").glob("*.ipynb"):
        process_file(path)


if __name__ == "__main__":
    main()
