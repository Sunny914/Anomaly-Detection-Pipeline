# windows/window_builder.py

from collections import defaultdict
from windows.window_types import TimeWindow

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
    Builds sliding windows for one time series.
    """
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
