
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(nombre_archivo, data, logo_path=None):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    text = c.beginText(40, height - 50)
    for linea in data:
        text.textLine(linea)
    c.drawText(text)
    if logo_path:
        c.drawImage(logo_path, width // 2 - 50, 30, width=100, preserveAspectRatio=True)
    c.save()
