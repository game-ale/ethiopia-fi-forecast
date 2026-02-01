# Interim Report: Forecasting Financial Inclusion in Ethiopia

**Date:** February 1, 2026  
**Analyst:** Antigravity (Data Scientist, Selam Analytics)  
**Status:** Task 1 & Task 2 Complete  

---

## 1. Executive Summary
This report summarizes the initial phases of the Ethiopia Financial Inclusion Forecasting project. Progress includes the unification and enrichment of regional financial data and a deep-dive exploratory analysis of inclusion trends from 2011 to 2024. Key findings highlight a "Digital First" transition where P2P transactions have surpassed cash withdrawals, despite a localized stagnation in overall account ownership growth.

---

## 2. Data Enrichment Summary
The provided dataset was enriched with four strategic records to better capture growth enablers and future policy drivers.

| Record ID | Type | Pillar | Indicator / Event | Why it was added |
|-----------|------|--------|--------------------|------------------|
| `REC_0034` | Obs | ACCESS | Mobile Internet Usage (21.4%) | Critical enabler for mobile money; helps explain the gap between coverage and usage. |
| `REC_0035` | Obs | ACCESS | Smartphone Penetration (29.5%) | Differentiates between USSD-based basic inclusion and app-based advanced usage. |
| `EVT_0011` | Event | Policy | NBE Open Banking Framework | A major 2025 milestone that will drive future fintech API integrations. |
| `IMP_0015` | Link | USAGE | Open Banking Impact Link | Bridges the new policy event to `USG_DIGITAL_PAYMENT` projections. |

---

## 3. Key Insights from Exploratory Data Analysis (EDA)

### Insight 1: The "Ownership Paradox" (2021-2024 slowdown)
**Observation:** Account ownership grew only 3 percentage points (46% to 49%) between 2021 and 2024.  
![Account Ownership Trend](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/account_ownership_trend.png)  
**Analysis:** This stagnation occurred despite the launch of Telebirr (54M users) and M-Pesa (10M users). This suggests that new mobile money users are largely individuals who already held bank accounts (multi-homing) or that registration has not yet converted to the "account ownership" definition used by Findex.

### Insight 2: Maturity Milestone: P2P > ATM
**Observation:** Interoperable P2P transfers have officially surpassed ATM cash withdrawals in volume.  
![P2P vs ATM Transaction Volume](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/p2p_vs_atm.png)  
**Analysis:** With a crossover ratio of 1.08, Ethiopia has reached a "Digital First" tipping point. The growth of EthSwitch-enabled transfers is outpacing cash-out demand.

### Insight 3: The Persistent Gender Gap
**Observation:** A gender gap of 18 percentage points remains in account ownership.  
![Account Ownership Gender Gap](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/gender_gap.png)  
**Analysis:** Male ownership is approaching 60%, while female ownership remains significantly lower. Policy interventions like Fayda ID are categorized as potential "gap reducers" in our upcoming models.

### Insight 4: The "Usage-Coverage Gap"
**Observation:** 4G population coverage (70%+) significantly outstrips actual mobile internet usage (21%).  
**Analysis:** Infrastructure investment has successfully provided the "rails," but affordability (hit by FX reforms) and digital literacy remain significant barriers to turning coverage into inclusion.

### Insight 5: Event Sensitivity
**Observation:** Historical data shows sharp "kinks" in adoption curves following major infrastructure launches (e.g., Telebirr in 2021).  
![Financial Inclusion Events Timeline](file:///C:/weak10/ethiopia-fi-forecast/reports/figures/event_timeline.png)  
**Analysis:** Most inclusion progress in Ethiopia is "event-driven" rather than purely organic trend-driven, necessitating the "Event-Augmented" forecasting model planned for Task 4.

---

## 4. Preliminary Observations on Event-Indicator Relationships
- **Product Launches (Telebirr/M-Pesa):** High immediate impact on **Usage** metrics (P2P counts) with a 3-6 month lag.
- **Infrastructure (Fayda ID):** High potential impact on **Access** but with a long 12-24 month lag as registration filters into financial KYC processes.
- **Economic Shocks (FX Reform):** Negative pressure on **Affordability**, potentially slowing mid-term digital adoption due to increased smartphone and data costs.

---

## 5. Data Limitations
1. **Low Frequency:** Findex data points only exist every 3 years, making high-fidelity time series modeling difficult.
2. **"Registered vs. Active" Gap:** Provider-side data (65M+ accounts) is heavily skewed by inactive registrations compared to demand-side survey data.
3. **Qualitative Gaps:** Sparse data on "Trust" and "Service Quality," which are essential components of the World Bank's deeper inclusion pillars.

---

**Next Steps:** Proceeding to Task 3 (Event Impact Modeling) to quantify the relationship between events and indicator shifts.
