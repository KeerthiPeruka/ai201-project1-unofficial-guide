from pathlib import Path

RAW_DIR = Path("data")

def load_documents():
    documents = []

    for file_path in RAW_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "source": file_path.name,
            "text": text
        })

    return documents