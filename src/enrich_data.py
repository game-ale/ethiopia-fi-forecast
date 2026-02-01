import pandas as pd
import os
from datetime import datetime

file_path = r"C:\weak10\ethiopia-fi-forecast\data\raw\ethiopia_fi_unified_data.csv"
df = pd.read_csv(file_path)

# New Records
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

new_df = pd.DataFrame(new_records)
df_enriched = pd.concat([df, new_df], ignore_index=True)

df_enriched.to_csv(file_path, index=False)
print(f"Enriched dataset with {len(new_records)} new records.")
