import pandas as pd
import os

data_dir = r"C:\weak10\ethiopia-fi-forecast\data"
raw_dir = os.path.join(data_dir, "raw")
os.makedirs(raw_dir, exist_ok=True)

# Load Excel files
unified_path = os.path.join(data_dir, "ethiopia_fi_unified_data.xlsx")
refs_path = os.path.join(data_dir, "reference_codes.xlsx")

# Check unified data sheets
with pd.ExcelFile(unified_path) as xls:
    print(f"Sheets in unified data: {xls.sheet_names}")
    df_data = pd.read_excel(xls, "ethiopia_fi_unified_data")
    df_links = pd.read_excel(xls, "Impact_sheet")

# Merge or keep separate? 
# The instructions say "Load ethiopia_fi_unified_data.csv" and 
# "Examine the structure: all records share the same columns"
# This suggests they should be combined into one CSV if they are to be "unified".

# Combine them
df_unified = pd.concat([df_data, df_links], ignore_index=True)

# Save to CSV
df_unified.to_csv(os.path.join(raw_dir, "ethiopia_fi_unified_data.csv"), index=False)

# Reference codes
df_refs = pd.read_excel(refs_path)
df_refs.to_csv(os.path.join(raw_dir, "reference_codes.csv"), index=False)

print("Conversion complete.")
print(f"Unified data rows: {len(df_unified)}")
print(f"Reference codes rows: {len(df_refs)}")
