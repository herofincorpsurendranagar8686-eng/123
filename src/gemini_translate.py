import os
import time
from google import genai
from google.genai import errors

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

PROMPT = """
Translate this single PDF page into Gujarati.

STRICT:
- Word by word
- No addition
- No deletion
- Keep formulas, numbers, tables and symbols unchanged.
- Return only Gujarati text.
"""

def translate_page(pdf_path):
    file = client.files.upload(file=pdf_path)

    while True:
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[file, PROMPT]
            )

            if response.text:
                return response.text

            time.sleep(5)

        except errors.ServerError:
            print("⏳ Gemini busy (503). Retrying in 30 sec...")
            time.sleep(30)

        except errors.ClientError as e:
            if e.code == 429:
                print("⏳ Rate limit. Waiting 60 sec...")
                time.sleep(60)
            else:
                raise
