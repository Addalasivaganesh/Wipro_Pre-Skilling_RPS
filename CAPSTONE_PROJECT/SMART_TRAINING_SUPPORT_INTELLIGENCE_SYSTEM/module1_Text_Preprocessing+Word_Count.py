import string

def preprocess(text: str):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Tokenization
    tokens = text.split()
    # Word count
    word_count = len(tokens)
    return tokens, word_count
user_input = input("Enter the message: ")

tokens, count = preprocess(user_input)

print("Preprocessed Tokens:", tokens)
print("Word Count:", count)