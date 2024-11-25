import matplotlib.pyplot as plt


def plot_data(df, x_col, y_col):
    """Scatter plot of two columns."""
    plt.scatter(df[x_col], df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{x_col} vs {y_col}")
    plt.show()
