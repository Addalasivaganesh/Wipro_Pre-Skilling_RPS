def chunk_text(
    text: str,
    chunk_size: int
):

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        20
    ):

        chunk = words[
            i:i+chunk_size
        ]

        chunks.append(
            " ".join(chunk)
        )

    return chunks


document = """
AI is changing healthcare.
""" * 200

chunks = chunk_text(
    document,
    20
)

print("Chunks:", len(chunks))

for index, chunk in enumerate(chunks[:3], start=1):

    print("\nChunk", index)

    print(chunk)