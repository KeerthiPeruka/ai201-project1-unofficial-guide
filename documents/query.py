import os
import chromadb
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

load_dotenv()

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "tech_careers"

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(COLLECTION_NAME)

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def retrieve(query, top_k=4):
    query_embedding = model.encode([query]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    chunks = []

    for i in range(len(results["documents"][0])):
        chunks.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "chunk_id": results["metadatas"][0][i]["chunk_id"],
            "distance": results["distances"][0][i]
        })

    return chunks

def ask(question):
    chunks = retrieve(question)

    context = "\n\n".join(
        f"Source: {chunk['source']} | Chunk {chunk['chunk_id']}\n{chunk['text']}"
        for chunk in chunks
    )

    prompt = f"""
You are answering questions using a retrieval system.

Rules:
1. Use ONLY the information in the provided context.
2. Do NOT use outside knowledge.
3. If the answer is not contained in the context, say:
   "I don't have enough information to answer that."
4. Give a concise answer.
5. End with a Sources section listing document names used.

Context:
{context}

Question:
{question}
"""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a grounded RAG assistant. Only answer from the provided context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens = 500
    )

    answer = response.choices[0].message.content

    sources = sorted(set(chunk["source"] for chunk in chunks))

    return {
        "answer": answer,
        "sources": sources,
        "chunks": chunks
    }

if __name__ == "__main__":
    question = input("Ask a question: ")
    result = ask(question)

    print("\nAnswer:\n")
    print(result["answer"])

    print("\nSources:")
    for source in result["sources"]:
        print("-", source)

    print("\nRetrieved chunks:")
    for chunk in result["chunks"]:
        print(f"- {chunk['source']} chunk {chunk['chunk_id']} distance {chunk['distance']}")