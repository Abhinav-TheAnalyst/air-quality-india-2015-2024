# scripts/city_comparison_dashboard.py
import pandas as pd
import plotly.express as px
import os

PROCESSED = "../data/processed/"
VISUALS = "../visuals/"
os.makedirs(VISUALS, exist_ok=True)

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

    metric = "PM2.5" if "PM2.5" in df.columns else ("AQI" if "AQI" in df.columns else None)
    if not metric:
        print("No PM2.5 or AQI. Exiting.")
        return

    # choose top 6 cities
    top = df.groupby("City")[metric].mean().nlargest(6).index.tolist()
    dash_df = df[df["City"].isin(top)].copy()

    # simple interactive figure
    fig = px.line(dash_df, x=date_col, y=metric, color="City",
                  title=f"{metric} over time — Top 6 cities",
                  labels={date_col:"Date", metric:metric})
    out_html = VISUALS + "city_comparison_dashboard.html"
    fig.write_html(out_html)
    print("Saved interactive dashboard:", out_html)

if __name__ == "__main__":
    main()
