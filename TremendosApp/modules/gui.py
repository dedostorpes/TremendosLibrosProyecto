
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from modules.logic import cargar_venta_manual, generar_reporte_pdf, registrar_encargo

def lanzar_gui():
    app = QApplication([])

    ventana = QWidget()
    ventana.setWindowTitle("Sistema de gestión de ventas")

    layout = QVBoxLayout()

    label = QLabel("Tremendos Libros - Gestión")
    layout.addWidget(label)

    boton_cargar = QPushButton("Cargar venta")
    boton_cargar.clicked.connect(cargar_venta_manual)
    layout.addWidget(boton_cargar)

    boton_reporte = QPushButton("Generar reporte PDF")
    boton_reporte.clicked.connect(generar_reporte_pdf)
    layout.addWidget(boton_reporte)

    boton_encargo = QPushButton("Registrar encargo")
    boton_encargo.clicked.connect(registrar_encargo)
    layout.addWidget(boton_encargo)

    ventana.setLayout(layout)
    ventana.show()
    app.exec_()
