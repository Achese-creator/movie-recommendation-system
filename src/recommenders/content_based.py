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



def recommend_movies(
    title: str,
    movies_df: pd.DataFrame,
    similarity_matrix: np.ndarray,
    top_n: int = 10,
) -> pd.DataFrame:
    """Recommend movies similar to a given title."""
    normalized_title = title.lower()

    matching_movies = movies_df[
        movies_df["title"].str.lower() == normalized_title
    ]

    if matching_movies.empty:
        return pd.DataFrame()

    movie_index = matching_movies.index[0]
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    sorted_scores = sorted(
        similarity_scores,
        key=lambda item: item[1],
        reverse=True,
    )

    top_scores = sorted_scores[1 : top_n + 1]
    top_movie_indices = [item[0] for item in top_scores]

    recommendations = movies_df.iloc[top_movie_indices][
        ["id", "title", "vote_average", "vote_count", "release_date", "runtime"]
    ].copy()

    recommendations["similarity_score"] = [item[1] for item in top_scores]

    return recommendations