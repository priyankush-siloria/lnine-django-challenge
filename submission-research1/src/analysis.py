import numpy as np
from sklearn.linear_model import LinearRegression


def compute_statistics(df):
    """Calculate basic statistics of the data."""
    return {
        "mean": np.mean(df['value']),
        "std": np.std(df['value']),
        "median": np.median(df['value'])
    }


def train_model(X, y):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X, y)
    return model
