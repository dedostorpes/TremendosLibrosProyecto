import os
import pandas as pd
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
client = gspread.authorize(credentials)

sheet = client.open(SHEET_NAME)
worksheet = sheet.worksheet("Stock")  # Cambia el nombre si es diferente

def cargar_inventario():
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

def registrar_venta(titulo):
    df = cargar_inventario()

    for i, row in df.iterrows():
        if row["Título"] == titulo and not row["Vendido"]:
            # Marcar como vendido
            worksheet.update_cell(i + 2, df.columns.get_loc("Vendido") + 1, "VENDIDO")
            print(f"Libro '{titulo}' marcado como vendido.")
            return
    print(f"No se encontró ejemplar disponible para: {titulo}")