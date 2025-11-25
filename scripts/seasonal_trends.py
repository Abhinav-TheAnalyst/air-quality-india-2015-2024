# scripts/seasonal_trends.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

PROCESSED = "../data/processed/"
VISUALS = "../visuals/"
OUTPUT = "../output/"

os.makedirs(VISUALS, exist_ok=True)
os.makedirs(OUTPUT, exist_ok=True)

# helper to detect date column
POSSIBLE_DATE_COLUMNS = ["Date","date","Datetime","datetime","timestamp","Timestamp","DateTime"]

def find_date_col(df):
    for c in POSSIBLE_DATE_COLUMNS:
        if c in df.columns:
            return c
    # fallback: try any datetime-like column
    for c in df.columns:
        if "date" in c.lower() or "time" in c.lower():
            return c
    return None

def season_of_month(m):
    # DJF (winter), MAM (spring), JJA (summer), SON (autumn)
    if m in [12,1,2]:
        return "Winter (DJF)"
    if m in [3,4,5]:
        return "Spring (MAM)"
    if m in [6,7,8]:
        return "Summer (JJA)"
    return "Autumn (SON)"

def main():
    file = PROCESSED + "city_day_cleaned.csv"
    print("Loading:", file)
    df = pd.read_csv(file)
    date_col = find_date_col(df)
    if not date_col:
        print("No date column found. Exiting.")
        return
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col])
    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["season"] = df["month"].apply(season_of_month)

    pollutant_cols = [c for c in df.columns if c.lower().replace('.','').startswith("pm") or c.lower() in ("pm2.5","pm10","no2","so2","co","o3","no")]
    # fallback list if above is empty
    if not pollutant_cols:
        candidates = ["PM2.5","PM10","NO2","SO2","CO","O3","NO"]
        pollutant_cols = [c for c in candidates if c in df.columns]

    print("Pollutants detected:", pollutant_cols)

    # seasonal means across entire dataset
    season_mean = df.groupby("season")[pollutant_cols].mean().reindex(["Winter (DJF)","Spring (MAM)","Summer (JJA)","Autumn (SON)"])
    season_mean.to_csv(OUTPUT + "seasonal_means_by_pollutant.csv")
    print("Saved seasonal means:", OUTPUT + "seasonal_means_by_pollutant.csv")

    # Plot each pollutant seasonal bar chart
    for col in pollutant_cols:
        plt.figure(figsize=(7,5))
        sns.barplot(x=season_mean.index, y=season_mean[col].values)
        plt.title(f"Seasonal average — {col}")
        plt.ylabel(col)
        plt.xlabel("")
        plt.xticks(rotation=15)
        fn = VISUALS + f"seasonal_{col.replace('.','').lower()}.png"
        plt.tight_layout()
        plt.savefig(fn, dpi=200)
        plt.close()
        print("Saved:", fn)

if __name__ == "__main__":
    main()
