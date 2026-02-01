import pandas as pd
import os

df = pd.read_csv(r"C:\weak10\ethiopia-fi-forecast\data\raw\ethiopia_fi_unified_data.csv")
refs = pd.read_csv(r"C:\weak10\ethiopia-fi-forecast\data\raw\reference_codes.csv")

print("--- Record Counts by Type ---")
print(df['record_type'].value_counts())

print("\n--- Counts by Pillar (Observations only) ---")
print(df[df['record_type'] == 'observation']['pillar'].value_counts())

print("\n--- Unique Indicators ---")
print(df[df['record_type'] == 'observation']['indicator'].unique())

print("\n--- Temporal Range (Observations) ---")
print(f"Start: {df['observation_date'].min()}")
print(f"End: {df['observation_date'].max()}")

print("\n--- Event Categories ---")
print(df[df['record_type'] == 'event']['category'].value_counts())

print("\n--- Confidence Levels ---")
print(df['confidence'].value_counts())

print("\n--- Sample Impact Links ---")
print(df[df['record_type'] == 'impact_link'][['parent_id', 'pillar', 'related_indicator', 'impact_magnitude']].head())

# Identify gaps
print("\n--- Missing Indicators/Pillars ---")
# Check if all pillars in reference codes are present in observations
expected_pillars = refs[refs['field'] == 'pillar']['code'].unique()
actual_pillars = df[df['record_type'] == 'observation']['pillar'].unique()
missing_pillars = set(expected_pillars) - set(actual_pillars)
print(f"Missing pillars: {missing_pillars}")
