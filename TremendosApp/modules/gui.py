import tkinter as tk
from modules.ventas import cargar_venta_manual
from modules.reportes import generar_reporte_pdf
from modules.encargos import registrar_encargo
from modules.sheets import actualizar_google_sheets

def lanzar_gui():
    root = tk.Tk()
    root.title("Tremendos Libros - Gestión de Ventas")
    root.geometry("800x600")

    def on_generar_reporte():
        generar_reporte_pdf()

    def on_cargar_venta():
        cargar_venta_manual()

    def on_registrar_encargo():
        registrar_encargo()

    tk.Button(root, text="Cargar venta", command=on_cargar_venta).pack(pady=10)
    tk.Button(root, text="Generar reporte PDF", command=on_generar_reporte).pack(pady=10)
    tk.Button(root, text="Registrar encargo", command=on_registrar_encargo).pack(pady=10)

    root.mainloop()
