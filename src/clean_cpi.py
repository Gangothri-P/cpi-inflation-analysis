"""Clean the MoSPI CPI file and write an analysis-ready, long-format CSV.

Run from the repo root:
    python src/clean_cpi.py

The raw file is never modified. Every change is made on a copy and listed in cleaning_log.md.
"""
import argparse
from pathlib import Path

import pandas as pd

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
KEY = ["year", "month", "state", "sector", "division"]   # one row = one observation
TEXT_COLS = ["series", "state", "sector", "division", "month"]


def load_raw(path):
    return pd.read_excel(path)


def clean(raw):
    df = raw.copy()

    # 1. Drop columns that are completely empty (no information)
    empty = [c for c in df.columns if df[c].isna().all()]
    df = df.drop(columns=empty)

    # 2. 'index' clashes with DataFrame.index, so rename it
    df = df.rename(columns={"index": "cpi_index"})

    # 3. Remove accidental leading/trailing spaces in text columns
    for c in TEXT_COLS:
        df[c] = df[c].str.strip()

    # 3b. 'code' is an identifier (division number), not a quantity: store as whole-number label, not float
    df["code"] = df["code"].astype("Int64")

    # 4. Month: ordered category + number, and a real date for time charts
    df["month_num"] = df["month"].map({m: i + 1 for i, m in enumerate(MONTHS)})
    df["month"] = pd.Categorical(df["month"], categories=MONTHS, ordered=True)
    df["period"] = pd.to_datetime(dict(year=df["year"], month=df["month_num"], day=1))

    # 5. Flags that make later filtering explicit
    df["is_aggregate"] = df["state"].eq("All India")   # national figure, not a state
    df["has_inflation"] = df["inflation"].notna()      # False for all of 2025 (see cleaning log)

    # 6. Derived (NOT published by MoSPI): month-on-month % change of the index.
    #    Available for 2025 too, because the index exists there even though year-on-year inflation does not.
    df = df.sort_values(["state", "sector", "division", "period"]).reset_index(drop=True)
    grp = df.groupby(["state", "sector", "division"], observed=True)["cpi_index"]
    df["derived_mom_pct"] = grp.pct_change(fill_method=None) * 100

    return df


def validate(df, raw):
    checks = []

    def check(name, ok):
        checks.append((name, bool(ok)))

    check("row count unchanged", len(df) == len(raw))
    check("no duplicate observations", df.duplicated(KEY).sum() == 0)
    check("sectors are Rural/Urban/Combined", set(df["sector"].unique()) == {"Rural", "Urban", "Combined"})
    check("cpi_index has no missing values and is positive", df["cpi_index"].notna().all() and (df["cpi_index"] > 0).all())
    check("inflation is missing only in 2025", set(df.loc[~df["has_inflation"], "year"].unique()) == {2025})
    periods = sorted(df["period"].unique())
    expected = pd.date_range(periods[0], periods[-1], freq="MS")
    check("months are continuous (no gaps)", len(periods) == len(expected))

    print("Validation report")
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    failed = [n for n, ok in checks if not ok]
    if failed:
        raise SystemExit(f"Validation failed: {failed}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", default="data/raw/cpi_1153.xlsx")
    p.add_argument("--out", default="data/cleaned/cpi_clean.csv")
    a = p.parse_args()

    raw = load_raw(a.raw)
    df = clean(raw)
    validate(df, raw)

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"Saved {df.shape[0]} rows x {df.shape[1]} columns to {out}")


if __name__ == "__main__":
    main()
