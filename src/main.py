from pathlib import Path
from gemini_translate import translate_page
from rebuild_pdf import build_pdf

INPUT = Path("input")
OUTPUT = Path("output")

OUTPUT.mkdir(exist_ok=True)

for pdf in sorted(INPUT.glob("source-*.pdf")):

    out_pdf = OUTPUT / pdf.name

    if out_pdf.exists():
        continue

    print("Translating:", pdf.name)

    text = translate_page(str(pdf))

    build_pdf(text, str(out_pdf))

    print("Saved:", out_pdf)

    break
