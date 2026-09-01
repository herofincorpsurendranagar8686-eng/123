from pathlib import Path
from gemini_translate import translate_page
from rebuild_pdf import build_pdf

INPUT = Path("input")
OUTPUT = Path("output")

OUTPUT.mkdir(exist_ok=True)

files = sorted(INPUT.glob("source-*.pdf"))

for pdf in files:

    out_pdf = OUTPUT / pdf.name
    txt = OUTPUT / pdf.with_suffix(".txt").name

    if out_pdf.exists():
        continue

    print(f"Translating {pdf.name}")

    result = translate_page(str(pdf))

    txt.write_text(result, encoding="utf-8")

    build_pdf(result, str(out_pdf))

    print(f"Saved {out_pdf.name}")

    # ONLY ONE PDF PER RUN
    break

print("Done")
