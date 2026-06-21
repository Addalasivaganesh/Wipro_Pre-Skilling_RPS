def estimate_tokens(text: str) -> int:
    return int(len(text.split())/ 0.75)

document = """siva ganesh """ * 1000

tokens = estimate_tokens(document)
print("Estimated_tokens" , tokens)
