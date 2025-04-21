import os
import gspread
import datetime
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

# Carga las variables del .env
load_dotenv()

# Variables de entorno necesarias
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")
WORKSHEET_NAME = os.getenv("GOOGLE_WORKSHEET_NAME")

# Asegurarse de que estén presentes
if not SERVICE_ACCOUNT_FILE or not SHEET_NAME or not WORKSHEET_NAME:
    raise ValueError("Faltan variables de entorno para Google Sheets")

# Define los scopes
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Autenticación y conexión
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
client = gspread.authorize(credentials)

# Abre el archivo y la hoja
try:
    sheet = client.open(SHEET_NAME)
    worksheet = sheet.worksheet(WORKSHEET_NAME)
except gspread.exceptions.SpreadsheetNotFound:
    raise Exception(f"No se encontró el archivo de Sheets: {SHEET_NAME}")
except gspread.exceptions.WorksheetNotFound:
    raise Exception(f"No se encontró la hoja: {WORKSHEET_NAME} en el archivo {SHEET_NAME}")

# Función de prueba: puedes ampliarla luego
def actualizar_google_sheets():
    print("Función de actualización de Google Sheets ejecutada.")
    # Por ejemplo, leer todo el contenido
    rows = worksheet.get_all_values()
    print(f"Se cargaron {len(rows)} filas de la hoja.")
    
def agregar_venta_a_sheets(venta: dict):
    """
    Agrega una venta al Google Sheet.
    Se espera un diccionario con claves como 'Fecha', 'Título', 'Precio venta', etc.
    """
    import datetime
    
    global worksheet  # Usa el worksheet ya cargado al inicio del módulo
    
    # Armar fila en el orden esperado
    fila = [
        venta.get("Fecha", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        venta.get("Proveedor", ""),
        venta.get("Precio del lote", ""),
        venta.get("Precio unitario", ""),
        venta.get("Precio de venta", ""),
        venta.get("%", ""),
        venta.get("Título", ""),
        venta.get("Autor", ""),
        venta.get("Editorial", ""),
        venta.get("Colección", ""),
        venta.get("Comentarios", ""),
        "NO"  # Vendido: por defecto NO; si ya está vendido, puede marcarse como 'SI'
    ]
    
    worksheet.append_row(fila, value_input_option="USER_ENTERED")
    print("✅ Venta agregada a Google Sheets.")
    
    def registrar_encargo_en_sheets(nombre_cliente, pedido):
    nueva_fila = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nombre_cliente, pedido]
    try:
        hoja_encargos = sheet.worksheet("Encargos")  # Asegúrate que exista esta hoja
    except WorksheetNotFound:
        hoja_encargos = sheet.add_worksheet(title="Encargos", rows="100", cols="3")
        hoja_encargos.append_row(["Fecha", "Cliente", "Pedido"])
    hoja_encargos.append_row(nueva_fila)