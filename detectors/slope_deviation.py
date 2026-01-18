# detectors/slope_deviation.py

# detectors/slope_deviation.py

from baselines.slope_models import compute_slope

def detect_slope_deviation(
    series_key,
    window_type,
    window,
    baseline_slope,
    tolerance=0.005
):
    """
    Detects anomaly based on absolute slope change.
    """

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