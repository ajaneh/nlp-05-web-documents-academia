"""Configuration values for the web document EVTL pipeline.

Source: arXiv abstract page for "Modern Earth-like Chemical Disequilibrium
Biosignatures Are Challenging To Constrain Through Spectroscopic Retrievals"
(2505.16231).
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

PAGE_URL: str = "https://arxiv.org/abs/2505.16231"
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

RAW_HTML_PATH: Path = RAW_PATH / "AH_GL_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "AH_GL_processed.csv"
