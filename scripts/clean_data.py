import pandas as pd
import os

RAW_PATH = "../data/raw/"
PROCESSED_PATH = "../data/processed/"

files = [
    "city_day.csv",
    "city_hour.csv",
    "station_day.csv",
    "station_hour.csv",
    "stations.csv"
]

def clean_file(filename):
    print(f"Cleaning {filename}...")
    df = pd.read_csv(RAW_PATH + filename)

    # Basic cleaning
    df = df.drop_duplicates()
    df = df.dropna(how='all')

    # Save cleaned file
    output_name = filename.replace(".csv", "_cleaned.csv")
    df.to_csv(PROCESSED_PATH + output_name, index=False)
    print(f"Saved cleaned file: {output_name}")

def main():
    for f in files:
        clean_file(f)

if __name__ == "__main__":
    main()
