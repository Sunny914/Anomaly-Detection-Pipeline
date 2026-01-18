# detectors/detector_utils.py

def relative_deviation(current, baseline):
    if baseline == 0:
        return float("inf") if current != 0 else 0.0
    return (current - baseline) / baseline






"""
def relative_deviation(current, baseline):
    
    # Computes relative deviation ratio.
    
    if baseline == 0:
        return 0.0
    return (current - baseline) / baseline
"""




"""
def z_score(value, mean, stdev):
    if stdev == 0:
        return 0.0
    return (value - mean) / stdev
"""