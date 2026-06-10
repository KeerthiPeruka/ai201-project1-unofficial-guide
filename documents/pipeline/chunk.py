def chunk_text(text, source, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append({
                "id": f"{source}_{chunk_id}",
                "source": source,
                "chunk_id": chunk_id,
                "text": chunk
            })

        chunk_id += 1
        start += chunk_size - overlap

    return chunks