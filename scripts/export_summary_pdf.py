from PIL import Image, ImageDraw, ImageFont
import textwrap
from pathlib import Path

INPUT = Path(__file__).resolve().parents[1] / "output" / "summary_report.md"
OUTPUT = Path(__file__).resolve().parents[1] / "output" / "summary_report.pdf"

# Page settings
DPI = 150
INCHES_W, INCHES_H = 8.27, 11.69  # A4
WIDTH = int(INCHES_W * DPI)
HEIGHT = int(INCHES_H * DPI)
MARGIN = 80
LINE_SPACING = 6

from PIL import ImageFont
try:
    FONT = ImageFont.load_default()
except Exception:
    FONT = None

if not INPUT.exists():
    print(f"Input file not found: {INPUT}")
    raise SystemExit(1)

with open(INPUT, 'r', encoding='utf-8') as f:
    text = f.read()

lines = []
# wrap to width in characters estimate
# estimate max chars per line
if FONT:
    # use a sample bbox to estimate character width and line height
    bbox = FONT.getmask("A").getbbox()
    if bbox:
        char_width = bbox[2] - bbox[0]
    else:
        char_width = 7
else:
    char_width = 7
max_chars = (WIDTH - 2*MARGIN) // (char_width if char_width>0 else 7)
for paragraph in text.split('\n'):
    if paragraph.strip() == "":
        lines.append("")
    else:
        wrapped = textwrap.wrap(paragraph, width=max_chars)
        if not wrapped:
            lines.append("")
        else:
            lines.extend(wrapped)

pages = []
current_lines = []
# measure line height
if FONT:
    # estimate line height
    line_height = FONT.getmask("A").getbbox()[3] + LINE_SPACING if FONT.getmask("A").getbbox() else 12
else:
    line_height = 12
max_lines_per_page = (HEIGHT - 2*MARGIN) // line_height

for i, l in enumerate(lines):
    current_lines.append(l)
    if len(current_lines) >= max_lines_per_page:
        pages.append(current_lines)
        current_lines = []
if current_lines:
    pages.append(current_lines)

images = []
for page_lines in pages:
    img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
    draw = ImageDraw.Draw(img)
    y = MARGIN
    for pline in page_lines:
        draw.text((MARGIN, y), pline, fill='black', font=FONT)
        y += line_height
    images.append(img)

# Save as multipage PDF
if images:
    images[0].save(OUTPUT, save_all=True, append_images=images[1:])
    print(f"Saved PDF: {OUTPUT}")
else:
    print("No content to save.")
