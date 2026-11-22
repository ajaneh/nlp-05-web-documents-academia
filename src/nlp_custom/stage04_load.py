"""Stage 04: load the transformed DataFrame to CSV."""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from pathlib import Path

from datafun_toolkit.logger import log_path
import pandas as pd

# ============================================================
# Section 2. Define Run Load Function
# ============================================================


def run_load(
    df: pd.DataFrame,
    processed_csv_path: Path,
    LOG: logging.Logger,
) -> None:
    """Write DataFrame to CSV sink.

    Args:
        df (pd.DataFrame): The DataFrame to write.
        processed_csv_path (Path): The path to save the processed CSV file.
        LOG (logging.Logger): The logger instance.

    Returns:
        None (just writes to the sink)
    """
    LOG.info("========================")
    LOG.info("STAGE 04: LOAD starting...")
    LOG.info("========================")

    df.to_csv(processed_csv_path, index=False)
    log_path(LOG, "SINK PATH", processed_csv_path)
