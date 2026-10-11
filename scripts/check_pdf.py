from pathlib import Path

from researchloop.ingestion.pdf import extract_pdf_text

PAPER_DIR = Path("data/raw/papers")


def main() -> None:
    pdf_files = sorted(PAPER_DIR.glob("*.pdf"))

    if not pdf_files:
        print(f"No PDF found in {PAPER_DIR.resolve()}")
        return

    for pdf_path in pdf_files:
        pages = extract_pdf_text(pdf_path)
        total_chars = sum(len(page["text"]) for page in pages)

        print(
            f"{pdf_path.name}: "
            f"{len(pages)} text pages, "
            f"{total_chars:,} characters"
        )

        if total_chars == 0:
            print("  WARNING: no extractable text; inspect this PDF.")


if __name__ == "__main__":
    main()