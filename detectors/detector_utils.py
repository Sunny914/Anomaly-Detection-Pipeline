# detectors/detector_utils.py

# detectors/detector_utils.py

MAX_RELATIVE_DEVIATION = 10.0  # safety cap for downstream logic


def relative_deviation(current, baseline, epsilon=1e-6):
    """
    Computes relative deviation in a bounded, numerically stable way.

    - Prevents division by zero
    - Avoids infinite values
    - Keeps deviations comparable across detectors
    """

    if abs(baseline) < epsilon:
        # Treat near-zero baseline as large but bounded deviation
        if abs(current) < epsilon:
            return 0.0
        return MAX_RELATIVE_DEVIATION

    return (current - baseline) / baseline









"""
def relative_deviation(current, baseline):
    if baseline == 0:
        return float("inf") if current != 0 else 0.0
    return (current - baseline) / baseline

"""




"""
def z_score(value, mean, stdev):
    if stdev == 0:
        return 0.0
    return (value - mean) / stdev
"""