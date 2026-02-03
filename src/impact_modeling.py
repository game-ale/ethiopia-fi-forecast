import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_impact_modeling():
    try:
        # Define paths
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(project_root, "data", "raw", "ethiopia_fi_unified_data.csv")
        processed_dir = os.path.join(project_root, "data", "processed")
        figures_dir = os.path.join(project_root, "reports", "figures")
        
        # Ensure directories exist
        os.makedirs(processed_dir, exist_ok=True)
        os.makedirs(figures_dir, exist_ok=True)

        # check data file
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found at {data_path}")

        # Load data
        df = pd.read_csv(data_path)
        logging.info("Data loaded for impact modeling.")

        # Filter records
        impacts = df[df['record_type'] == 'impact_link'].copy()
        events = df[df['record_type'] == 'event'].copy()
        
        if impacts.empty or events.empty:
            logging.warning("No impact links or events found. Cannot build model.")
            return

        # Join impacts with events
        # impact_link has 'parent_id' which matches event 'record_id'
        impact_model = impacts.merge(
            events[['record_id', 'indicator', 'observation_date']], 
            left_on='parent_id', 
            right_on='record_id', 
            suffixes=('', '_event')
        )

        # Map magnitudes to numeric scores for the matrix
        mag_map = {'high': 3, 'medium': 2, 'low': 1}
        dir_map = {'increase': 1, 'decrease': -1}

        impact_model['magnitude_score'] = impact_model['impact_magnitude'].map(mag_map).fillna(1)
        impact_model['direction_score'] = impact_model['impact_direction'].map(dir_map).fillna(1)
        impact_model['total_impact_score'] = impact_model['magnitude_score'] * impact_model['direction_score']

        logging.info(f" modeled {len(impact_model)} impact relationships.")

        # Create Association Matrix (Event vs Indicator)
        # We use 'indicator_event' (the name of the event) as index
        pivot_df = impact_model.pivot_table(
            index='indicator_event', 
            columns='related_indicator', 
            values='total_impact_score',
            aggfunc='sum' # In case an event has multiple links to same indicator? Unlikely but safe.
        ).fillna(0)

        # Save Matrix
        matrix_path = os.path.join(processed_dir, "event_indicator_matrix.csv")
        pivot_df.to_csv(matrix_path)
        logging.info(f"Association Matrix saved to {matrix_path}")

        # Visualize Heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot_df, annot=True, cmap='RdYlGn', center=0, linewidths=.5)
        plt.title("Event-Indicator Impact Association Matrix (Score: -3 to +3)", fontsize=14)
        plt.xlabel("Indicator Affected")
        plt.ylabel("Event")
        plt.tight_layout()
        pivot_img_path = os.path.join(figures_dir, "impact_matrix.png")
        plt.savefig(pivot_img_path)
        plt.close()
        logging.info(f"Impact heatmap saved to {pivot_img_path}")
        
        # Save the detailed joined model for forecasting script
        model_path = os.path.join(processed_dir, "impact_model_detailed.csv")
        impact_model.to_csv(model_path, index=False)
        logging.info(f"Detailed impact model saved to {model_path}")

    except Exception as e:
        logging.error(f"Impact modeling failed: {e}")
        exit(1)

if __name__ == "__main__":
    run_impact_modeling()
