from pathlib import Path
from rebuild_pdf import build_pdf

INPUT=Path("input")
OUTPUT=Path("output")

OUTPUT.mkdir(exist_ok=True)

files=sorted(INPUT.glob("source-*.txt"))

for txt in files:

    pdf=OUTPUT/f"{txt.stem}.pdf"

    if pdf.exists():
        continue

    text=txt.read_text(encoding="utf-8")

    num=int(txt.stem.split("-")[1])

    build_pdf(text,str(pdf),num)

    print("Created",pdf.name)

    break
