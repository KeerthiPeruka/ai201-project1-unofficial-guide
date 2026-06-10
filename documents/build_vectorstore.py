import chromadb
from sentence_transformers import SentenceTransformer

from pipeline.load import load_documents
from pipeline.clean import clean_text
from pipeline.chunk import chunk_text

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "tech_careers"

print("Starting build...")

def build_vectorstore():
    docs = load_documents()
    all_chunks = []

    for doc in docs:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned, doc["source"])
        all_chunks.extend(chunks)

    print(f"Total chunks: {len(all_chunks)}")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(COLLECTION_NAME)

    texts = [chunk["text"] for chunk in all_chunks]
    ids = [chunk["id"] for chunk in all_chunks]
    metadatas = [
        {"source": chunk["source"], "chunk_id": chunk["chunk_id"]}
        for chunk in all_chunks
    ]

    embeddings = model.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    print("Vector store created successfully.")

if __name__ == "__main__":
    build_vectorstore()