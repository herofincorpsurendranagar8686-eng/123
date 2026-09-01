from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
import os

FONT = "Helvetica"

if os.path.exists("fonts/NotoSansGujarati-Regular.ttf"):
    pdfmetrics.registerFont(TTFont("Gujarati", "fonts/NotoSansGujarati-Regular.ttf"))
    FONT = "Gujarati"

style = getSampleStyleSheet()["BodyText"]
style.fontName = FONT
style.leading = 18

def build_pdf(text: str, output_file: str):
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(output_file)

    story = [
        Paragraph(text.replace("\n", "<br/>"), style)
    ]

    doc.build(story)
