
from modules.pdf_generator import generar_pdf_reporte
from modules.sheets import worksheet, agregar_venta_a_sheets, registrar_encargo_en_sheets

def cargar_venta_manual():
    print("📦 Función para cargar venta manual iniciada.")
    # Aquí deberías implementar la lógica de ingreso manual de ventas
    # Por ejemplo, con un diálogo para ingresar título, precio de venta, etc.
    # y luego llamar a agregar_venta_a_sheets con los datos

def generar_reporte_pdf():
    print("📝 Generando reporte PDF...")

    data = worksheet.get_all_values()
    if not data:
        print("⚠️ No hay datos en el sheet.")
        return

    headers = data[0]
    rows = data[1:]

    generar_pdf_reporte(headers, rows)

def registrar_encargo():
    print("📬 Función para registrar encargo iniciada.")
    # Aquí podrías abrir un diálogo para ingresar título/tema solicitado
    # y luego llamar a registrar_encargo_en_sheets con esos datos
