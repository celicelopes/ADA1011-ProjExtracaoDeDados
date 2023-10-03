import pandas as pd
from pandas import json_normalize

def count_articles_by_date(parquet_file):
    # Read the Parquet file into a DataFrame
    df = pd.read_parquet(parquet_file)

    # Normalize the 'articles' column to extract nested information
    articles_df = json_normalize(df['articles'])

    # Combine the normalized data with the original DataFrame
    df = pd.concat([df, articles_df], axis=1)

    # Convert the 'publishedAt' column to datetime format
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])

    # Extract year, month, and day from the 'publishedAt' column
    df['year'] = df['publishedAt'].dt.year
    df['month'] = df['publishedAt'].dt.month
    df['day'] = df['publishedAt'].dt.day

    # Count the number of articles for each year, month, and day
    count_by_year = df['year'].value_counts().sort_index()
    count_by_month = df.groupby(['year', 'month']).size().unstack().fillna(0)
    count_by_day = df.groupby(['year', 'month', 'day']).size().unstack().fillna(0)

    return count_by_year, count_by_month, count_by_day
