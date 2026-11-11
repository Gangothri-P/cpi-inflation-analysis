# CPI Dataset — Data Dictionary

## Dataset Overview

**Source:** Ministry of Statistics and Programme Implementation (MoSPI), Government of India  
**Dataset:** Consumer Price Index (CPI)  
**Base Year:** 2024  
**Purpose:** Analyse consumer price index and inflation across Indian states, sectors and CPI divisions.

## Column Definitions

| No. | Column | Data Type | Description |
|---:|---|---|---|
| 1 | base_year | Integer | Base year used for calculating the CPI index. |
| 2 | series | String | Identifies the CPI data series, such as Current. |
| 3 | year | Integer | Year for which the CPI observation is recorded. |
| 4 | month | String | Month of the CPI observation. |
| 5 | state | String | State, Union Territory or All India geographical category. |
| 6 | sector | String | Sector classification, such as Rural, Urban or Combined. |
| 7 | division | String | Broad CPI expenditure division, such as Food and beverages or Health. |
| 8 | group | String | Subcategory within a CPI division. |
| 9 | class | String | Further classification within a group. |
| 10 | sub_class | String | More specific classification within a class. |
| 11 | item | String | Individual commodity or service represented in the CPI hierarchy. |
| 12 | code | String | Identification code for the corresponding CPI category or item. |
| 13 | index | Decimal | Consumer Price Index value for the corresponding observation. |
| 14 | inflation | Decimal | Inflation rate associated with the CPI observation, expressed as a percentage. |
| 15 | imputation | Numeric / Nullable | Imputation-related value associated with the observation, where available. |

## Missing Data and Data Quality Notes

1. Some hierarchical classification fields, such as group, class, sub_class and item, may be blank for higher-level aggregate observations.
2. Blank values should not automatically be treated as zero.
3. The imputation column appears blank in some of the displayed observations. Its missing-value pattern requires further verification.
4. State names must be standardized before performing lookups. For example, "NCT of Delhi" and "Delhi" may fail to match because their spellings differ.
5. During Excel analysis, some inflation values were observed to be stored as text rather than numeric values. Numeric conversion is required before reliable numerical sorting and calculations.

## Data Preparation Notes

- Preserve the original raw dataset.
- Use a separate working copy for cleaning and analysis.
- Check missing values and duplicates before analysis.
- Ensure numeric columns are stored as numeric values.
- Standardize state names before joining external reference tables.
