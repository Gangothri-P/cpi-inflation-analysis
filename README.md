# Project: India State-wise CPI Inflation, Jan–Sep 2026

## Project Scope

This project analyses state-wise Consumer Price Index (CPI) inflation in India using the MoSPI eSankhyiki dataset (base year 2024).

The project focuses on:
- Comparing inflation across Indian states.
- Analysing monthly inflation changes from January to September 2026.
- Comparing inflation across CPI divisions.
- Identifying unusual values and verifying them against original sources.

Excel is used for initial data exploration, cleaning and analysis. Python (Pandas) will be used for further analysis.

## Data

- **Source:** MoSPI eSankhyiki, Consumer Price Index (base year 2024).
- **Downloaded:** 9 November 2026.
- **Size:** 30,030 rows and 15 columns.
- **Observation level:** State × sector × division × month.

## Questions

1. How did Food and Beverages inflation change from January to September 2026 (All India, Combined)?
2. Which state had the highest average CPI (General) inflation, and is that driven by rural or urban prices?
3. How did Health and Transport inflation compare across January to September 2026 (All India, Combined)?
4. Which values look anomalous, and do they change any conclusions?

## Known Limitations

- Only nine months of 2026 are analysed, so trends cover a short period.
- Year-on-year inflation values are blank for 2025 under the new CPI 2024 series.
- Chandigarh Rural has no data; the reason has not yet been verified.
- All India is a national aggregate and is excluded from state rankings.
- Small states and Union Territories may show extreme values. These are flagged for investigation, not automatically removed.
- The dataset does not contain expenditure weights. Therefore, a high inflation rate does not necessarily mean the largest impact on household spending. Food and Beverages has a much larger basket weight than Personal Care.

## Definitions Confirmed

- **Inflation:** The inflation field represents year-on-year percentage change.
- **2025 inflation blanks:** Year-on-year inflation under the new CPI 2024 series starts in January 2026. Index values for 2025 are available.
- **Personal Care division:** Personal care, social protection and miscellaneous goods and services includes items such as gold, diamond, platinum and silver jewellery.

## Sources Checked

1. MoSPI / Press Information Bureau — Official CPI 2024 series release. Primary source to be reviewed and cited.
2. ICRA — Research note on the revised CPI series and expenditure weights: https://www.icra.in/Rating/DownloadResearchSpecialCommentReport?id=6775
3. Canara Bank — CPI inflation note, January 2026: https://www.canarabank.bank.in/documents/d/guest/cpi-inflation-jan-2026
4. The Tribune — January 2026 CPI inflation under the new base year: https://www.tribuneindia.com/news/business/cpi-inflation-for-january-recorded-at-2-75-under-new-base-year/

## Data Quality Notes

- The All India category contains 819 rows (3 sectors × 13 division entries × 21 months).
- Unusual values must be checked against the original source before correction or removal.
- Cleaning decisions and reasons are recorded in `cleaning_log.md`.
- The original raw dataset is preserved.