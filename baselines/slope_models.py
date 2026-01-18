# baselines/slope_models.py

def compute_slope(window):
    """
    Computes slope (trend) of values over time.
    """
    values = window.values()

    if len(values) < 2:
        return 0.0

    x = list(range(len(values)))
    y = values

    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    denominator = sum((xi - x_mean) ** 2 for xi in x)

    if denominator == 0:
        return 0.0

    return numerator / denominator
