# detectors/slope_deviation.py

from baselines.slope_models import compute_slope


def _severity_from_slope(diff, tolerance):
    """
    Maps slope deviation magnitude to severity.
    """
    ratio = diff / tolerance if tolerance > 0 else diff

    if ratio >= 3.0:
        return "high"
    elif ratio >= 1.5:
        return "medium"
    else:
        return "low"


def _confidence_from_slope(diff, tolerance):
    """
    Confidence based on how strongly slope exceeds tolerance.
    """
    if tolerance <= 0:
        return 0.5
    return min(1.0, diff / (tolerance * 3))


def detect_slope_deviation(
    series_key,
    window_type,
    window,
    baseline_slope,
    tolerance=0.005
):
    """
    Detects anomaly based on slope (trend) deviation.
    """

    current_slope = compute_slope(window)
    slope_diff = current_slope - baseline_slope

    if abs(slope_diff) < tolerance:
        return None

    direction = "increasing" if slope_diff > 0 else "decreasing"
    abs_diff = abs(slope_diff)

    severity = _severity_from_slope(abs_diff, tolerance)
    confidence = _confidence_from_slope(abs_diff, tolerance)

    return {
        "series": str(series_key),
        "window_type": window_type,
        "timestamp": window.center_ts,   # ✅ ADD THIS
        "detector": "slope_deviation",

        # Slopes
        "current_slope": current_slope,
        "baseline_slope": baseline_slope,
        "slope_diff": slope_diff,
        "direction": direction,

        # Scoring
        "severity": severity,
        "confidence": round(confidence, 2)
    }












"""
from baselines.slope_models import compute_slope

def detect_slope_deviation(
    series_key,
    window_type,
    window,
    baseline_slope,
    tolerance=0.005
):
    
    # Detects anomaly based on absolute slope change.
    
    current_slope = compute_slope(window)
    slope_diff = abs(current_slope - baseline_slope)

    if slope_diff >= tolerance:
        return {
            "series": str(series_key),
            "window_type": window_type,
            "current_slope": current_slope,
            "baseline_slope": baseline_slope,
            "slope_diff": slope_diff,
            "detector": "slope_deviation"
        }

    return None
"""








"""
from baselines.slope_models import compute_slope

def detect_slope_deviation(
    series_key,
    window_type,
    window,
    baseline_slope,
    #tolerence=2.0
    tolerence=0.005

):
    
    #Detects anomaly based on slope deviation.
    
    current_slope = compute_slope(window)

    # Avoid division by zero / meaningless baseline
    if baseline_slope == 0:
        return None

    # deviation_ratio = current_slope / baseline_slope
    slope_diff = abs(current_slope - baseline_slope)

    if abs(slope_diff) >= tolerence:
        return {
            "series": str(series_key),
            "window_type": window_type,
            "current_slope": current_slope,
            "baseline_slope": baseline_slope,
            "deviation_ratio": slope_diff,
            "detector": "slope_deviation"
        }

    return None

"""




"""
def detect_slope_deviation(current_slope, baseline_slope, tolerance=2.0):

    # Detects abnormal slope change.

    deviation = current_slope - baseline_slope

    return {
        "detector": "slope_deviation",
        "slope_diff": deviation,
        "anomalous": abs(deviation) >= tolerance
    }
"""