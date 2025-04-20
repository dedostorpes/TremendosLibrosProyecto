
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def cargar_stock_desde_sheets(sheet_name="Inventario de compras"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)
