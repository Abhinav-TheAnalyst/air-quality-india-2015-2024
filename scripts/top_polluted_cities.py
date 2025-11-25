import pandas as pd
import matplotlib.pyplot as plt
import os

PROCESSED_PATH = "../data/processed/"
OUTPUT_PATH = "../output/"
VISUALS_PATH = "../visuals/"

# Ensure folders exist
os.makedirs(OUTPUT_PATH, exist_ok=True)
os.makedirs(VISUALS_PATH, exist_ok=True)

def top_polluted_cities_report():
    file_path = PROCESSED_PATH + "city_day_cleaned.csv"
    print(f"📌 Loading {file_path}")

    df = pd.read_csv(file_path)

    # Ensure AQI column exists
    if "AQI" not in df.columns:
        print("❌ AQI column not found in city_day_cleaned.csv")
        return

    # Drop rows missing AQI
    df = df.dropna(subset=["AQI"])

    # Convert AQI to numeric (clean bad data)
    df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")
    df = df.dropna(subset=["AQI"])

    # Compute average AQI per city
    top_cities = df.groupby("City")["AQI"].mean().sort_values(ascending=False)

    # Get top 10 most polluted
    top10 = top_cities.head(10)

    # Save to CSV
    csv_path = OUTPUT_PATH + "top_polluted_cities.csv"
    top10.to_csv(csv_path)
    print(f"✅ Saved CSV report: {csv_path}")

    # Plot and save chart
    plt.figure(figsize=(12, 6))
    top10.plot(kind="bar", edgecolor="black")
    plt.title("Top 10 Most Polluted Cities in India (Avg AQI 2015–2024)")
    plt.xlabel("City")
    plt.ylabel("Average AQI")
    plt.tight_layout()

    img_path = VISUALS_PATH + "top_polluted_cities.png"
    plt.savefig(img_path)
    print(f"📊 Saved visual: {img_path}")

    plt.close()

def main():
    top_polluted_cities_report()

if __name__ == "__main__":
    main()
