"""Fast checks that do not call Mistral or download an embedding model."""

from __future__ import annotations

from pathlib import Path

from src.classifier import classify_query


SOURCE_PDF_DIR = Path(__file__).resolve().parent / "data" / "source_pdfs"


SAMPLES = {
    "What attendance do I need for the exam?": "academic",
    "When is my tuition fee due?": "fee",
    "Hello, what can you do?": "general",
}


def main() -> None:
    missing_pdfs = [
        name
        for name in ("northstar_academic_guide.pdf", "northstar_fee_guide.pdf")
        if not (SOURCE_PDF_DIR / name).exists()
    ]
    if missing_pdfs:
        raise SystemExit(f"Missing sample PDFs: {', '.join(missing_pdfs)}")

    for question, expected in SAMPLES.items():
        actual = classify_query(question)
        print(f"{actual:8} | {question}")
        if actual != expected:
            raise SystemExit(f"Expected {expected!r}; received {actual!r}")

    print("Smoke test passed.")


if __name__ == "__main__":
    main()
