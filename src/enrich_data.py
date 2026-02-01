import pandas as pd
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def enrich_data():
    try:
        # Define paths
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(project_root, "data", "raw", "ethiopia_fi_unified_data.csv")

        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Unified data file not found at {file_path}. Run init_data.py first.")

        # Load existing data
        df = pd.read_csv(file_path)
        logging.info(f"Loaded existing data with {len(df)} records.")

        # New Records definition
        new_records = [
            {
                "record_id": "REC_0034",
                "record_type": "observation",
                "pillar": "ACCESS",
                "indicator": "Mobile Internet Usage Rate",
                "indicator_code": "ACC_MOBILE_INTERNET",
                "indicator_direction": "higher_better",
                "value_numeric": 21.4,
                "unit": "%",
                "observation_date": "2024-12-31",
                "source_name": "DataReportal Digital 2025",
                "source_type": "research",
                "source_url": "https://datareportal.com/",
                "confidence": "high",
                "collected_by": "Antigravity",
                "collection_date": datetime.now().strftime("%Y-%m-%d"),
                "notes": "Enabler for mobile money usage"
            },
            {
                "record_id": "REC_0035",
                "record_type": "observation",
                "pillar": "ACCESS",
                "indicator": "Smartphone Penetration",
                "indicator_code": "ACC_SMARTPHONE",
                "indicator_direction": "higher_better",
                "value_numeric": 29.5,
                "unit": "%",
                "observation_date": "2024-12-31",
                "source_name": "GSMA Intelligence",
                "source_type": "research",
                "source_url": "https://www.gsma.com/intelligence/",
                "confidence": "medium",
                "collected_by": "Antigravity",
                "collection_date": datetime.now().strftime("%Y-%m-%d"),
                "notes": "Key driver for app-based financial services"
            },
            {
                "record_id": "EVT_0011",
                "record_type": "event",
                "category": "policy",
                "indicator": "NBE Open Banking Framework",
                "indicator_code": "EVT_OPEN_BANKING",
                "value_text": "Implemented",
                "value_type": "categorical",
                "observation_date": "2025-01-15",
                "source_name": "National Bank of Ethiopia",
                "source_type": "regulator",
                "confidence": "high",
                "collected_by": "Antigravity",
                "collection_date": datetime.now().strftime("%Y-%m-%d"),
                "notes": "Allows third-party API access to bank data"
            },
            {
                "record_id": "IMP_0015",
                "record_type": "impact_link",
                "pillar": "USAGE",
                "indicator": "Open Banking Effect on Digital Payments",
                "related_indicator": "USG_DIGITAL_PAYMENT",
                "observation_date": "2025-01-15",
                "confidence": "medium",
                "impact_direction": "increase",
                "impact_magnitude": "medium",
                "lag_months": 12.0,
                "evidence_basis": "literature",
                "comparable_country": "Nigeria",
                "parent_id": "EVT_0011",
                "collected_by": "Antigravity",
                "collection_date": datetime.now().strftime("%Y-%m-%d"),
                "notes": "Expected to boost fintech innovation and transaction volumes"
            }
        ]

        # Avoid double enrichment by checking record IDs
        existing_ids = df['record_id'].tolist()
        records_to_add = [r for r in new_records if r['record_id'] not in existing_ids]

        if not records_to_add:
            logging.info("No new records to add. Dataset is already enriched.")
            return

        # Concatenate and save
        new_df = pd.DataFrame(records_to_add)
        df_enriched = pd.concat([df, new_df], ignore_index=True)
        
        df_enriched.to_csv(file_path, index=False)
        logging.info(f"Enriched dataset with {len(records_to_add)} new records. Saved to {file_path}")

    except Exception as e:
        logging.error(f"Data enrichment failed: {e}")
        exit(1)

if __name__ == "__main__":
    enrich_data()
