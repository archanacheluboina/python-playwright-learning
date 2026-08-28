import tempfile
import unittest
import zipfile
from pathlib import Path

from word_count_agent import count_words, find_document


class WordCountAgentTests(unittest.TestCase):
    def test_counts_words_in_docx_text(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            document_path = Path(temporary_directory) / "sample.docx"
            document_xml = """<?xml version="1.0" encoding="UTF-8"?>
            <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
              <w:body>
                <w:p><w:r><w:t>Hello world</w:t></w:r></w:p>
                <w:p><w:r><w:t>It's a test</w:t></w:r></w:p>
              </w:body>
            </w:document>"""
            with zipfile.ZipFile(document_path, "w") as archive:
                archive.writestr("word/document.xml", document_xml)

            self.assertEqual(count_words(document_path), 5)

    def test_finds_docx_in_folder(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory)
            (folder / "~$open.docx").touch()
            expected = folder / "report.docx"
            expected.touch()

            self.assertEqual(find_document(folder), expected)


if __name__ == "__main__":
    unittest.main()
