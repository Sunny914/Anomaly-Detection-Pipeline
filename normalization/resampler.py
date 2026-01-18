# normalization/resampler.py

import math

def resample_timestamp(timestamp: float, interval: int = 15):
    """
    Aligns timestamps to fixed sampling intervals.
    """
    return math.floor(timestamp / interval) * interval
