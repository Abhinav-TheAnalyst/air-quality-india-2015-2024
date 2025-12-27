import pandas as pd
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================================
# 1. Project paths (IMPORTANT PART)
# =====================================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

INPUT_FILE = RAW_DIR / "city_day.csv"
OUTPUT_FILE = PROCESSED_DIR / "city_day_cleaned.csv"

try:
    # Verify input file exists
    if not INPUT_FILE.exists():
        logger.error(f"Input file not found: {INPUT_FILE}")
        logger.info(f"Files in {RAW_DIR}:")
        if RAW_DIR.exists():
            for f in RAW_DIR.glob("*.csv"):
                logger.info(f"  - {f.name}")
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")
    
    # =====================================
    # 2. Load data
    # =====================================
    df = pd.read_csv(INPUT_FILE)
    logger.info(f"Loaded {len(df)} rows")

    # ...existing code...

    # =====================================
    # 9. Save cleaned data
    # =====================================
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    logger.info(f"✅ Cleaned data saved to: {OUTPUT_FILE}")

except FileNotFoundError as e:
    logger.error(f"❌ File error: {e}")
except Exception as e:
    logger.error(f"❌ Error: {e}", exc_info=True)