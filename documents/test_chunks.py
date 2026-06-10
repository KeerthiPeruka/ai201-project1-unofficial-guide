from pipeline.load import load_documents
from pipeline.clean import clean_text
from pipeline.chunk import chunk_text

docs = load_documents()
all_chunks = []

for doc in docs:
    cleaned = clean_text(doc["text"])
    chunks = chunk_text(cleaned, doc["source"])
    all_chunks.extend(chunks)

print(f"Loaded documents: {len(docs)}")
print(f"Total chunks: {len(all_chunks)}")

print("\nSample chunks:\n")

for chunk in all_chunks[:5]:
    print("SOURCE:", chunk["source"])
    print("CHUNK ID:", chunk["chunk_id"])
    print("TEXT:", chunk["text"])
    print("-" * 50)