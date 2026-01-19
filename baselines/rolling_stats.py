# baselines/rolling_stats.py

import statistics


def _mad(values, median):
    deviations = [abs(v - median) for v in values]
    return statistics.median(deviations)


def _extract_values(windows):
    """
    Extract values from:
    - TimeWindow
    - list[TimeWindow]
    """
    values = []

    if isinstance(windows, list):
        for w in windows:
            values.extend([s["value"] for s in w.samples])
    else:
        values = [s["value"] for s in windows.samples]

    return values


def compute_rolling_stats(windows):
    values = _extract_values(windows)

    if not values:
        return None

    median = statistics.median(values)
    mad = _mad(values, median)

    return {
        "count": len(values),
        "mean": statistics.mean(values),
        "median": median,
        "stdev": statistics.stdev(values) if len(values) > 1 else 0.0,
        "mad": mad,
        "min": min(values),
        "max": max(values),
        "p90": statistics.quantiles(values, n=10)[8] if len(values) >= 10 else max(values),
        "p95": statistics.quantiles(values, n=20)[18] if len(values) >= 20 else max(values),
    }





















"""
import statistics

def _mad(values, median):
    
    # Median Absolute Deviation (robust spread).
    
    deviations = [abs(v - median) for v in values]
    return statistics.median(deviations)


def compute_rolling_stats(window):
    
    # Computes robust baseline statistics for a window.
    
    values = list(window.values())

    if not values:
        return None

    median = statistics.median(values)
    mad = _mad(values, median)

    stats = {
        "count": len(values),

        # Central tendency
        "mean": statistics.mean(values),
        "median": median,

        # Spread
        "stdev": statistics.stdev(values) if len(values) > 1 else 0.0,
        "mad": mad,

        # Bounds
        "min": min(values),
        "max": max(values),

        # Quantiles (robust for observability)
        "p90": statistics.quantiles(values, n=10)[8] if len(values) >= 10 else max(values),
        "p95": statistics.quantiles(values, n=20)[18] if len(values) >= 20 else max(values),
    }

    return stats


"""






"""
import statistics

def compute_rolling_stats(window):
    
    # Computes baseline statistics for a window.
    
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
"""