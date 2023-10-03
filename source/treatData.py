import pandas as pd
from pandas import json_normalize

def count_articles_by_date(parquet_file):
    df = pd.read_parquet(parquet_file)

    articles_df = json_normalize(df['articles'])

    df = pd.concat([df, articles_df], axis=1)

    df['publishedAt'] = pd.to_datetime(df['publishedAt'])

    df['year'] = df['publishedAt'].dt.year
    df['month'] = df['publishedAt'].dt.month
    df['day'] = df['publishedAt'].dt.day

    count_by_year = df['year'].value_counts().sort_index()
    count_by_month = df.groupby(['year', 'month']).size().unstack().fillna(0)
    count_by_day = df.groupby(['year', 'month', 'day']).size().unstack().fillna(0)

    return count_by_year, count_by_month, count_by_day

def count_articles_by_source_and_author(parquet_file):
    df = pd.read_parquet(parquet_file)

    articles_df = json_normalize(df['articles'])

    df = pd.concat([df, articles_df], axis=1)

    count_by_source_author = df.groupby(['source.name', 'author']).size().reset_index(name='article_count')

    return count_by_source_author

