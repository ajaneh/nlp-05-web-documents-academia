"""Stage 03: transform validated HTML into a structured DataFrame."""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
import re

from bs4 import BeautifulSoup, Tag
import pandas as pd

# ============================================================
# Section 2. Define Run Transform Function
# ============================================================


def run_transform(
    soup: BeautifulSoup,
    LOG: logging.Logger,
) -> pd.DataFrame:
    """Transform HTML into a structured DataFrame.

    Args:
        soup (BeautifulSoup): Validated BeautifulSoup object.
        LOG (logging.Logger): The logger instance.

    Returns:
        pd.DataFrame: The transformed dataset.
    """
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    LOG.info("Extracting metadata from HTML")
    LOG.info("========================")
    LOG.info("STAGE 03a: Extract bibliographic fields (title, authors, abstract)")
    LOG.info("========================")

    title_tag: Tag | None = soup.find("h1", class_="title")
    authors_tag: Tag | None = soup.find("div", class_="authors")
    abstract_tag: Tag | None = soup.find("blockquote", class_="abstract")
    doi_td = soup.find("td", class_="doi")

    # Read the journal DOI from arXiv's DOI metadata cell when present; leave blank if not listed.
    link_tag = doi_td.find("a") if doi_td else None
    if link_tag:
        journal_doi_url = str(link_tag.get("href", "")).strip()
        journal_doi = str(link_tag.get("data-doi", "")).strip()
        LOG.info(f"Found journal DOI URL: {journal_doi_url or '(blank)'}")
    else:
        journal_doi_url = ""
        journal_doi = ""

    title: str = (
        title_tag.get_text(strip=True).replace("Title:", "").strip()
        if title_tag
        else "unknown"
    )

    author_tags_list: list[Tag] = authors_tag.find_all("a") if authors_tag else []
    number_of_authors: int = len(author_tags_list)
    LOG.info(f"Found {number_of_authors} author tags in the authors <div>")
    authors: str = (
        ", ".join([tag.get_text(strip=True) for tag in author_tags_list])
        .replace("Authors:", "")
        .strip()
        if authors_tag
        else "unknown"
    )

    abstract: str = (
        abstract_tag.get_text(strip=True).replace("Abstract:", "").strip()
        if abstract_tag
        else "unknown"
    )

    LOG.info(f"Extracted title: {title}")
    LOG.info(f"Extracted authors: {authors}")
    LOG.info(f"Extracted abstract: {abstract[:100]}...")

    LOG.info("========================")
    LOG.info("STAGE 03b: Extract metadata field subjects from subheader")
    LOG.info("========================")
    subheader: Tag | None = soup.find("div", class_="subheader")
    subjects: str = subheader.get_text(strip=True) if subheader else "unknown"
    LOG.info(f"Extracted subjects: {subjects}")

    LOG.info("========================")
    LOG.info("STAGE 03c: Extract metadata field date from dateline")
    LOG.info("========================")
    dateline: Tag | None = soup.find("div", class_="dateline")
    date_submitted_str: str = dateline.get_text(strip=True) if dateline else "unknown"
    LOG.info(f"Extracted submitted: {date_submitted_str}")

    LOG.info("========================")
    LOG.info("STAGE 03d: Extract metadata field arxiv_id from canonical link")
    LOG.info("========================")
    canonical: Tag | None = soup.find("link", rel="canonical")
    if canonical is None:
        LOG.warning("Canonical link not found, setting arXiv ID to 'unknown'")
        arxiv_id: str = "unknown"
    else:
        href: str = str(canonical["href"])
        arxiv_id = href.split("/abs/")[-1]
    LOG.info(f"Extracted arxiv_id: {arxiv_id}")

    LOG.info("========================")
    LOG.info("STAGE 03e: Calculate derived fields")
    LOG.info("========================")

    abstract_word_count: int = len(abstract.split()) if abstract != "unknown" else 0
    LOG.info(f"Calculated abstract word count: {abstract_word_count}")

    author_count: int = (
        len([a.strip() for a in authors.split(",")]) if authors != "unknown" else 0
    )
    LOG.info(f"Calculated author count: {author_count}")

    chemical_disequilibrium_count: int = (
        len(re.findall(r"chemical disequilibrium", abstract, flags=re.IGNORECASE))
        if abstract != "unknown"
        else 0
    )
    LOG.info(
        "Calculated chemical_disequilibrium_count: %s",
        chemical_disequilibrium_count,
    )

    LOG.info("========================")
    LOG.info("STAGE 03f: Build record and create DataFrame")
    LOG.info("========================")

    record = {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "subjects": subjects,
        "submitted": date_submitted_str,
        "abstract": abstract,
        "abstract_word_count": abstract_word_count,
        "author_count": author_count,
        "chemical_disequilibrium_count": chemical_disequilibrium_count,
        "journal_doi_url": journal_doi_url,
        "journal_doi": journal_doi,
    }

    df = pd.DataFrame([record])
    LOG.info(f"Created DataFrame with {len(df)} row and {len(df.columns)} columns")
    LOG.info(f"Columns: {list(df.columns)}")

    LOG.info("DataFrame Details")
    LOG.info(f"  Title: {title}")
    LOG.info(f"  Author count: {record['author_count']}")
    LOG.info(f"  Abstract word count: {record['abstract_word_count']}")
    LOG.info(f"  DataFrame preview:\n{df.head()}")

    LOG.info("Sink: Pandas DataFrame created")
    LOG.info("Transformation complete.")
    return df
