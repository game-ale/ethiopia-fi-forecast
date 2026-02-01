import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_eda():
    try:
        # Define paths
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(project_root, "data", "raw", "ethiopia_fi_unified_data.csv")
        output_dir = os.path.join(project_root, "reports", "figures")
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Check if data file exists
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found at {data_path}. Run enrichment first.")

        # Load data
        df = pd.read_csv(data_path)
        df['observation_date'] = pd.to_datetime(df['observation_date'])
        logging.info("Data loaded successfully for EDA.")

        # Set appearance
        sns.set_theme(style="whitegrid")

        # 1. Access Analysis
        logging.info("Generating Account Ownership trend...")
        acc_own = df[(df['indicator_code'] == 'ACC_OWNERSHIP') & 
                     (df['record_type'] == 'observation') & 
                     (df['gender'] == 'all')]
        
        if not acc_own.empty:
            acc_own = acc_own.sort_values('observation_date')
            plt.figure(figsize=(10, 6))
            plt.plot(acc_own['observation_date'], acc_own['value_numeric'], marker='o', linewidth=2, color='#1f77b4')
            plt.title("Ethiopia: Account Ownership Rate (2014-2024)", fontsize=14)
            plt.ylabel("Ownership Rate (%)")
            plt.ylim(0, 70)
            for x, y in zip(acc_own['observation_date'], acc_own['value_numeric']):
                plt.text(x, y + 2, f"{y}%", ha='center')
            plt.savefig(os.path.join(output_dir, "account_ownership_trend.png"))
            plt.close()
        else:
            logging.warning("No data found for Account Ownership trend.")

        # 2. P2P vs ATM
        logging.info("Generating P2P vs ATM comparison...")
        p2p_atm = df[df['indicator_code'].isin(['USG_P2P_COUNT', 'USG_ATM_COUNT'])]
        recent_fy = p2p_atm['fiscal_year'].max() if not p2p_atm.empty else None
        p2p_atm_recent = p2p_atm[p2p_atm['fiscal_year'] == recent_fy] if recent_fy else pd.DataFrame()

        if not p2p_atm_recent.empty:
            plt.figure(figsize=(8, 6))
            sns.barplot(data=p2p_atm_recent, x='indicator', y='value_numeric', palette='viridis', hue='indicator', legend=False)
            plt.title(f"Transaction Volume: P2P vs ATM ({recent_fy})")
            plt.ylabel("Number of Transactions")
            plt.savefig(os.path.join(output_dir, "p2p_vs_atm.png"))
            plt.close()
        else:
            logging.warning("No data found for P2P vs ATM comparison.")

        # 3. Gender Gap
        logging.info("Generating Gender Gap analysis...")
        gender_data = df[(df['indicator_code'] == 'ACC_OWNERSHIP') & (df['gender'].isin(['male', 'female']))]
        if not gender_data.empty:
            gender_pivot = gender_data.pivot(index='observation_date', columns='gender', values='value_numeric')
            plt.figure(figsize=(10, 6))
            gender_pivot.plot(kind='bar', ax=plt.gca(), color=['#ff7f0e', '#1f77b4'])
            plt.title("Account Ownership by Gender")
            plt.ylabel("Ownership Rate (%)")
            plt.legend(title="Gender")
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, "gender_gap.png"))
            plt.close()
        else:
            logging.warning("No data found for Gender Gap analysis.")

        # 4. Event Timeline
        logging.info("Generating Event Timeline...")
        events = df[df['record_type'] == 'event'].sort_values('observation_date')
        if not events.empty:
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
        else:
            logging.warning("No data found for Event Timeline.")

        logging.info(f"EDA visualizations saved to {output_dir}")

    except Exception as e:
        logging.error(f"EDA execution failed: {e}")
        exit(1)

if __name__ == "__main__":
    run_eda()
