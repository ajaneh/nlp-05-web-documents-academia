"""Orchestrate the web document EVTL pipeline.

Run from the project root with:

  uv run python -m nlp_custom.pipeline_web_html
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging

from datafun_toolkit.logger import get_logger, log_header, log_path
from wordcloud import WordCloud

from nlp_custom.config import (
    DATA_PATH,
    HTTP_REQUEST_HEADERS,
    PAGE_URL,
    PROCESSED_CSV_PATH,
    PROCESSED_PATH,
    RAW_HTML_PATH,
    RAW_PATH,
    ROOT_PATH,
)
from nlp_custom.stage01_extract import run_extract
from nlp_custom.stage02_validate import run_validate
from nlp_custom.stage03_transform import run_transform
from nlp_custom.stage04_load import run_load

# ============================================================
# Section 2. Configure Logging
# ============================================================

LOG: logging.Logger = get_logger("CI", level="DEBUG")


# ============================================================
# Section 3. Define Main Pipeline Function
# ============================================================


def main() -> None:
    """Main function."""
    log_header(LOG, "Module 5: EVTL PIPELINE - WEB DOCUMENTS (HTML)")
    LOG.info("START PIPELINE")

    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DATA_PATH", DATA_PATH)
    log_path(LOG, "RAW_PATH", RAW_PATH)
    log_path(LOG, "PROCESSED_PATH", PROCESSED_PATH)

    # EXTRACT
    html_content = run_extract(
        source_url=PAGE_URL,
        http_request_headers=HTTP_REQUEST_HEADERS,
        raw_html_path=RAW_HTML_PATH,
        LOG=LOG,
    )

    # VALIDATE
    validated_soup = run_validate(
        html_content=html_content,
        LOG=LOG,
    )

    # TRANSFORM
    df = run_transform(
        soup=validated_soup,
        LOG=LOG,
    )

    # LOAD
    run_load(
        df=df,
        processed_csv_path=PROCESSED_CSV_PATH,
        LOG=LOG,
    )

    # Save to docs/assets so the same image can be embedded in README and docs.
    wordcloud_path = ROOT_PATH / "docs" / "assets" / "abstract_wordcloud.png"
    wordcloud_path.parent.mkdir(parents=True, exist_ok=True)
    abstract_text = str(df.loc[0, "abstract"]) if not df.empty else ""
    wordcloud = WordCloud(width=1200, height=600, background_color="white").generate(
        abstract_text or "abstract"
    )
    wordcloud.to_file(str(wordcloud_path))
    log_path(LOG, "WORDCLOUD PATH", wordcloud_path)

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")


# ============================================================
# Section 4. Run Main Function when This File is Executed
# ============================================================

if __name__ == "__main__":
    main()
