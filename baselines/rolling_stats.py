# baselines/rolling_stats.py

import statistics

def compute_rolling_stats(window):
    """
    Computes baseline statistics for a window.
    """
    values = window.values()

    if len(values) == 0:
        return None

    return {
        "count": len(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "stdev": statistics.stdev(values) if len(values) > 1 else 0.0,
        "min": min(values),
        "max": max(values)
    }
