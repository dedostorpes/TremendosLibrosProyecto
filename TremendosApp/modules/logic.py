
from modules.sheets import agregar_venta_a_sheets
from datetime import datetime

def cargar_venta_manual(datos, callback=None):
    try:
        venta = {
            "Fecha": datos.get("fecha", datetime.now().strftime("%Y-%m-%d")),
            "Título": datos["titulo"],
            "Método de pago": datos["metodo_pago"],
            "Comentarios": datos.get("comentarios", "")
        }
        print("Cargando venta:", venta)
        agregar_venta_a_sheets(venta)
        if callback:
            callback(success=True)
    except Exception as e:
        print("Error al cargar venta manual:", e)
        if callback:
            callback(success=False, error=str(e))
