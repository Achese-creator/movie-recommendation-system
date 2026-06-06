# Data Directory

This folder stores local project datasets.

The actual dataset files are not committed to Git because they may be large and can be downloaded or regenerated.

## Expected Structure

data/
  raw/
    movielens/
      ratings.csv
      movies.csv
      links.csv
      tags.csv
    tmdb/
      movies_metadata.csv
      credits.csv
      keywords.csv
  processed/

## Raw Data

The raw data folder stores original downloaded files.

Do not edit raw data files directly.

MovieLens raw files should be placed in:

data/raw/movielens/

TMDB raw files should be placed in:

data/raw/tmdb/

## Processed Data

The processed data folder will store cleaned, transformed, or merged files created by project scripts.

Processed files are also ignored by Git because they can be regenerated.

## Notes

See docs/data_sources.md for download links and dataset usage explanations.