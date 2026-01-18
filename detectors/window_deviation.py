# detectors/window_deviation.py


from detectors.detector_utils import relative_deviation

def detect_window_deviation(
    series_key,
    window_type,
    window,
    baseline_stats,
    relative_threshold=0.5,
    absolute_threshold=0.02
):
    """
    Detects anomaly based on window mean deviation.
    Uses both relative and absolute thresholds.
    """

    values = list(window.values())
    if not values:
        return None

    current_mean = sum(values) / len(values)
    baseline_mean = baseline_stats["mean"]

    deviation = relative_deviation(current_mean, baseline_mean)
    absolute_diff = abs(current_mean - baseline_mean)

    if (
        abs(deviation) >= relative_threshold
        or absolute_diff >= absolute_threshold
    ):
        return {
            "series": str(series_key),
            "window_type": window_type,
            "current_mean": current_mean,
            "baseline_mean": baseline_mean,
            "relative_deviation": deviation,
            "absolute_diff": absolute_diff,
            "detector": "window_mean_deviation"
        }

    return None












"""
from detectors.detector_utils import relative_deviation

def detect_window_deviation(series_key, window_type, window, baseline_stats, threshold=0.5):
    
    # Detects anomaly based on window mean deviation from baseline mean.
    
    current_mean = sum(window.values()) / len(window.values())
    baseline_mean = baseline_stats["mean"]

    deviation = relative_deviation(current_mean, baseline_mean)

    if abs(deviation) >= threshold:
        return {
            "series": str(series_key),
            "window_type": window_type,
            "current_mean": current_mean,
            "baseline_mean": baseline_mean,
            "deviation": deviation,
            "detector": "window_mean_deviation"
        }

    return None
"""




"""
from detectors.detector_utils import z_score

def detect_window_deviation(window, baseline_stats, threshold=3.0):

    # Detects deviation of window mean from baseline mean.
    
    window_mean = sum(window.values()) / len(window.values())

    z = z_score(
        window_mean,
        baseline_stats["mean"],
        baseline_stats["stdev"]
    )

    return {
        "detector": "window_deviation",
        "z_score": z,
        "anomalous": abs(z) >= threshold
    }
"""