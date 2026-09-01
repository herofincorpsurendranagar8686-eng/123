import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

PROMPT = """
Translate this single PDF page into Gujarati.
No addition.
No deletion.
Keep numbers and formulas unchanged.
"""

def translate_page(pdf_path):
    f = client.files.upload(file=pdf_path)

    r = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[f, PROMPT]
    )

    return r.text
