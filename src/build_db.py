"""Build a SQLite database for the CPI project from the cleaned CSV and the state-region lookup.

Run from the repo root (after python src/clean_cpi.py):
    python src/build_db.py

Creates data/cpi.db with two tables:
    cpi    one row = state x sector x division x month   (the primary key enforces this)
    zones  one row = state -> region_group              (lookup table; 'All India' is deliberately NOT in it)
The database is rebuilt from scratch each time, so it is never edited by hand and is not committed to Git.
"""
import argparse
import sqlite3
from pathlib import Path

import pandas as pd

DDL = """
DROP TABLE IF EXISTS cpi;
DROP TABLE IF EXISTS zones;

CREATE TABLE zones (
    state        TEXT PRIMARY KEY,
    region_group TEXT NOT NULL
);

CREATE TABLE cpi (
    year            INTEGER NOT NULL,
    month           TEXT    NOT NULL,
    month_num       INTEGER NOT NULL CHECK (month_num BETWEEN 1 AND 12),
    period          TEXT    NOT NULL,
    state           TEXT    NOT NULL,
    sector          TEXT    NOT NULL CHECK (sector IN ('Rural', 'Urban', 'Combined')),
    division        TEXT    NOT NULL,
    code            INTEGER,
    cpi_index       REAL    NOT NULL,
    inflation       REAL,
    is_aggregate    INTEGER NOT NULL CHECK (is_aggregate IN (0, 1)),
    has_inflation   INTEGER NOT NULL CHECK (has_inflation IN (0, 1)),
    derived_mom_pct REAL,
    PRIMARY KEY (year, month_num, state, sector, division)
);

CREATE INDEX idx_cpi_state ON cpi (state);
CREATE INDEX idx_cpi_division ON cpi (division);
"""

CPI_COLS = ["year", "month", "month_num", "period", "state", "sector", "division", "code",
            "cpi_index", "inflation", "is_aggregate", "has_inflation", "derived_mom_pct"]


def to_rows(df):
    """DataFrame -> list of tuples with plain Python values; missing values become None (SQL NULL)."""
    df = df.astype(object).where(df.notna(), None)
    return list(df.itertuples(index=False, name=None))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--clean", default="data/cleaned/cpi_clean.csv")
    p.add_argument("--zones", default="data/reference/state_regions.csv")
    p.add_argument("--db", default="data/cpi.db")
    a = p.parse_args()

    cpi = pd.read_csv(a.clean)
    zones = pd.read_csv(a.zones)

    # Fail early, with a useful message, if the lookup does not cover every state
    states = set(cpi.loc[cpi["is_aggregate"] == False, "state"])  # noqa: E712
    missing = sorted(states - set(zones["state"]))
    if missing:
        raise SystemExit(f"These states are in the CPI data but not in {a.zones}: {missing}\n"
                         "Fix the spelling in the lookup file (never in the raw data).")
    if not zones["state"].is_unique:
        raise SystemExit("state_regions.csv has duplicate states")

    cpi["code"] = cpi["code"].astype("Int64")
    for c in ["is_aggregate", "has_inflation"]:
        cpi[c] = cpi[c].astype(int)
    cpi = cpi[CPI_COLS]

    Path(a.db).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(a.db)
    conn.executescript(DDL)
    conn.executemany("INSERT INTO zones (state, region_group) VALUES (?, ?)", to_rows(zones[["state", "region_group"]]))
    conn.executemany(f"INSERT INTO cpi ({', '.join(CPI_COLS)}) VALUES ({', '.join('?' * len(CPI_COLS))})", to_rows(cpi))
    conn.commit()

    n_cpi = conn.execute("SELECT COUNT(*) FROM cpi").fetchone()[0]
    n_zones = conn.execute("SELECT COUNT(*) FROM zones").fetchone()[0]
    assert n_cpi == len(cpi), "row count mismatch between CSV and database"
    print(f"Built {a.db}: cpi = {n_cpi} rows, zones = {n_zones} rows")
    conn.close()


if __name__ == "__main__":
    main()
