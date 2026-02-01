import pandas as pd
path = r"C:\weak10\ethiopia-fi-forecast\data\Additional Data Points Guide.xlsx"
xls = pd.ExcelFile(path)
sheet_name = [s for s in xls.sheet_names if "Indirect" in s][0]
df = pd.read_excel(xls, sheet_name=sheet_name)
print(f"Reading sheet: {sheet_name}")
print(df.head(20))
