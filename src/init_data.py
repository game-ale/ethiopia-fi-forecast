import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def init_data():
    try:
        # Define paths relative to the script location or project root
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(project_root, "data")
        raw_dir = os.path.join(data_dir, "raw")
        
        # Ensure raw directory exists
        if not os.path.exists(raw_dir):
            os.makedirs(raw_dir, exist_ok=True)
            logging.info(f"Created directory: {raw_dir}")

        # Input file paths
        unified_path = os.path.join(data_dir, "ethiopia_fi_unified_data.xlsx")
        refs_path = os.path.join(data_dir, "reference_codes.xlsx")

        # Check if input files exist
        if not os.path.exists(unified_path):
            raise FileNotFoundError(f"Input file not found: {unified_path}")
        if not os.path.exists(refs_path):
            raise FileNotFoundError(f"Input file not found: {refs_path}")

        # Load Excel files with error handling
        logging.info("Loading Excel data...")
        try:
            with pd.ExcelFile(unified_path) as xls:
                sheets = xls.sheet_names
                logging.info(f"Sheets in unified data: {sheets}")
                
                # Handling variation in sheet names if possible
                data_sheet = "ethiopia_fi_unified_data" if "ethiopia_fi_unified_data" in sheets else sheets[0]
                impact_sheet = "Impact_sheet" if "Impact_sheet" in sheets else (sheets[1] if len(sheets) > 1 else None)
                
                df_data = pd.read_excel(xls, data_sheet)
                df_links = pd.read_excel(xls, impact_sheet) if impact_sheet else pd.DataFrame()
        except Exception as e:
            raise RuntimeError(f"Error reading Excel file {unified_path}: {e}")

        # Combine them
        df_unified = pd.concat([df_data, df_links], ignore_index=True)

        # Save to CSV
        output_data_path = os.path.join(raw_dir, "ethiopia_fi_unified_data.csv")
        df_unified.to_csv(output_data_path, index=False)
        logging.info(f"Saved unified data to {output_data_path}")

        # Reference codes
        try:
            df_refs = pd.read_excel(refs_path)
            output_refs_path = os.path.join(raw_dir, "reference_codes.csv")
            df_refs.to_csv(output_refs_path, index=False)
            logging.info(f"Saved reference codes to {output_refs_path}")
        except Exception as e:
            raise RuntimeError(f"Error processing reference codes: {e}")

        logging.info("Data initialization complete.")
        logging.info(f"Unified data rows: {len(df_unified)}")
        logging.info(f"Reference codes rows: {len(df_refs)}")

    except Exception as e:
        logging.error(f"Data initialization failed: {e}")
        exit(1)

if __name__ == "__main__":
    init_data()
