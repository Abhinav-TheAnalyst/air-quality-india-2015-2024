import os
import pandas as pd

OUTPUT = "../output/"
VISUALS = "../visuals/"

os.makedirs(OUTPUT, exist_ok=True)

# Load key outputs if they exist
summary_lines = []
summary_lines.append("# Summary Report\n")
summary_lines.append("Generated from processed outputs and visuals.\n")

# Top polluted cities
try:
    top = pd.read_csv(os.path.join(OUTPUT, "top_polluted_cities.csv"))
    summary_lines.append("## Top Polluted Cities (Avg AQI)\n")
    for i, row in top.head(10).iterrows():
        summary_lines.append(f"- {row['City']}: {row['AQI']:.1f}\n")
    summary_lines.append("\n")
except Exception:
    summary_lines.append("## Top Polluted Cities (data not available)\n\n")

# Stations summary
try:
    stations = pd.read_csv(os.path.join(OUTPUT, "stations_summary.csv"))
    summary_lines.append("## Stations Summary\n")
    for i, row in stations.head(10).iterrows():
        summary_lines.append(f"- {row['City']}: {int(row['Station'])} stations\n")
    summary_lines.append("\n")
except Exception:
    summary_lines.append("## Stations Summary (data not available)\n\n")

# Seasonal means
try:
    season = pd.read_csv(os.path.join(OUTPUT, "seasonal_means_by_pollutant.csv"))
    summary_lines.append("## Seasonal Means by Pollutant\n")
    summary_lines.append(season.to_markdown(index=False))
    summary_lines.append("\n\n")
except Exception:
    summary_lines.append("## Seasonal Means (data not available)\n\n")

# Missing values summary
try:
    mv = pd.read_csv(os.path.join(OUTPUT, "missing_values_summary.csv"))
    summary_lines.append("## Missing Values Summary\n")
    summary_lines.append(mv.to_markdown(index=False))
    summary_lines.append("\n\n")
except Exception:
    summary_lines.append("## Missing Values Summary (data not available)\n\n")

# Link to visuals
summary_lines.append("## Visuals\n")
if os.path.exists(VISUALS):
    for f in sorted(os.listdir(VISUALS)):
        if f.endswith('.png') or f.endswith('.html'):
            summary_lines.append(f"- {os.path.join('visuals', f)}\n")

summary_lines.append("\n## How to regenerate this summary\n")
summary_lines.append("Run `python scripts/generate_summary.py` from the `scripts/` folder or from the repo root.\n")

# Write summary
out_file = os.path.join(OUTPUT, "summary_report.md")
with open(out_file, 'w', encoding='utf-8') as f:
    f.writelines([line + '\n' if not line.endswith('\n') else line for line in summary_lines])

print("Created:", out_file)
