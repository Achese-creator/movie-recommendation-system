"""Content-based recommendation utilities."""

import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def normalize_text(series: pd.Series) -> pd.Series:
    """Fill missing text values and convert text to lowercase."""
    return series.fillna("").str.lower()


def build_tfidf_matrix(
    text_series: pd.Series,
    max_features: int = 5000,
    stop_words: str = "english",
) -> tuple[TfidfVectorizer, csr_matrix]:
    """Build a TF-IDF vectorizer and matrix from a text series."""
    vectorizer = TfidfVectorizer(
        max_features=max_features,
        stop_words=stop_words,
    )
    matrix = vectorizer.fit_transform(text_series)
    return vectorizer, matrix
     
     
def compute_similarity_matrix(feature_matrix: csr_matrix) -> np.ndarray:
    """Compute pairwise cosine similarity for a feature matrix."""
    return cosine_similarity(feature_matrix)     