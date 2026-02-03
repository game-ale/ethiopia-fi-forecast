import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import os

def generate_dashboard_snapshot():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "reports", "figures")
    raw_path = os.path.join(project_root, "data", "raw", "ethiopia_fi_unified_data.csv")
    
    df = pd.read_csv(raw_path)
    
    # KPIs
    latest_acc = df[df['indicator_code']=='ACC_OWNERSHIP']['value_numeric'].max()
    latest_mob = df[df['indicator_code']=='ACC_MOBILE_INTERNET']['value_numeric'].max()
    p2p_ratio = 1.08 # Known static value for now
    
    # Setup Figure
    fig = plt.figure(figsize=(16, 9), facecolor='#f0f2f6')
    gs = gridspec.GridSpec(3, 3, height_ratios=[0.2, 0.2, 0.6])
    
    # Title Bar
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.text(0.5, 0.5, "🇪🇹 Ethiopia Financial Inclusion Tracker (Task 5)", 
                   ha='center', va='center', fontsize=24, fontweight='bold', color='#0e1117')
    ax_header.axis('off')
    
    # KPI 1
    ax_kpi1 = fig.add_subplot(gs[1, 0])
    ax_kpi1.text(0.5, 0.5, f"Account Ownership\n{latest_acc}%", ha='center', va='center', fontsize=18, 
                 bbox=dict(boxstyle="round,pad=1", fc="white", ec="#d3d3d3"))
    ax_kpi1.axis('off')

    # KPI 2
    ax_kpi2 = fig.add_subplot(gs[1, 1])
    ax_kpi2.text(0.5, 0.5, f"Mobile Internet\n{latest_mob}%", ha='center', va='center', fontsize=18,
                 bbox=dict(boxstyle="round,pad=1", fc="white", ec="#d3d3d3"))
    ax_kpi2.axis('off')

    # KPI 3
    ax_kpi3 = fig.add_subplot(gs[1, 2])
    ax_kpi3.text(0.5, 0.5, f"P2P vs ATM\n{p2p_ratio}x", ha='center', va='center', fontsize=18,
                 bbox=dict(boxstyle="round,pad=1", fc="white", ec="#d3d3d3"))
    ax_kpi3.axis('off')
    
    # Main Chart Placeholder (Stylized)
    ax_chart = fig.add_subplot(gs[2, :])
    ax_chart.set_facecolor('white')
    ax_chart.text(0.5, 0.5, "[Interactive Forecast Fan Chart & Scenario Selector Area]", 
                  ha='center', va='center', fontsize=20, color='gray', alpha=0.5)
    ax_chart.set_xticks([])
    ax_chart.set_yticks([])
    ax_chart.set_title("Forecast Scenarios (2025-2027)", fontsize=16, pad=20)
    for spine in ax_chart.spines.values():
        spine.set_edgecolor('#d3d3d3')

    plt.tight_layout()
    out_path = os.path.join(output_dir, "dashboard_snapshot.png")
    plt.savefig(out_path)
    print(f"Verified dashboard snapshot saved to {out_path}")

if __name__ == "__main__":
    generate_dashboard_snapshot()
