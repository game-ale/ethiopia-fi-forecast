import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"C:\weak10\ethiopia-fi-forecast\data\raw\ethiopia_fi_unified_data.csv")
output_dir = r"C:\weak10\ethiopia-fi-forecast\reports\figures"
processed_dir = r"C:\weak10\ethiopia-fi-forecast\data\processed"
os.makedirs(processed_dir, exist_ok=True)

# Filter records
impacts = df[df['record_type'] == 'impact_link']
events = df[df['record_type'] == 'event']

# Join impacts with events
impact_model = impacts.merge(events[['record_id', 'indicator']], left_on='parent_id', right_on='record_id', suffixes=('', '_event'))

# Map magnitudes to scores
mag_map = {'high': 3, 'medium': 2, 'low': 1}
dir_map = {'increase': 1, 'decrease': -1}

impact_model['magnitude_score'] = impact_model['impact_magnitude'].map(mag_map)
impact_model['direction_score'] = impact_model['impact_direction'].map(dir_map)
impact_model['impact_score'] = impact_model['magnitude_score'] * impact_model['direction_score']

# Create Association Matrix
pivot_df = impact_model.pivot_table(
    index='indicator_event', 
    columns='related_indicator', 
    values='impact_score',
    aggfunc='sum'
).fillna(0)

# Visualize Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_df, annot=True, cmap='RdYlGn', center=0)
plt.title("Event-Indicator Impact Association Matrix")
plt.xlabel("Indicator Affected")
plt.ylabel("Event")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "impact_matrix.png"))
plt.close()

# Document Summary
print("Top Events by Impact Count:")
print(impact_model['indicator_event'].value_counts())

impact_model.to_csv(r"C:\weak10\ethiopia-fi-forecast\data\processed\event_impact_model.csv", index=False)
print("Impact modeling results saved to data/processed/")
