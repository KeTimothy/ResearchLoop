from pathlib import Path

import pymupdf


def extract_pdf_text(pdf_path: str | Path) -> list[dict]:
    """Extract text page by page, preserving stable page references."""
    pdf_path = Path(pdf_path)

    pages = []

    with pymupdf.open(pdf_path) as document:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()

            if not text:
                continue

            pages.append(
                {
                    "source_file": pdf_path.name,
                    "page_number": page_number,
                    "text": text,
                }
            )

    return pages