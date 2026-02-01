import pandas as pd
import os

path = r"C:\weak10\ethiopia-fi-forecast\data\Additional Data Points Guide.xlsx"
xls = pd.ExcelFile(path)
print(f"Sheets: {xls.sheet_names}")

for sheet in xls.sheet_names:
    print(f"\n--- {sheet} ---")
    df = pd.read_excel(xls, sheet)
    print(df.head())
    print(df.columns)
