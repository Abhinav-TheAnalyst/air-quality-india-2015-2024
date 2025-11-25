# scripts/generate_report.py
import os
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image

VISUALS = "../visuals/"
OUTPUT = "../output/"
os.makedirs(OUTPUT, exist_ok=True)

# list of images to include (common outputs from other scripts)
images = [
    "pm25_trend.png",  # may exist if earlier script created it
    "seasonal_pm25.png",  # example names; include what you generated
    "city_pollution_over_years_top6.png",
    "aqi_category_distribution.png",
    "top10_polluted.png",
    "top10_cleanest.png",
    "stations_per_city.png",
    "pollution_hotspots_clusters.png",
    "missing_values_heatmap.png"
]

def collect_existing_images():
    found = []
    for im in images:
        path = os.path.join(VISUALS, im)
        if os.path.exists(path):
            found.append(path)
    # include any PNGs in visuals folder too
    for f in os.listdir(VISUALS):
        if f.endswith(".png") and os.path.join(VISUALS,f) not in found:
            found.append(os.path.join(VISUALS,f))
    return found

def make_pdf(out_pdf="air_quality_report.pdf"):
    img_paths = collect_existing_images()
    if not img_paths:
        print("No images found in visuals/. Run analysis scripts first.")
        return
    out_path = os.path.join(OUTPUT, out_pdf)
    print("Creating PDF:", out_path)
    with PdfPages(out_path) as pdf:
        for p in img_paths:
            try:
                img = Image.open(p)
                # convert RGBA to RGB
                if img.mode == "RGBA":
                    img = img.convert("RGB")
                # add figure to pdf
                fig = plt.figure(figsize=(8.27, 11.69))  # A4 portrait
                plt.axis("off")
                plt.imshow(img)
                plt.tight_layout()
                pdf.savefig(fig, bbox_inches='tight')
                plt.close(fig)
            except Exception as e:
                print("Skipping:", p, "due to", e)
    print("Saved PDF:", out_path)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    make_pdf()
