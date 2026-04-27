from groq import Groq

import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ddr(merged_data):
    prompt = f"""
You are a senior building inspection analyst preparing a client-ready Detailed Diagnostic Report (DDR).

You MUST follow this structure exactly:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause (with reasoning)
4. Severity Assessment (with justification)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

Data:
{merged_data}

Instructions:

- Use ONLY the provided data. Do NOT invent details.
- Do NOT use vague phrases like "issue detected" or "not clear".
- Be specific and descriptive based on the input.

- If the same issue appears in multiple sources:
  → Merge them into one observation.

- If thermal data exists:
  → Use it as supporting evidence.

- If data conflicts:
  → Explicitly mention the conflict.

- If information is missing:
  → Write "Not Available" and include it in Missing Information section.

- Assign severity (Low / Moderate / Critical) based on impact and justify it.

- Use simple, client-friendly language.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content