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

print(prompt)