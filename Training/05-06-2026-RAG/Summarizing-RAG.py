import os

from anthropic import Anthropic
from anthropic.types import MessageParam, TextBlock
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

MODEL = "claude-sonnet-4-6"

document = """
A healthcare group operates
multiple clinics...
""" * 20

messages: list[MessageParam] = [
    {
        "role": "user",
        "content": f"""
Summarize this document.

{document}
"""
    }
]

response = client.messages.create(
    model=MODEL,
    max_tokens=1000,
    messages=messages
)

block = response.content[0]

if isinstance(block, TextBlock):

    print(block.text)


















    #Chunking