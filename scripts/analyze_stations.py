import pandas as pd
import matplotlib.pyplot as plt
import os

PROCESSED_PATH = "../data/processed/"
OUTPUT_PATH = "../output/"
VISUALS_PATH = "../visuals/"

# Create folders if missing
os.makedirs(OUTPUT_PATH, exist_ok=True)
os.makedirs(VISUALS_PATH, exist_ok=True)

def analyze_stations():
    file_path = PROCESSED_PATH + "stations_cleaned.csv"

    print(f"📌 Loading: {file_path}")
    df = pd.read_csv(file_path)

    print("Columns found:", df.columns.tolist())

    # Check for required columns
    if "City" not in df.columns or "Station" not in df.columns:
        print("❌ Missing required columns City or Station")
        return

    # Count stations per city
    station_counts = df.groupby("City")["Station"].count().sort_values(ascending=False)

    print("\n🏙️ Stations per city:")
    print(station_counts)

    # Save summary
    summary_file = OUTPUT_PATH + "stations_summary.csv"
    station_counts.to_csv(summary_file)
    print(f"✅ Saved station summary: {summary_file}")

    # Plot
    plt.figure(figsize=(12, 6))
    colors = plt.cm.plasma(np.linspace(0, 1, len(station_counts)))  # Colorful palette
    station_counts.plot(kind="bar", color=colors, edgecolor="black", linewidth=1.5)
    plt.title("Number of Monitoring Stations per City", fontsize=16, fontweight='bold')
    plt.xlabel("City", fontsize=14)
    plt.ylabel("Total Stations", fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    img_path = VISUALS_PATH + "stations_per_city.png"
    plt.savefig(img_path)
    print(f"📊 Saved plot: {img_path}")
    plt.close()

def main():
    analyze_stations()

if __name__ == "__main__":
    main()
