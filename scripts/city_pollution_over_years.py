# scripts/city_pollution_over_years.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

PROCESSED = "../data/processed/"
VISUALS = "../visuals/"
OUTPUT = "../output/"
os.makedirs(VISUALS, exist_ok=True)
os.makedirs(OUTPUT, exist_ok=True)

def detect_date_col(df):
    for c in ["Date","date","Datetime","datetime","timestamp","Timestamp","DateTime"]:
        if c in df.columns:
            return c
    return None

def main():
    file = PROCESSED + "city_day_cleaned.csv"
    print("Loading:", file)
    df = pd.read_csv(file)
    date_col = detect_date_col(df)
    if not date_col:
        print("No date column. Exiting.")
        return
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col])
    df["year"] = df[date_col].dt.year

    # prefer AQI if available, otherwise PM2.5
    metric = "AQI" if "AQI" in df.columns else ("PM2.5" if "PM2.5" in df.columns else None)
    if not metric:
        print("No AQI or PM2.5 column. Exiting.")
        return

    # compute yearly average per city
    city_year = df.groupby(["City","year"])[metric].mean().reset_index()

    # pick top 6 cities by overall avg
    top_cities = df.groupby("City")[metric].mean().nlargest(6).index.tolist()
    print("Top cities:", top_cities)

    plot_df = city_year[city_year["City"].isin(top_cities)]
    plt.figure(figsize=(12,6))
    sns.lineplot(data=plot_df, x="year", y=metric, hue="City", marker="o", palette="tab10")
    plt.title(f"{metric} trend over years — Top {len(top_cities)} cities", fontsize=16, fontweight='bold')
    plt.xlabel("Year", fontsize=14)
    plt.ylabel(metric, fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    out = VISUALS + "city_pollution_over_years_top6.png"
    plt.savefig(out, dpi=200)
    plt.close()
    print("Saved:", out)

    # Also save a wide CSV of city vs year
    pivot = city_year.pivot(index="City", columns="year", values=metric)
    pivot.to_csv(OUTPUT + "city_yearly_avg.csv")
    print("Saved:", OUTPUT + "city_yearly_avg.csv")

if __name__ == "__main__":
    main()
