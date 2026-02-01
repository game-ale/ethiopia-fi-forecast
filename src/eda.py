import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")
output_dir = r"C:\weak10\ethiopia-fi-forecast\reports\figures"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(r"C:\weak10\ethiopia-fi-forecast\data\raw\ethiopia_fi_unified_data.csv")
df['observation_date'] = pd.to_datetime(df['observation_date'])

# 1. Dataset Overview
print("Summary by Record Type:")
print(df['record_type'].value_counts())

# 2. Access Analysis: Account Ownership Trajectory
acc_own = df[(df['indicator_code'] == 'ACC_OWNERSHIP') & (df['record_type'] == 'observation') & (df['gender'] == 'all')]
acc_own = acc_own.sort_values('observation_date')

plt.figure(figsize=(10, 6))
plt.plot(acc_own['observation_date'], acc_own['value_numeric'], marker='o', linewidth=2, color='#1f77b4')
plt.title("Ethiopia: Account Ownership Rate (2014-2024)", fontsize=14)
plt.ylabel("Ownership Rate (%)")
plt.xlabel("Year")
plt.ylim(0, 70)
for x, y in zip(acc_own['observation_date'], acc_own['value_numeric']):
    plt.text(x, y + 2, f"{y}%", ha='center')
plt.savefig(os.path.join(output_dir, "account_ownership_trend.png"))
plt.close()

# 3. Usage Analysis: P2P vs ATM
p2p_atm = df[df['indicator_code'].isin(['USG_P2P_COUNT', 'USG_ATM_COUNT'])]
# Filter for FY2024/25
p2p_atm_recent = p2p_atm[p2p_atm['fiscal_year'] == 'FY2024/25']

plt.figure(figsize=(8, 6))
sns.barplot(data=p2p_atm_recent, x='indicator', y='value_numeric', palette='viridis')
plt.title("Transaction Volume: P2P vs ATM (FY2024/25)")
plt.ylabel("Number of Transactions")
plt.savefig(os.path.join(output_dir, "p2p_vs_atm.png"))
plt.close()

# 4. Gender Gap Analysis
gender_data = df[(df['indicator_code'] == 'ACC_OWNERSHIP') & (df['gender'].isin(['male', 'female']))]
gender_pivot = gender_data.pivot(index='observation_date', columns='gender', values='value_numeric')

plt.figure(figsize=(10, 6))
gender_pivot.plot(kind='bar', ax=plt.gca())
plt.title("Account Ownership by Gender")
plt.ylabel("Ownership Rate (%)")
plt.savefig(os.path.join(output_dir, "gender_gap.png"))
plt.close()

# 5. Event Timeline
events = df[df['record_type'] == 'event'].sort_values('observation_date')
plt.figure(figsize=(12, 4))
plt.scatter(events['observation_date'], [1]*len(events), color='red', marker='|', s=500)
for i, row in events.iterrows():
    plt.text(row['observation_date'], 1.05, row['indicator'], rotation=45, ha='right', fontsize=8)
plt.title("Major Financial Inclusion Events Timeline")
plt.yticks([])
plt.ylim(0.9, 1.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "event_timeline.png"))
plt.close()

print("EDA visualizations saved to reports/figures/")
