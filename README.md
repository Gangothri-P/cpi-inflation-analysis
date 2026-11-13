## Project: India State-wise CPI Inflation, Jan–Sep 2026

### Data
MoSPI eSankhyiki, Consumer Price Index (base year 2024).
Downloaded 9 Nov 2026. 30,030 rows, 15 columns.
One row = state × sector × division × month.

### Questions
1. How did Food and beverages inflation change from Jan to Sep 2026 (All India, Combined)?
2. Which state had the highest average CPI (General) inflation, and is that driven by rural or urban prices?
3. How did Health and Transport inflation compare across Jan to Sep 2026 (All India, Combined)?
4. Which values look anomalous, and do they change any conclusion?

### Known limitations
- Only 9 months of 2026, so "trend" means a short window.
- Inflation values are blank for all of 2025.
- Chandigarh Rural has no data.
- "All India" is an aggregate and is excluded from state rankings.
- Small states and UTs can show extreme values; flagged, not removed.
- No spending weights in the file, so a high inflation rate does not
  show how much a household is affected.

### Definitions to confirm at the source
- Whether `inflation` is year-on-year percentage change.
- What the "Personal care, social protection and miscellaneous goods and services" division contains.
