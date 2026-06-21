

text = "HELLO"

encrypted = ""

for ch in text:
    encrypted += chr(ord(ch) + 4)

print(encrypted)