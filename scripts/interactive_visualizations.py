import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_DIR = Path(__file__).resolve().parents[1]
CLEAN_PATH = BASE_DIR / 'data' / 'processed'
VIS_PATH = BASE_DIR / 'visuals'

# Ensure output directory exists
VIS_PATH.mkdir(parents=True, exist_ok=True)

def create_interactive_pm25_trend(filename):
    """Create interactive PM2.5 trend plot."""
    file_path = CLEAN_PATH / filename
    if not file_path.exists():
        logging.warning(f"File not found: {file_path}. Skipping.")
        return

    df = pd.read_csv(file_path)

    if "Datetime" not in df.columns or "PM2.5" not in df.columns:
        logging.warning(f"Required columns not found in {filename}. Skipping.")
        return

    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df = df.dropna(subset=['PM2.5'])

    # Reduce size by focusing on top cities and using monthly resampling
    df = df.set_index('Datetime')
    if "City" in df.columns:
        # pick top N cities by mean PM2.5 to keep the HTML small
        top_n = 6
        city_means = df.groupby('City')['PM2.5'].mean().sort_values(ascending=False)
        top_cities = city_means.head(top_n).index.tolist()
        df_top = df[df['City'].isin(top_cities)]
        monthly_pm25 = df_top.groupby('City')['PM2.5'].resample('M').mean().reset_index()
        fig = px.line(monthly_pm25, x='Datetime', y='PM2.5', color='City',
                      title=f'Interactive Monthly PM2.5 Trends (Top {top_n} Cities) ({filename})',
                      color_discrete_sequence=px.colors.qualitative.Set1)
    else:
        monthly_pm25 = df['PM2.5'].resample('M').mean().reset_index()
        fig = px.line(monthly_pm25, x='Datetime', y='PM2.5',
                      title=f'Interactive Monthly PM2.5 Trend ({filename})')

    fig.update_layout(xaxis_title='Date', yaxis_title='PM2.5')
    out_path = VIS_PATH / filename.replace(".csv", "_pm25_trend_interactive.html")
    # Use the CDN-hosted plotly.js to keep files smaller and avoid huge embedded bundles.
    fig.write_html(str(out_path), include_plotlyjs='cdn', full_html=True)
    logging.info(f"Saved interactive PM2.5 trend: {out_path}")

def create_interactive_top_cities():
    """Create interactive bar chart of top polluted cities."""
    file_path = CLEAN_PATH / "city_day_cleaned.csv"
    if not file_path.exists():
        logging.warning(f"File not found: {file_path}. Skipping top cities chart.")
        return
    df = pd.read_csv(file_path)

    if "City" not in df.columns or "AQI" not in df.columns:
        logging.warning("Required columns not found. Skipping top cities chart.")
        return

    top_cities = df.groupby("City")["AQI"].mean().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(top_cities, x='City', y='AQI',
                 title='Top 10 Most Polluted Cities (Average AQI)',
                 color='AQI', color_continuous_scale='Plasma')
    fig.update_layout(xaxis_title='City', yaxis_title='Average AQI')

    out_path = VIS_PATH / "top_polluted_cities_interactive.html"
    fig.write_html(str(out_path), include_plotlyjs='cdn', full_html=True)
    logging.info(f"Saved interactive top cities chart: {out_path}")

def create_interactive_seasonal_trends():
    """Create interactive seasonal trends."""
    file_path = CLEAN_PATH / "city_day_cleaned.csv"
    if not file_path.exists():
        logging.warning(f"File not found: {file_path}. Skipping seasonal trends.")
        return
    df = pd.read_csv(file_path)

    if "Datetime" not in df.columns or "PM2.5" not in df.columns:
        logging.warning("Required columns not found. Skipping seasonal trends.")
        return

    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df['Month'] = df['Datetime'].dt.month
    df['Year'] = df['Datetime'].dt.year

    monthly_pm25 = df.groupby(['Year', 'Month'])['PM2.5'].mean().reset_index()
    monthly_pm25['Date'] = pd.to_datetime(monthly_pm25[['Year', 'Month']].assign(DAY=1))

    fig = px.line(monthly_pm25, x='Date', y='PM2.5',
                  title='Seasonal PM2.5 Trends Over Years')
    fig.update_layout(xaxis_title='Date', yaxis_title='PM2.5')

    out_path = VIS_PATH / "seasonal_pm25_trends_interactive.html"
    fig.write_html(str(out_path), include_plotlyjs='cdn', full_html=True)
    logging.info(f"Saved interactive seasonal trends: {out_path}")

def create_interactive_correlation_heatmap(filename):
    """Create interactive correlation heatmap."""
    file_path = CLEAN_PATH / filename
    if not file_path.exists():
        logging.warning(f"File not found: {file_path}. Skipping correlation heatmap.")
        return
    df = pd.read_csv(file_path)

    pollutants = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
    available_pollutants = [p for p in pollutants if p in df.columns]

    if len(available_pollutants) < 2:
        logging.warning("Not enough pollutants for correlation analysis.")
        return

    corr_matrix = df[available_pollutants].corr()

    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0))

    fig.update_layout(title=f'Interactive Pollutant Correlation Matrix ({filename})')

    out_path = VIS_PATH / filename.replace(".csv", "_correlation_interactive.html")
    fig.write_html(str(out_path), include_plotlyjs='cdn', full_html=True)
    logging.info(f"Saved interactive correlation heatmap: {out_path}")

def main():
    # Create interactive visualizations for city_day data
    create_interactive_pm25_trend("city_day_cleaned.csv")
    create_interactive_top_cities()
    create_interactive_seasonal_trends()
    create_interactive_correlation_heatmap("city_day_cleaned.csv")

if __name__ == "__main__":
    main()
