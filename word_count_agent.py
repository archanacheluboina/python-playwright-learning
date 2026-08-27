"""Count words in a Microsoft Word .docx file."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree

WORD_PATTERN = re.compile(r"\b[\w]+(?:['-][\w]+)*\b", re.UNICODE)
WORD_NAMESPACE = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
DEFAULT_FOLDER = Path(
    r"C:\Users\91989\Desktop\Archu\PTL-Github-Python-Playwright\Playwright\Agents\Agent-WordCountSinglefile"
)


def count_words(document_path: Path) -> int:
    """Return the number of words in the visible text of a .docx file."""
    with zipfile.ZipFile(document_path) as document:
        document_xml = document.read("word/document.xml")

    root = ElementTree.fromstring(document_xml)
    text_parts = [
        node.text or ""
        for node in root.iter(f"{WORD_NAMESPACE}t")
    ]
    return len(WORD_PATTERN.findall(" ".join(text_parts)))


def find_document(folder: Path) -> Path:
    """Find the first .docx file in a folder, excluding temporary Word files."""
    documents = sorted(
        path for path in folder.glob("*.docx") if not path.name.startswith("~$")
    )
    if not documents:
        raise FileNotFoundError(f"No .docx file found in: {folder}")
    return documents[0]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Count words in a Word .docx file or a folder containing one."
    )
    parser.add_argument(
        "location",
        type=Path,
        nargs="?",
        default=DEFAULT_FOLDER,
        help="Path to a .docx file or folder; defaults to the configured agent folder",
    )
    args = parser.parse_args()

    location = args.location.expanduser()
    try:
        document_path = (
            location
            if location.is_file()
            else find_document(location)
        )
        if document_path.suffix.lower() != ".docx":
            raise ValueError("The input must be a .docx file or a folder containing one")
        print(f"File: {document_path.name}")
        print(f"Word count: {count_words(document_path)}")
    except (FileNotFoundError, NotADirectoryError, ValueError, zipfile.BadZipFile) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
