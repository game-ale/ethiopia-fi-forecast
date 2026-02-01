import pandas as pd
path = r"C:\weak10\ethiopia-fi-forecast\data\Additional Data Points Guide.xlsx"
df = pd.read_excel(path, sheet_name="C. Indirect Corelating ")
print(df)
