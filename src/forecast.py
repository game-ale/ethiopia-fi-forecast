import pandas as pd
import numpy as np
import os
import logging
from sklearn.linear_model import LinearRegression

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_forecasting():
    try:
        # Define paths
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(project_root, "data", "raw", "ethiopia_fi_unified_data.csv")
        impact_path = os.path.join(project_root, "data", "processed", "impact_model_detailed.csv")
        output_dir = os.path.join(project_root, "data", "processed")
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Load data
        if not os.path.exists(data_path) or not os.path.exists(impact_path):
            raise FileNotFoundError("Required data files not found.")
            
        df = pd.read_csv(data_path)
        impacts = pd.read_csv(impact_path)
        
        logging.info("Data loaded for forecasting.")

        # Define targets to forecast
        targets = {
            'ACC_OWNERSHIP': 'Account Ownership Rate',
            'USG_DIGITAL_PAYMENT': 'Digital Payment Usage'
        }

        forecast_results = []

        for code, name in targets.items():
            logging.info(f"Forecasting {name} ({code})...")
            
            # 1. Get Historical Data
            history = df[(df['indicator_code'] == code) & 
                         (df['record_type'] == 'observation') & 
                         (df['gender'] == 'all')].copy()
            
            if history.empty:
                logging.warning(f"No historical data for {code}. Skipping.")
                continue

            history['year'] = pd.to_datetime(history['observation_date']).dt.year
            history = history.sort_values('year')
            
            # 2. Fit Baseline Trend (Linear)
            X = history[['year']].values
            y = history['value_numeric'].values
            
            model = LinearRegression()
            model.fit(X, y)
            
            future_years = np.array([[2025], [2026], [2027]])
            baseline_pred = model.predict(future_years)
            
            # 3. Apply Event Impacts
            # Filter impacts for this indicator
            # We look for impacts that active in the forecast period
            relevant_impacts = impacts[impacts['related_indicator'] == code]
            
            # Simple simulation: 
            # - Base: Trend
            # - Optimistic: Trend + High Impacts
            # - Pessimistic: Trend - Risk Impacts
            
            # Sum of 'magnitude_score' where direction is increase
            # This is a simplification. Ideally we'd distribute this over the lag period.
            # For this 'interim' model, we will add a fixed step-up for events occurring 2024-2026.
            
            future_impact_score = 0
            risk_score = 0
            
            # Get events that happened recently or will happen
            # We assume impacts build up.
            
            for _, row in relevant_impacts.iterrows():
                # If event date is approx near forecast window
                evt_year = int(str(row['observation_date'])[:4])
                
                if 2023 <= evt_year <= 2027:
                    # Calculate net effect
                    # Magnitude: High=3, Medium=2, Low=1
                    # We treat specific magnitude points if available, else use score proxy
                    
                    mag = row['impact_magnitude']
                    score = 0
                    if mag == 'high': score = 3.0
                    elif mag == 'medium': score = 1.5
                    elif mag == 'low': score = 0.5
                    
                    if row['impact_direction'] == 'increase':
                        future_impact_score += score
                    elif row['impact_direction'] == 'decrease':
                        risk_score += score

            # Construct Forecasts
            for i, year in enumerate([2025, 2026, 2027]):
                base_val = baseline_pred[i]
                
                # Apply gradual impact (33% per year of the total expected impact block)
                # This simulates the "S-curve" adoption slightly
                ramp_up = (i + 1) / 3.0 
                
                # Scenarios
                # Base: Pure Trend + 50% of event promise (conservative delivery)
                val_base = base_val + (future_impact_score * 0.5 * ramp_up) - (risk_score * 0.5 * ramp_up)
                
                # Optimistic: Trend + 100% of event promise
                val_opt = base_val + (future_impact_score * 1.0 * ramp_up)
                
                # Pessimistic: Trend + 0% event promise (delays) - 100% risks
                val_pess = base_val - (risk_score * 1.0 * ramp_up)
                
                # Cap at 100%
                val_base = min(100, val_base)
                val_opt = min(100, val_opt)
                val_pess = min(100, val_pess)

                forecast_results.append({
                    'indicator': name,
                    'indicator_code': code,
                    'year': year,
                    'scenario': 'Base',
                    'value': round(val_base, 2)
                })
                forecast_results.append({
                    'indicator': name,
                    'indicator_code': code,
                    'year': year,
                    'scenario': 'Optimistic',
                    'value': round(val_opt, 2)
                })
                forecast_results.append({
                    'indicator': name,
                    'indicator_code': code,
                    'year': year,
                    'scenario': 'Pessimistic',
                    'value': round(val_pess, 2)
                })

        # Save Forecasts
        forecast_df = pd.DataFrame(forecast_results)
        out_path = os.path.join(output_dir, "forecasts_2025_2027.csv")
        forecast_df.to_csv(out_path, index=False)
        logging.info(f"Forecasts saved to {out_path}")
        print(forecast_df)

    except Exception as e:
        logging.error(f"Forecasting failed: {e}")
        exit(1)

if __name__ == "__main__":
    run_forecasting()
