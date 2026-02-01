# Interim Report: Forecasting Financial Inclusion in Ethiopia

**Date:** February 1, 2026  
**Analyst:** Antigravity (Data Scientist, Selam Analytics)  
**Status:** Task 1 & Task 2 Complete  

---

## 1. Business Objective & Executive Summary

### Business Objective
Selam Analytics has been engaged by a consortium including the **National Bank of Ethiopia (NBE)**, mobile money operators, and development finance institutions. The primary objective is to develop a data-driven forecasting system that tracks Ethiopia's digital financial transformation. 

Specifically, the system must:
*   **Predict Core Dimensions**: Forecast *Access* (Account Ownership) and *Usage* (Digital Payment Adoption) for the critical 2025–2027 period.
*   **Inform Policy**: Provide stakeholders with evidence-based projections to evaluate the progress toward **NFIS-II (National Financial Inclusion Strategy)** targets.
*   **Quantify Impact**: Understand how specific "interventions"—such as the launch of **Telebirr** and **M-Pesa**, the rollout of **Fayda Digital ID**, and major **FX reforms**—accelerate or hinder inclusion.

### Executive Summary
Initial analysis reveals a "Digital First" transition where P2P transactions have surpassed cash withdrawals (Ratio 1.08). However, a significant "Ownership Paradox" exists: account ownership grew only 3pp (46% to 49%) between 2021 and 2024 despite massive mobile money expansion. Our modeling will focus on bridging this gap by analyzing infrastructure enablers and event-driven adoption curves to provide reliable 2025-2027 forecasts.

---

## 2. Discussion of Completed Work

### Task 1: Data Exploration and Enrichment
The provided dataset was enriched with strategic records to capture leading indicators of inclusion.

| Record ID | Type | Pillar | Indicator / Event | Why it was added |
|-----------|------|--------|--------------------|------------------|
| `REC_0034` | Obs | ACCESS | Mobile Internet Usage (21.4%) | Corrects for the "Coverage vs Usage" gap; is a critical enabler for app-based services. |
| `REC_0035` | Obs | ACCESS | Smartphone Penetration (29.5%) | Differentiates between basic USSD access and advanced digital financial service (DFS) usage. |
| `EVT_0011` | Event | Policy | NBE Open Banking Framework | A strategic shift allowing third-party API access, set to drive 2026-2027 usage growth. |
| `IMP_0015` | Link | USAGE | Open Banking Impact Link | Mathematically connects the regulatory event to `USG_DIGITAL_PAYMENT` models. |

### Task 2: Exploratory Data Analysis (EDA)

#### Insight 1: The "Ownership Paradox" (2021-2024 slowdown)
Account ownership growth slowed (46% to 49%) despite high registration. This suggests that new mobile money entrants may be existing bank customers or that demand-side surveys lag supply-side registration numbers.
![Account Ownership Trend](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/account_ownership_trend.png)

#### Insight 2: Maturity Milestone: P2P > ATM
Interoperable P2P transfers have surpassed ATM withdrawals, signaling a shift away from cash-out dependency.
![P2P vs ATM Transaction Volume](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/p2p_vs_atm.png)

#### Insight 3: The Persistent Gender Gap
A gap of 18pp remains. X-axis shows the core survey years 2021 and 2024 (projected).
![Account Ownership Gender Gap](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/gender_gap.png)

#### Insight 4: The Usage-Coverage Gap (Enabler Status)
Infrastructure (4G) is ready, but usage lags at only ~21%. This bottleneck is a key area for policy focus (affordability/literacy).
![Usage-Coverage Gap](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/usage_coverage_gap.png)

#### Insight 5: Event-Indicator Sensitivity
Historically, inclusion progress in Ethiopia is "lumpy"—triggered by major platform launches. Our model uses these event anchors to predict future trajectory kinks.
![Event vs Indicator Impact](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/event_indicator_impact.png)

---

## 3. Next Steps & Detailed Roadmap

### Task 3: Event Impact Modeling (Next Immediate Step)
*   **Goal**: Quantify the relationship between historical events and indicator shifts.
*   **Action Plan**: 
    1.  Build an **Association Matrix** (Events vs. Indicators).
    2.  Model **Temporal Characteristics**: Define the 'Lag' (months before impact) and 'Persistence' (decay of effect) for each event type.
    3.  Benchmark against **Comparable Country Evidence** (using Kenya/Nigeria as proxies where data is sparse).

### Task 4: Forecasting Access and Usage (2025-2027)
*   **Goal**: Produce 3-year projections under different economic conditions.
*   **Action Plan**:
    1.  **Baseline Trend**: Linear/Log-linear regression on historical Findex points.
    2.  **Event-Augmented Model**: Overlay impacts from Task 3 (e.g., adding +X% growth due to the M-Pesa entry lag).
    3.  **Scenario Analysis**: Create **Optimistic** (high policy success), **Base**, and **Pessimistic** (macroeconomic shocks) forecasts with 95% confidence intervals.

### Task 5: Interactive Dashboard Development
*   **Goal**: Create a decision-support tool for the Consortium using Streamlit.
*   **Action Plan**:
    1.  **Overview Module**: Real-time tracking of the P2P/ATM ratio and current inclusion levels.
    2.  **Scenario Playground**: Allow users to toggle future "Events" (e.g., "What if a new foreign bank enters in 2026?") to see forecast shifts.
    3.  **Policy Insights Page**: Direct visual answers to the consortium's core questions regarding the NFIS-II 70% target.

---

## 4. Data Quality & Limitations
- **Constraint**: Low-frequency historical points (every 3 years) necessitates a "structural" modeling approach rather than pure statistical time-series (ARIMA/LSTM).
- **Reliance**: High reliance on "High Confidence" NBE and Operator reports to fill gaps between Findex surveys.
