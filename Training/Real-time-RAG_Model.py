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
Employees are entitled to 30 days annual leave.

Employees may carry forward 10 days.

Medical leave requires documentation.
"""

question = """
How many leave days are allowed?
"""

prompt = f"""
Answer ONLY from the provided document.

Document:
{document}

Question:
{question}
"""

messages: list[MessageParam] = [
    {
        "role": "user",
        "content": prompt
    }
]

response = client.messages.create(
    model=MODEL,
    max_tokens=500,
    messages=messages
)

block = response.content[0]

if isinstance(block, TextBlock):
    print(block.text)