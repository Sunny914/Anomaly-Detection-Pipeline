# windows/window_builder.py

from collections import defaultdict
from windows.window_types import TimeWindow

MIN_SAMPLES_PER_WINDOW = 3   # critical for slope & stats


def group_by_series(samples):
    """
    Groups samples by (metric + labels).
    """
    series = defaultdict(list)

    for s in samples:
        key = (
            s["metric"],
            tuple(sorted(s["labels"].items()))
        )
        series[key].append(s)

    # Ensure time ordering
    for key in series:
        series[key].sort(key=lambda x: x["timestamp"])

    return series


def build_windows(samples, window_size, slide_size):
    """
    Builds sliding windows for one time series using time-based sliding.
    """

    windows = []

    if not samples:
        return windows

    series_start_ts = samples[0]["timestamp"]
    series_end_ts = samples[-1]["timestamp"]

    start_ts = series_start_ts

    while start_ts + window_size <= series_end_ts:
        end_ts = start_ts + window_size

        # Collect samples inside this time window
        window_samples = [
            s for s in samples
            if start_ts <= s["timestamp"] < end_ts
        ]

        if len(window_samples) >= MIN_SAMPLES_PER_WINDOW:
            windows.append(
                TimeWindow(
                    start_ts=start_ts,
                    end_ts=end_ts,
                    samples=window_samples
                )
            )

        # Slide forward in TIME (not index)
        start_ts += slide_size

    return windows



















"""
# windows/window_builder.py

from collections import defaultdict
from windows.window_types import TimeWindow


MIN_SAMPLES_PER_WINDOW = 3   # critical for slope & stats


def group_by_series(samples):
    
    # Groups samples by (metric + labels).
    
    series = defaultdict(list)

    for s in samples:
        key = (
            s["metric"],
            tuple(sorted(s["labels"].items()))
        )
        series[key].append(s)

    # Ensure time ordering
    for key in series:
        series[key].sort(key=lambda x: x["timestamp"])

    return series


def build_windows(samples, window_size, slide_size):

    #Builds sliding windows for one time series using time-based sliding.
    

    windows = []

    if not samples:
        return windows

    start_ts = samples[0]["timestamp"]
    end_of_series = samples[-1]["timestamp"]

    idx = 0

    while start_ts + window_size <= end_of_series:
        end_ts = start_ts + window_size

        window_samples = []

        # collect samples inside window
        while idx < len(samples) and samples[idx]["timestamp"] < end_ts:
            if samples[idx]["timestamp"] >= start_ts:
                window_samples.append(samples[idx])
            idx += 1

        if len(window_samples) >= MIN_SAMPLES_PER_WINDOW:
            windows.append(
                TimeWindow(start_ts, end_ts, window_samples)
            )

        # slide window forward in TIME, not index
        start_ts += slide_size
        idx = 0  # reset index for next window scan

    return windows
"""








"""
from collections import defaultdict
from windows.window_types import TimeWindow

def group_by_series(samples):
    
    # Groups samples by (metric + labels).
    
    series = defaultdict(list)

    for s in samples:
        key = (
            s["metric"],
            tuple(sorted(s["labels"].items()))
        )
        series[key].append(s)

    # Ensure time ordering
    for key in series:
        series[key].sort(key=lambda x: x["timestamp"])

    return series


def build_windows(samples, window_size, slide_size):
    
    #Builds sliding windows for one time series.
    
    windows = []
    start_idx = 0

    while start_idx < len(samples):
        start_ts = samples[start_idx]["timestamp"]
        end_ts = start_ts + window_size

        window_samples = [
            s for s in samples
            if start_ts <= s["timestamp"] < end_ts
        ]

        if window_samples:
            windows.append(
                TimeWindow(start_ts, end_ts, window_samples)
            )

        # advance window
        start_idx += 1

    return windows


"""