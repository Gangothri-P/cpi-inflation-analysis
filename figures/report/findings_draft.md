# Findings draft – CPI inflation, January–September 2026

All state-level summaries below exclude the `All India` aggregate. State means are **unweighted**; they do not reproduce the official national weighted CPI.

## 1. All India Combined division trends
- **What the numbers show:** Across the nine months, Personal care, social protection and miscellaneous goods and services had the highest mean inflation (17.10%; median 17.66%), while Information and communication had the lowest mean (0.78%; median 0.43%). CPI (General) averaged 4.00% (median 3.93%).
- **Guess (not established):** The high personal-care average may reflect sustained price increases in some components, while the lower information-and-communication rate may reflect slower price changes in that division.
- **Limitation:** These are nine monthly observations, not a weighted decomposition; monthly values are serially related, and a division mean does not reveal which items drove the change.

## 2. September cross-state CPI (General) spread
- **What the numbers show:** Across 36 states, the median was 5.06%, Q1 4.035%, Q3 5.87%, and IQR 1.835 percentage points. The 1.5×IQR fences were 1.283% and 8.623%; no state fell outside them.
- **Guess (not established):** The lack of IQR-flagged observations suggests September general inflation was not dominated by a single unusually high or low state value under this rule.
- **Limitation:** IQR fences are a screening convention, not a test of data quality or economic unusualness; a value inside the fences can still be important.

## 3. Cross-state spread over time
- **What the numbers show:** The max–min gap narrowed from 4.80 pp in January to 4.01 pp in September, while the cross-state standard deviation rose from 0.99 pp to 1.13 pp.
- **Guess (not established):** The extremes moved closer in range, while more of the distribution may have spread away from its mean; this is not a simple convergence story.
- **Limitation:** Range and standard deviation describe different aspects of dispersion; neither explains the causes of state-level movements or accounts for spatial dependence.

## 4. September rural–urban difference
- **What the numbers show:** For 35 states with both sectors, the mean Rural-minus-Urban CPI (General) gap was 0.91 pp and the median was 1.00 pp. Rural inflation was higher in 30 of 35 paired states.
- **Guess (not established):** Rural inflation may have been higher across most states because of differences in consumption baskets or local price movements.
- **Limitation:** The comparison is descriptive and unweighted; Chandigarh is excluded because the source contains no Rural rows, and the two sector rates are based on separate price samples.

## 5. September division-level extreme values
- **What the numbers show:** The 1.5×IQR rule flags five states in Paan, tobacco and intoxicants, including Ladakh at 38.07%. It also flags Ladakh in Education services and several states in other divisions. Ladakh's tobacco observation is retained.
- **Guess (not established):** These high values may reflect genuine local price movements, basket composition, or measurement/source effects; the file alone cannot distinguish these explanations.
- **Limitation:** An IQR flag is not evidence of an error. No flagged value was deleted or adjusted; extreme values should be checked against the original release and underlying collection notes.

## 6. Index-based validation
- **What the numbers show:** Recomputed year-on-year inflation matches the published 2026 inflation column closely across 12,870 rows; the maximum absolute difference is 0.0141 pp and every difference is at most 0.02 pp.
- **Guess (not established):** The small residuals are consistent with inflation rates calculated from index values rounded to two decimal places.
- **Limitation:** This check verifies internal arithmetic against rounded published indices; it does not validate the original price collection or index construction.

## 7. Combined index check and external headline
- **What the numbers show:** Combined index lies between Rural and Urban in all 4,095 complete 2026 state/month/division comparisons. Chandigarh has no Rural rows. The project September headline is 5.54%, matching MoSPI's published 5.54%.
- **Guess (not established):** The internal ordering and external match support consistency of the cleaned series for these checks.
- **Limitation:** Passing these checks does not prove every source row is correct. The external headline is one national-level cross-check, not a full independent audit.

## 8. Pre-specified inference results
- **What the numbers show:** Rural-minus-Urban September differences were non-normal (Shapiro–Wilk p=0.0319); Wilcoxon signed-rank p=9.76e-06, median difference 1.00 pp (bootstrap 95% CI 0.64 to 1.45). January–September differences passed the normality check (p=0.970); paired t-test mean increase was 2.63 pp (95% CI 2.24 to 3.01; p=9.42e-16). Food and general inflation had Spearman rho=0.824 (bootstrap 95% CI 0.620 to 0.928; p=6.47e-10).
- **Guess (not established):** The results are consistent with a broad rural-over-urban gap, an increase from January to September, and a strong positive cross-state association between food and general inflation.
- **Limitation:** States are the full observed set, not a random sample; p-values are descriptive. Price-quote sampling uncertainty is not available, and neighbouring states may share shocks, violating independence assumptions.
