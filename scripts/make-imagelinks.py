#!/usr/bin/env python3
"""Make image links in Jupyter notebook files."""
import re
import urllib.request
from pathlib import Path
from typing import Match, Sequence

repo = "tueda/PS2022SS"


def check_url(url: str) -> bool:
    """Check if the given URL is available."""
    if not url.lower().startswith("http"):
        return False
    try:
        return (  # type: ignore[no-any-return]
            urllib.request.urlopen(url).getcode()  # noqa: S310; checked in the above
            == 200
        )
    except urllib.error.HTTPError:
        return False


def make_links(input_lines: Sequence[str]) -> Sequence[str]:
    """Resolve image links in Markdown."""
    output_lines = []
    for line in input_lines:
        line = re.sub(
            r"!\[([^\]]+)\]\((images/[^/)]+)\)",
            _replace,
            line,
        )
        output_lines.append(line)
    return output_lines


def _replace(m: Match[str]) -> str:
    repo_parts = repo.split("/", 1)
    image_url = (
        f"https://{repo_parts[0]}.github.io/{repo_parts[1]}/notebooks/{m.group(2)}"
    )
    if check_url(image_url):
        return f"![{m.group(1)}]({image_url})"
    else:
        return f"![{m.group(1)}]({m.group(2)})"


def process_file(path: Path) -> None:
    """Process the specified file."""
    input_lines = path.read_text().splitlines()
    output_lines = make_links(input_lines)
    if input_lines != output_lines:
        print(f"image link resolved: {path}")
        path.write_text("\n".join(output_lines) + "\n")


def main() -> None:
    """Entry point."""
    for path in Path("notebooks").glob("*.ipynb"):
        process_file(path)


if __name__ == "__main__":
    main()
