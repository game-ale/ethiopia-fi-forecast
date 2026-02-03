import pandas as pd
import matplotlib.pyplot as plt
import os
import logging

logging.basicConfig(level=logging.INFO)

def generate_forecast_chart():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    forecast_path = os.path.join(project_root, "data", "processed", "forecasts_2025_2027.csv")
    raw_path = os.path.join(project_root, "data", "raw", "ethiopia_fi_unified_data.csv")
    output_dir = os.path.join(project_root, "reports", "figures")
    
    df_forecast = pd.read_csv(forecast_path)
    df_raw = pd.read_csv(raw_path)
    
    # 1. Account Ownership Forecast
    indicator = 'ACC_OWNERSHIP'
    title = 'Ethiopia Account Ownership Forecast (2011-2027)'
    
    history = df_raw[(df_raw['indicator_code'] == indicator) & 
                     (df_raw['record_type'] == 'observation') & 
                     (df_raw['gender'] == 'all')].copy()
    history['year'] = pd.to_datetime(history['observation_date']).dt.year
    
    prediction = df_forecast[df_forecast['indicator_code'] == indicator].copy()
    
    plt.figure(figsize=(12, 7))
    
    # Plot History
    plt.plot(history['year'], history['value_numeric'], marker='o', color='black', linewidth=2.5, label='Historical Data')
    
    # Connect last history point to forecasts
    last_year = history['year'].max()
    last_val = history.loc[history['year'].idxmax(), 'value_numeric']
    
    colors = {'Base': '#1f77b4', 'Optimistic': '#2ca02c', 'Pessimistic': '#d62728'}
    styles = {'Base': '-', 'Optimistic': '--', 'Pessimistic': ':'}
    
    for scen in ['Optimistic', 'Base', 'Pessimistic']:
        subset = prediction[prediction['scenario'] == scen]
        years = [last_year] + subset['year'].tolist()
        values = [last_val] + subset['value'].tolist()
        
        plt.plot(years, values, linestyle=styles[scen], color=colors[scen], linewidth=2, label=f'{scen} Scenario')
        
        # Annotate 2027 value
        final_val = values[-1]
        plt.text(2027.1, final_val, f"{final_val:.1f}%", verticalalignment='center', color=colors[scen], fontweight='bold')

    plt.title(title, fontsize=16)
    plt.ylabel("Account Ownership (%)", fontsize=12)
    plt.xlabel("Year", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    
    out_path = os.path.join(output_dir, "forecast_fan_chart.png")
    plt.savefig(out_path)
    logging.info(f"Saved chart to {out_path}")

if __name__ == "__main__":
    generate_forecast_chart()
