system_prompt = 500
conversation = 5000
documents = 165000
response = 4000

total = (
    system_prompt +
    conversation +
    documents + 
    response
)
print(total)