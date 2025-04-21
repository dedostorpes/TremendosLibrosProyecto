import os
import gspread
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