"""Stage 01: extract HTML from the configured source and save it to disk."""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from pathlib import Path

from datafun_toolkit.logger import log_path
import requests

# ============================================================
# Section 2. Define Run Extract Function
# ============================================================


def run_extract(
    source_url: str,
    http_request_headers: dict,
    raw_html_path: Path,
    LOG: logging.Logger,
) -> str:
    """Extract HTML data from the web page and save it to a file.

    Args:
        source_url (str): The URL of the web page.
        http_request_headers (dict[str, str]): The HTTP request headers.
        raw_html_path (Path): The path to save the raw HTML file.
        LOG (logging.Logger): The logger instance.

    Returns:
        str: The extracted HTML content as a string.

    Raises:
        requests.HTTPError: If the HTTP request to the web page fails.
        requests.RequestException: For other types of request exceptions.
        ValueError: If the response content cannot be parsed as HTML.
    """
    LOG.info("========================")
    LOG.info("STAGE 01: EXTRACT starting... ")
    LOG.info("========================")

    LOG.info(f"EXTRACT: Fetching HTML from {source_url}")
    response = requests.get(source_url, headers=http_request_headers, timeout=30)
    response.raise_for_status()

    html_content: str = response.text
    raw_html_path.write_text(html_content, encoding="utf-8")

    LOG.info(f"SOURCE URL = {source_url}")
    log_path(LOG, "SINK PATH", raw_html_path)
    return html_content
