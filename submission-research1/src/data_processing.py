import pandas as pd


def load_data(filepath):
    """Load data from a CSV file."""
    return pd.read_csv(filepath)


def clean_data(df):
    """Perform basic data cleaning."""
    df = df.dropna()  # Remove missing values
    df = df[df['value'] > 0]  # Remove invalid entries
    return df
