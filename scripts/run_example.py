import os
import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def find_pm_column(cols):
    # common variants
    targets = ["pm2.5", "pm25", "pm_2_5", "pm2_5", "pm_2.5", "pm25_ugm3", "pm25_mean"]
    lower = {c.lower(): c for c in cols}
    for t in targets:
        if t in lower:
            return lower[t]
    # fallback: any column with 'pm' and '2' in name
    for c in cols:
        ln = c.lower()
        if "pm" in ln and "2" in ln:
            return c
    return None


def main():
    repo_root = Path(__file__).resolve().parents[1]
    data_path = repo_root / "data" / "processed" / "city_day_cleaned.csv"

    if not data_path.exists():
        print(f"Data file not found: {data_path}")
        print("Make sure you have processed the data or place a sample CSV at this path.")
        sys.exit(1)

    print(f"Loading: {data_path}")
    df = pd.read_csv(data_path)

    print("\n=== Quick summary ===")
    print("Rows:", len(df))
    print("Columns:", len(df))
    print(df.columns.tolist())
    print("\nTop 5 rows:\n", df.head(5).to_string())

    pm_col = find_pm_column(df.columns)
    if pm_col is None:
        print("\nNo PM2.5-like column detected. Skipping plot generation.")
        return

    # Try to parse date column
    date_cols = [c for c in df.columns if "date" in c.lower() or "time" in c.lower()]
    if date_cols:
        date_col = date_cols[0]
        try:
            df[date_col] = pd.to_datetime(df[date_col])
        except Exception:
            date_col = None
    else:
        date_col = None

    # Make a small example plot: PM2.5 trend for the top city (by count)
    city_col = None
    for c in df.columns:
        if c.lower() in ("city", "city_name", "cityname"):
            city_col = c
            break

    out_dir = repo_root / "visuals"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "run_example_pm25.png"

    if city_col and date_col:
        top_city = df[city_col].value_counts().idxmax()
        sub = df[df[city_col] == top_city].dropna(subset=[pm_col, date_col])
        if sub.empty:
            print("No usable rows for plotting.")
            return
        sub = sub.sort_values(date_col)
        plt.figure(figsize=(10, 4))
        plt.plot(sub[date_col], sub[pm_col], marker="o", linewidth=0.7, color='crimson', markersize=2)
        plt.title(f"{pm_col} over time — {top_city}")
        plt.xlabel(date_col)
        plt.ylabel(pm_col)
        plt.tight_layout()
        plt.savefig(out_path)
        plt.close()
        print(f"Saved example plot to: {out_path}")
    else:
        # If no city/date columns, show distribution
        plt.figure(figsize=(6, 4))
        df[pm_col].dropna().hist(bins=40, color='skyblue', edgecolor='black')
        plt.title(f"Distribution of {pm_col}")
        plt.xlabel(pm_col)
        plt.tight_layout()
        plt.savefig(out_path)
        plt.close()
        print(f"Saved example histogram to: {out_path}")


if __name__ == "__main__":
    main()
