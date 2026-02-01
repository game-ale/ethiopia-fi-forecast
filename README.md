# Ethiopia Financial Inclusion Forecasting System

## Overview
This project develops a forecasting system to track Ethiopia's digital financial transformation. It predicts progress on two core dimensions of financial inclusion: **Access (Account Ownership)** and **Usage (Digital Payment Adoption)** for the years 2025-2027.

## Project Structure
```text
ethiopia-fi-forecast/
├── data/
│   ├── raw/                      # Starter and enriched unified datasets
│   └── processed/                # Analysis-ready data
├── notebooks/
│   └── EDA.ipynb                 # Task 2: Exploratory Data Analysis
├── src/
│   ├── init_data.py              # Data initialization and CSV conversion
│   ├── enrich_data.py            # Task 1: Dataset enrichment script
│   └── eda.py                    # Static EDA visualization script
├── reports/
│   ├── figures/                  # Generated plots and charts
│   └── eda_summary.md            # Task 2: Key insights and findings
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## Task Progress

### Task 1: Data Exploration and Enrichment (Completed)
- **Unified Schema:** All records (observations, events, impact links, targets) share a single structure.
- **Enrichment:** Added metrics for **Smartphone Penetration** (29.5%) and **Mobile Internet Usage** (21.4%) to fill enabler gaps.
- **New Events:** Cataloged the **NBE Open Banking Framework (2025)** as a significant policy driver.
- **Deliverables:** `data/raw/ethiopia_fi_unified_data.csv`, `data_enrichment_log.md`.

### Task 2: Exploratory Data Analysis (Completed)
- **Growth Analysis:** Identified a growth deceleration in account ownership (46% to 49% from 2021-2024).
- **Milestone:** P2P transactions surpassed ATM withdrawals for the first time in late 2024.
- **Gender Gap:** Significant 18pp gap in account ownership persists.
- **Deliverables:** `notebooks/EDA.ipynb`, `reports/eda_summary.md`.

## Setup and Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize data:
   ```bash
   python src/init_data.py
   python src/enrich_data.py
   ```
4. Run EDA:
   ```bash
   python src/eda.py
   ```
   Or open `notebooks/EDA.ipynb` in a Jupyter environment.

## Key Insights Summary
1. **The Ownership Paradox:** Despite 60M+ mobile money registrations, Findex-reported account ownership only grew by 3pp. This suggests a transition from "registration" to "meaningful usage" is still ongoing, or significant multi-homing exists.
2. **Digital First:** The P2P/ATM crossover ratio of 1.08 indicates the ecosystem is maturing beyond cash.
3. **Usage Gap:** 4G coverage (70%+) far outpaces mobile internet usage (21%), pointing to affordability and literacy barriers.
