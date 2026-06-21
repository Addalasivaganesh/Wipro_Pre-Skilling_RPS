def chunk_with_overlap(
    text,
    chunk_size,
    overlap
):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = words[start:end]

        chunks.append(
            " ".join(chunk)
        )

        start += (
            chunk_size - overlap
        )

    return chunks


document = """
AI is transforming healthcare.
""" * 100

chunks = chunk_with_overlap(
    document,
    chunk_size=30,
    overlap=10
)

print("Chunks:", len(chunks))

print(chunks[0])