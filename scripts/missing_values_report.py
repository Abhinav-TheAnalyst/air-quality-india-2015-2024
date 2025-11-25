# scripts/missing_values_report.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

PROCESSED = "../data/processed/"
OUTPUT = "../output/"
VISUALS = "../visuals/"
os.makedirs(OUTPUT, exist_ok=True)
os.makedirs(VISUALS, exist_ok=True)

def main():
    file = PROCESSED + "city_day_cleaned.csv"
    print("Loading:", file)
    df = pd.read_csv(file)

    # missing counts and fraction
    miss = df.isna().sum()
    miss_frac = (miss / len(df)).sort_values(ascending=False)
    miss_df = pd.concat([miss, miss_frac], axis=1)
    miss_df.columns = ["missing_count", "missing_fraction"]
    miss_df.to_csv(OUTPUT + "missing_values_summary.csv")
    print("Saved:", OUTPUT + "missing_values_summary.csv")

    # heatmap for top 25 columns with missing values
    top_cols = miss_frac[miss_frac > 0].head(25).index.tolist()
    if not top_cols:
        print("No missing values found.")
        return

    plt.figure(figsize=(12,6))
    sns.heatmap(df[top_cols].isna().transpose(), cbar=False)
    plt.title("Missing values heatmap (rows=columns)")
    plt.xlabel("Row index (truncated)")
    plt.ylabel("Columns")
    out = VISUALS + "missing_values_heatmap.png"
    plt.tight_layout()
    plt.savefig(out, dpi=200)
    plt.close()
    print("Saved:", out)

if __name__ == "__main__":
    main()
