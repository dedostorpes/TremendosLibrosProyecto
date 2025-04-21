
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generar_pdf_reporte(ventas, archivo_salida="reporte_ventas.pdf"):
    if not ventas:
        print("No hay ventas para generar el reporte.")
        return

    c = canvas.Canvas(archivo_salida, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 10)

    margen_izquierdo = 40
    margen_superior = height - 40
    alto_linea = 15
    y = margen_superior

    c.drawString(margen_izquierdo, y, "REPORTE DE VENTAS - Tremendos Libros")
    y -= alto_linea * 2
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    c.drawString(margen_izquierdo, y, f"Fecha de generación: {fecha_actual}")
    y -= alto_linea * 2

    headers = ["Fecha", "Título", "Precio venta", "Proveedor", "Precio compra", "%", "Ganancia socio", "Saldo"]
    col_widths = [70, 150, 70, 90, 70, 30, 90, 60]

    # Encabezados
    x = margen_izquierdo
    for i, header in enumerate(headers):
        c.drawString(x, y, header)
        x += col_widths[i]
    y -= alto_linea

    for venta in ventas:
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = margen_superior

        x = margen_izquierdo
        for i, campo in enumerate(venta):
            texto = str(campo)
            if len(texto) > 35 and i == 1:
                texto = texto[:32] + "..."
            c.drawString(x, y, texto)
            x += col_widths[i]
        y -= alto_linea

    # Logo o firma final
    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, y, "Tremendos Libros")

    c.save()
    print(f"Reporte PDF generado: {archivo_salida}")
