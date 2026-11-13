# CPI Dataset — Cleaning Log

| What I found | How many rows | What I did | Why |
|---|---:|---|---|
| 2025 inflation values are blank | To be counted | Kept them unchanged | Year-on-year inflation under the new CPI 2024 series starts in January 2026. |
| All India is an aggregate, not an individual state | 819 | Excluded from state comparisons | To avoid mixing national and state-level figures. |
| Unusual or extreme inflation values | To be investigated | Flagged for verification | Extreme values may be genuine and should not be removed without checking the source. |

## Notes
- Original raw data is preserved.
- No values are changed without verification.
- MoSPI is the primary source for checking unusual values.