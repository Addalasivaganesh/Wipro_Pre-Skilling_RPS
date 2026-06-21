# MODULE 08 - PROMPTS

# ZERO SHOT
zero_shot = """
Classify this resume:
Python, Machine Learning, Azure
"""

# ONE SHOT
one_shot = """
Resume: Java, Spring
Role: Backend Developer

Resume: React, Angular
Role:
"""

# FEW SHOT
few_shot = """
Resume: Python, NLP -> AI Engineer
Resume: Java, Spring -> Backend Developer
Resume: React, Angular -> Frontend Developer

Resume: SQL, Power BI ->
"""

print("Zero Shot:\n", zero_shot)
print("One Shot:\n", one_shot)
print("Few Shot:\n", few_shot)