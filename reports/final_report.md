# Final Report: Ethiopia Financial Inclusion Forecasting (2025-2027)

**Date:** February 3, 2026  
**Analyst:** Gemechu Alemu (Selam Analytics)  
**Status:** **Final Submission**  
**Project Link:** [GitHub Repository](https://github.com/game-ale/ethiopia-fi-forecast)

---

## 1. Executive Summary

This report presents the final outputs of the **Ethiopia Financial Inclusion Forecasting System**. By integrating supply-side infrastructure data with demand-side Findex surveys, we have modeled the trajectory of financial inclusion through 2027.

**Key Conclusion**: Ethiopia is on track to break the **60% Account Ownership** threshold by late 2026. Our modeling identifies that whilst infrastructure (4G/Agents) set the stage, it is specific *Usage Events*—like the interoperability of P2P transfers—that are now the primary drivers of growth.

### 1.1 Consortium Objectives
To ensure actionable insights, we tailored this analysis for:
*   **National Bank of Ethiopia (NBE)**: Validating if the "Open Banking Framework" (2025) will bridge the gap to the NFIS-II 70% target.
*   **Mobile Network Operators (MNOs)**: Understanding if market saturation is near for basic wallets vs. advanced credit products.
*   **DFIs**: Identifying the "Usage-Coverage Gap" to target funding towards device financing and digital literacy.

---

## 2. Methodology

### 2.1 Data Enrichment Strategy
The core Findex dataset (3 observations) was insufficient for high-fidelity forecasting. We enriched this with a **Unified Schema** approach:
*   **Proxy Integration**: We ingested GSMA intelligence data (`ACC_SMARTPHONE`, `ACC_MOBILE_INTERNET`) to serve as leading indicators for demand-side adoption.
*   **Event Cataloging**: We structured qualitative milestones (e.g., "Telebirr Launch") into quantitative event records (`EVT_00XX`), allowing us to measure "Shock" vs. "Trend" dynamics.

### 2.2 Event Impact Modeling Framework
We developed a semi-structural forecasting model (`Value_t = Trend_t + Σ Impact_i`) rather than a pure black-box regression.
1.  **Scoring**: Qualitative events were assigned magnitude scores (High=3, Medium=2, Low=1) and directions based on expert consensus and comparable market analysis (e.g., Kenya's M-Pesa trajectory).
2.  **Lag & Persistence**: Improvements were modeled with a 12-month "ramp-up" period, reflecting the time lag between policy announcement and consumer adoption.
3.  **Association Matrix**: We visualized these derived scores (Figure 3) to validate that our model weights aligned with historical reality (e.g., the massive inclusion spike post-2021).

---

## 3. Retrospective: Key Insights (2014-2024)

### A. The "Digital Dominance" Milestone
In a historic shift, the volume of digital P2P transfers has surpassed ATM cash withdrawals (Ratio: **1.08**). Ethiopia has effectively leapfrogged the "card era" directly to mobile-based payments.
![P2P vs ATM](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/p2p_vs_atm.png)

### B. The Ownership Paradox
Despite 54M+ registered mobile money accounts, unique account ownership grew slowly (46% → 49%) between 2021-2024.
*   **Root Cause**: High rate of "multi-homing" (banked users opening wallets).
*   **Implication**: Future growth relies on the "Usage-Coverage Gap"—converting the 21% of mobile internet users who are not yet financially active.

**Visual Evidence**:
![Account Ownership Trend](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/account_ownership_trend.png)
![Usage Coverage Gap](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/usage_coverage_gap.png)

---

### 3.1 Interactive Dashboard
We delivered a **Streamlit Dashboard** (`dashboard/app.py`) to allow stakeholders to explore these insights dynamically.
*   **Overview Tab**: Real-time tracking of the P2P/ATM crossover and account ownership.
*   **Forecast Tab**: Interactive scenario selector (Base/Optimistic/Pessimistic).
*   **Impact Tab**: Visualizes the underlying event weights.

![Dashboard Snapshot](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/dashboard_snapshot.png)

---

## 4. Answering the Consortium's Core Questions

### Q1: What drives financial inclusion in Ethiopia?
**Answer**: It is currently **Supply-Push** driven. Our EDA shows that account growth correlates most strongly with "Product Launches" (Telebirr) rather than organic demand factors like GDP. The *Ownership Paradox* (Insight B) confirms that infrastructure is ahead of actual usage.

### Q2: How do events affect outcomes?
**Answer**: Events act as "Step Functions". Historical analysis reveals that inclusion affects don't grow linearly but spike following platform launches. Our model assigns the highest weights to **Interoperability Events** (EthSwitch P2P) over physical infrastructure events (ATM deployment).

### Q3: What is the 2025-2027 Outlook?
**Answer**: We forecast a transition from "Acquisition" to "Deepening".
*   **2025**: Re-acceleration to **54.5%** driven by M-Pesa scaling.
*   **2027**: Reaching **60.4%** as Open Banking allows third-party fintechs to build on top of MNO rails.

---

## 5. Forecast Results (2025-2027)

### Target: Account Ownership Rate
Our model predicts a steady climb.
*   **Uncertainty Quantification**: The 1.5pp spread between Optimistic and Pessimistic scenarios reflects the execution risk of the NBE's upcoming reforms. A failure to launch Open Banking would pin results to the Pessimistic (59.6%) trajectory.

| Year | Pessimistic | **Base Case** | Optimistic |
| :--- | :--- | :--- | :--- |
| **2025** | 54.24% | **54.49%** | 54.74% |
| **2026** | 56.95% | **57.45%** | 57.95% |
| **2027** | 59.66% | **60.41%** | 61.16% |

> **Analyst Note**: Crossing the 60% mark in 2027 aligns with the revised NFIS-II mid-term targets, suggesting that current policy levers are effective but require sustained execution.

![Forecast Fan Chart](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/forecast_fan_chart.png)

---

## 6. Event Impact Analysis

**Figure 3: Event-Indicator Association Matrix**
*This heatmap visualizes the model's assigned impact scores (Red to Green), identifying which events are the strongest predictors of future growth.*

1.  **High Impact (Driver)**: *Telebirr Launch (2021)* - Validated as the primary driver of recent growth.
2.  **Medium Impact (Enabler)**: *NBE Open Banking (2025)* - Critical for the 2026-2027 "Optimistic" scenario.
3.  **Low Impact (Saturated)**: *ATMs* - Infrastructure saturation suggests marginal returns.

![Impact Matrix](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/impact_matrix.png)

---

## 7. Strategic Recommendations

To ensure the **Optimistic Scenario (61.16%)** is realized, we propose:

1.  **Bridge the Device Gap** (*Evidence: Usage-Coverage Gap*)
    *   **Strategy**: MNOs should shift subsidies from airtime to **4G Handset Financing**. The 29.5% smartphone penetration is the hard ceiling for advanced app-based inclusion.
2.  **Leverage Digital ID** (*Evidence: Gender Gap trend*)
    *   **Strategy**: Use Fayda eKYC to lower the cost-to-serve for rural women, directly addressing the 18pp gender gap which has remained stubborn despite general growth.
3.  **Merchant Interoperability** (*Evidence: P2P vs ATM Ratio*)
    *   **Strategy**: Capitalize on the "Digital Dominance" behavior. The public is ready for digital P2P; a unified QR standard will convert this P2P habit into P2B (Merchant) commerce.

---

## 7. Limitations and Future Work

### Limitations
1.  **Data Frequency**: The core Findex survey occurs only every 3 years, necessitating the use of proxy supply-side data (NBE reports) which may overstate "active" users due to multi-homing.
2.  **Linear Assumptions**: The Event Impact Model assumes additive shocks; real-world adoption often follows non-linear S-curves which were only partially simulated via ramp-up factors.
3.  **Excluded Variables**: Informal financial sector activity (Equb/Iddir) is not captured, potentially underestimating true liquidity.

### Future Work
1.  **Regional Granularity**: Extend the model to forecast inclusion at the *Woreda* level to identify specific "dark spots."
2.  **Real-Time NBE Link**: Automate the data pipeline to ingest NBE quarterly reports directly, removing manual CSV entry.
3.  **Agent Network Modeling**: Include "Agent Density" as an explicit predictor variable in the next iteration of the forecasting engine.

---

*Verified by Antigravity Forecast Engine v1.1*
