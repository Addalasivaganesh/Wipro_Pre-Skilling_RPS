documents = [
    "Leave policy allows 30 days leave.",
    "Office timings are 9 AM to 6 PM"
    "Medical insurance covers family Members"
]

question = "How many leave days are allowed ?"

for doc in documents:
    if "leave" in doc.lower():
        retreived_document = doc
        break
print(retreived_document)
