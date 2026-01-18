# baselines/slope_models.py

# baselines/slope_models.py

import statistics

def compute_slope(window):
    """
    Computes time-normalized slope (trend) of values over time.
    Slope unit: value change per second.
    """

    samples = list(window.samples)

    if len(samples) < 2:
        return 0.0

    # Use real timestamps (seconds)
    times = [s["timestamp"] for s in samples]
    values = [s["value"] for s in samples]

    # Normalize time axis to start at 0
    t0 = times[0]
    x = [t - t0 for t in times]
    y = values

    x_mean = statistics.mean(x)
    y_mean = statistics.mean(y)

    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    denominator = sum((xi - x_mean) ** 2 for xi in x)

    if denominator == 0:
        return 0.0

    raw_slope = numerator / denominator  # units per second

    # --- Light smoothing (robustness) ---
    # Clamp extreme spikes caused by jitter
    if abs(raw_slope) > 1e6:
        return 0.0

    return raw_slope











"""
def compute_slope(window):
    
   # Computes slope (trend) of values over time.
    
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


"""