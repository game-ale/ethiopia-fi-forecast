# Data Enrichment Log

This document tracks all additions and modifications made to the `ethiopia_fi_unified_data.csv` dataset.

## Date: 2026-02-01
**Collected By:** Antigravity

### New Observations
| Record ID | Indicator | Value | Date | Source | Why it's useful |
|-----------|-----------|-------|------|--------|-----------------|
| `REC_0034` | Mobile Internet Usage Rate | 21.4% | 2024-12-31 | DataReportal | Key enabler for digital financial inclusion; correlates with mobile money usage. |
| `REC_0035` | Smartphone Penetration | 29.5% | 2024-12-31 | GSMA Intelligence | Important driver for app-based services (Telebirr/M-Pesa apps). |

### New Events
| Record ID | Event | Date | Category | Description |
|-----------|-------|------|----------|-------------|
| `EVT_0011` | NBE Open Banking Framework | 2025-01-15 | policy | Strategic shift allowing third-party API access to banking infrastructure. |

### New Impact Links
| Record ID | Parent Event | Affected Indicator | Magnitude | Lag | Evidence |
|-----------|--------------|--------------------|-----------|-----|----------|
| `IMP_0015` | `EVT_0011` | `USG_DIGITAL_PAYMENT` | medium | 12mo | Based on Nigerian Open Banking adoption curves. |

## Data Quality Assessment
- **Confidence:** Median confidence remains "High". New research-based data points are "Medium" to "High".
- **Gaps:** Still lacking high-frequency (monthly) transaction data for the most recent months of 2025.
