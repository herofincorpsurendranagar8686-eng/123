import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

PROMPT = """
Translate ALL visible English text on this single PDF page into Gujarati.

STRICT RULES:
- Translate word by word.
- Do NOT add or remove content.
- Keep formulas, numbers and symbols unchanged.
- Return only the translated page text.
"""

def translate_page(pdf_path):
    uploaded = client.files.upload(file=pdf_path)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[uploaded, PROMPT]
    )

    if not response.text:
        raise Exception("Empty response from Gemini")

    return response.text
