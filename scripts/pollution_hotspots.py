# scripts/pollution_hotspots.py
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

PROCESSED = "../data/processed/"
VISUALS = "../visuals/"
OUTPUT = "../output/"
os.makedirs(VISUALS, exist_ok=True)
os.makedirs(OUTPUT, exist_ok=True)

def main():
    file = PROCESSED + "city_day_cleaned.csv"
    print("Loading:", file)
    df = pd.read_csv(file)

    # choose pollutant columns
    poll_cols = [c for c in ["PM2.5","PM10","NO2","SO2","O3","CO"] if c in df.columns]
    if not poll_cols:
        # fallback: pick numeric columns that look like pollutants
        poll_cols = [c for c in df.select_dtypes("number").columns if c.lower() not in ("aqi",)]
    print("Using pollutant columns:", poll_cols)

    # compute city-level averages
    city_avg = df.groupby("City")[poll_cols].mean().dropna()
    if city_avg.shape[0] < 3:
        print("Not enough cities to cluster.")
        return

    scaler = StandardScaler()
    X = scaler.fit_transform(city_avg)

    # choose K (simple heuristic: sqrt(n))
    k = max(2, int(np.sqrt(city_avg.shape[0])))
    print("Clustering with K =", k)
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    city_avg["cluster"] = labels

    city_avg.to_csv(OUTPUT + "city_pollution_clusters.csv")
    print("Saved cluster assignment:", OUTPUT + "city_pollution_clusters.csv")

    # Plot clusters on a 2D PCA-like scatter (use first two PCA components via SVD)
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    coords = pca.fit_transform(X)
    plt.figure(figsize=(10,7))
    sns.scatterplot(x=coords[:,0], y=coords[:,1], hue=labels, palette="tab10", s=100)
    for i, city in enumerate(city_avg.index):
        plt.text(coords[i,0]+0.02, coords[i,1]+0.02, city, fontsize=8)
    plt.title("City Pollution Clusters (based on average pollutant levels)")
    out = VISUALS + "pollution_hotspots_clusters.png"
    plt.tight_layout()
    plt.savefig(out, dpi=200)
    plt.close()
    print("Saved:", out)

if __name__ == "__main__":
    main()
