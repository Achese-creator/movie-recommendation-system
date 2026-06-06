# Data Sources

This project uses two main data sources: MovieLens and TMDB.

## MovieLens 25M Dataset

MovieLens 25M is used for user ratings and collaborative filtering.

Download page:

https://grouplens.org/datasets/movielens/25m/

Expected raw files include:

- ratings.csv
- movies.csv
- tags.csv
- links.csv
- genome-scores.csv
- genome-tags.csv

Place the extracted files in:

data/raw/movielens/

MovieLens will support:

- Ratings analysis
- User-item interaction modeling
- Collaborative filtering
- Matrix factorization
- Personalized recommendations

## TMDB Metadata Dataset

TMDB metadata is used for richer movie content information.

Possible sources include Kaggle TMDB metadata datasets and the official TMDB API.

Expected metadata may include:

- Movie title
- Overview
- Genres
- Keywords
- Cast
- Crew
- Poster path
- Release date

Place downloaded metadata files in:

data/raw/tmdb/

TMDB metadata will support:

- Content-based recommendations
- Text feature engineering
- NLP-based similarity
- Poster display in the Streamlit app
- Metadata enrichment through the TMDB API

## Data Versioning Note

Raw datasets should not be committed to Git.

The project stores raw data locally in data/raw/ and processed data locally in data/processed/.

These folders are ignored by Git because the files may be large and can be downloaded or regenerated.