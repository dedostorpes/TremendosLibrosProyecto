
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import sys

def run_app():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Tremendos Libros")
    layout = QVBoxLayout()
    layout.addWidget(QLabel("Sistema de Gestión de Ventas"))
    layout.addWidget(QPushButton("Generar Reporte"))
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
