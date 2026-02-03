import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set page config
st.set_page_config(
    page_title="Ethiopia FI Forecast System",
    page_icon="🇪🇹",
    layout="wide"
)

# Load Data
@st.cache_data
def load_data():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    forecast_path = os.path.join(project_root, "data", "processed", "forecasts_2025_2027.csv")
    raw_path = os.path.join(project_root, "data", "raw", "ethiopia_fi_unified_data.csv")
    matrix_path = os.path.join(project_root, "data", "processed", "event_indicator_matrix.csv")
    
    df_forecast = pd.read_csv(forecast_path)
    df_raw = pd.read_csv(raw_path)
    df_matrix = pd.read_csv(matrix_path, index_col=0)
    
    return df_forecast, df_raw, df_matrix

try:
    df_forecast, df_raw, df_matrix = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}. Please ensure Tasks 1-4 are complete.")
    st.stop()

# Information Sidebar
st.sidebar.title("🇪🇹 Ethiopia FI Forecast")
st.sidebar.info(
    """
    **Project Phase**: Task 5 (Dashboard)
    **Objective**: Visualize 2025-2027 Financial Inclusion Scenarios.
    **Dimensions**: Access & Usage.
    """
)
page = st.sidebar.radio("Navigate", ["Overview", "Forecasts", "Impact Analysis"])

def plot_fan_chart(indicator_code, title):
    history = df_raw[(df_raw['indicator_code'] == indicator_code) & 
                     (df_raw['record_type'] == 'observation') & 
                     (df_raw['gender'] == 'all')].copy()
    history['year'] = pd.to_datetime(history['observation_date']).dt.year
    history['scenario'] = 'Historical'
    
    prediction = df_forecast[df_forecast['indicator_code'] == indicator_code].copy()
    
    fig = go.Figure()
    
    # Historical Line
    fig.add_trace(go.Scatter(
        x=history['year'], y=history['value_numeric'],
        mode='lines+markers', name='Historical',
        line=dict(color='black', width=3)
    ))
    
    # Scenarios
    colors = {'Base': 'blue', 'Optimistic': 'green', 'Pessimistic': 'red'}
    for scen, color in colors.items():
        subset = prediction[prediction['scenario'] == scen]
        
        # Connect to last history point
        last_yr = history['year'].max()
        last_val = history.loc[history['year'].idxmax(), 'value_numeric']
        
        x_vals = [last_yr] + subset['year'].tolist()
        y_vals = [last_val] + subset['value'].tolist()
        
        fig.add_trace(go.Scatter(
            x=x_vals, y=y_vals,
            mode='lines', name=scen,
            line=dict(color=color, dash='dash' if scen=='Base' else 'dot')
        ))
        
    fig.update_layout(title=title, yaxis_title="Percentage (%)", xaxis_title="Year")
    return fig

if page == "Overview":
    st.title("Executive Summary: Financial Inclusion Tracker")
    
    col1, col2, col3 = st.columns(3)
    
    # KPIs (Latest Historical)
    latest_acc = df_raw[df_raw['indicator_code']=='ACC_OWNERSHIP']['value_numeric'].max()
    latest_mob = df_raw[df_raw['indicator_code']=='ACC_MOBILE_INTERNET']['value_numeric'].max()
    
    col1.metric("Account Ownership (2024)", f"{latest_acc}%", "3% since 2021")
    col2.metric("Mobile Internet Usage", f"{latest_mob}%")
    col3.metric("P2P vs ATM Ratio", "1.08", "Digital Dominance")
    
    st.divider()
    
    st.subheader("Key Insight: The Ownership Paradox")
    st.markdown("Despite high registration numbers (Telebirr > 54M), actual account ownership growth has decelerated.")
    
    # Simple Bar Chart for Gender Gap
    gender_gap = df_raw[(df_raw['indicator_code']=='ACC_OWNERSHIP') & (df_raw['gender'].isin(['male','female']))]
    if not gender_gap.empty:
        fig_gender = px.bar(gender_gap, x='observation_date', y='value_numeric', color='gender', barmode='group', title="Gender Gap Trend")
        st.plotly_chart(fig_gender, use_container_width=True)

elif page == "Forecasts":
    st.title("Projections 2025-2027")
    
    st.markdown("### Scenario Planning")
    st.markdown("""
    *   **Base Case**: Current trend + partial realization of pending policy impacts.
    *   **Optimistic**: Full implementation of Open Banking & FX liberalization.
    *   **Pessimistic**: Macroeconomic headwinds and delayed infrastructure rollout.
    """)
    
    tab1, tab2 = st.tabs(["Access (Ownership)", "Usage (Digital Payments)"])
    
    with tab1:
        st.plotly_chart(plot_fan_chart('ACC_OWNERSHIP', "Account Ownership Forecast"), use_container_width=True)
        
    with tab2:
        st.plotly_chart(plot_fan_chart('USG_DIGITAL_PAYMENT', "Digital Payment Usage Forecast"), use_container_width=True)

elif page == "Impact Analysis":
    st.title("Event Impact Modeling")
    
    st.info("The forecasting engine 'augments' the baseline trend with these event scores.")
    
    # Heatmap
    fig_heat = px.imshow(df_matrix, text_auto=True, aspect="auto", color_continuous_scale='RdYlGn', title="Event-Indicator Association Matrix")
    st.plotly_chart(fig_heat, use_container_width=True)
    
    st.subheader("Modeled Events")
    events = df_raw[df_raw['record_type']=='event'][['observation_date', 'indicator', 'category']].sort_values('observation_date', ascending=False)
    st.dataframe(events, use_container_width=True)
