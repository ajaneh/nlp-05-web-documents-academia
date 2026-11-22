"""src/nlp_custom/config.py - Module Configuration.

(MODIFY YOUR VERSION OF THIS FILE)
Alex Heyert November 2026.

Stores configuration values for the web document EVTL pipeline.
Source: TODO: arXiv abstract page for "Modern Earth-like Chemical Disequilibrium Biosignatures Are Challenging To Constrain Through Spectroscopic Retrievals" (2505.16231)

Purpose

  Store configuration values.

Analytical Questions

- What web page URL should be used as the data source?
- Where should raw and processed data be stored?

Edit your Python file to change:
- PAGE_URL (source of the HTML web page document),
- customize your output file name.
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

# New ArXiv abstract page
PAGE_URL: str = "https://arxiv.org/abs/2505.16231"
# arXiv abstract page - stable, scraping-friendly, academically relevant

# Let them know who we are (and that we're doing educational web mining).
HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"


# changed URLs for phase 4
RAW_HTML_PATH: Path = RAW_PATH / "phase4_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "phase4_processed.csv"
