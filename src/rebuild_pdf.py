from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

FONT = "Helvetica"

if os.path.exists("fonts/NotoSansGujarati-Regular.ttf"):
    pdfmetrics.registerFont(
        TTFont("Gujarati", "fonts/NotoSansGujarati-Regular.ttf")
    )
    FONT = "Gujarati"

style = getSampleStyleSheet()["BodyText"]
style.fontName = FONT
style.leading = 18

def build_pdf(text, output_file):
    doc = SimpleDocTemplate(output_file)

    story = [
        Paragraph(text.replace("\n", "<br/>"), style)
    ]

    doc.build(story)
