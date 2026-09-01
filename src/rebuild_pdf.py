from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

if os.path.exists("fonts/NotoSansGujarati-Regular.ttf"):
    pdfmetrics.registerFont(TTFont("Gujarati","fonts/NotoSansGujarati-Regular.ttf"))
    FONT="Gujarati"
else:
    FONT="Helvetica"

styles=getSampleStyleSheet()
title=styles["Heading1"]
title.fontName=FONT
title.textColor=HexColor("#1D4ED8")

body=styles["BodyText"]
body.fontName=FONT
body.leading=18

def build_pdf(text, output_file, page_no):
    doc=SimpleDocTemplate(output_file)

    story=[]

    story.append(Paragraph(
        '<font color="#FFFFFF"><b>MATHS BY DC</b></font>',
        styles["Title"]
    ))

    story.append(Spacer(1,10))

    story.append(Paragraph(
        f'<font color="#1D4ED8"><b>ગુજરાતી આવૃત્તિ</b></font>',
        title
    ))

    story.append(Paragraph(
        f"<b>Page {page_no}</b>",
        body
    ))

    story.append(Spacer(1,12))

    story.append(Paragraph(
        text.replace("\n","<br/>"),
        body
    ))

    story.append(Spacer(1,20))

    story.append(Paragraph(
        '<font color="#2563EB"><b>www.mathsbydc.in</b></font>',
        body
    ))

    doc.build(story)
