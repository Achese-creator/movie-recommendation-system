"""Content-based recommendation utilities."""

import pandas as pd


def normalize_text(series: pd.Series) -> pd.Series:
    """Fill missing text values and convert text to lowercase."""
    return series.fillna("").str.lower()