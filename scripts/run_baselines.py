# scripts/run_baselines.py


from scripts.run_windowing import run_windowing
from baselines.rolling_stats import compute_rolling_stats
from baselines.slope_models import compute_slope
from baselines.baseline_store import store_baseline

# Minimum windows required before trusting a baseline
MIN_WINDOWS_FOR_BASELINE = 2


def run_baselines(windowed_series=None):
    """
    Stage 4 — Baseline computation
    - Computes stable baselines from windows
    - Stores baselines in an append-only store
    """

    if windowed_series is None:
        windowed_series = run_windowing()

    for series_key, windows_by_type in windowed_series.items():
        for window_type, windows in windows_by_type.items():

            # Require sufficient history
            if len(windows) < MIN_WINDOWS_FOR_BASELINE:
                continue

            # Use all but the most recent window as baseline
            baseline_windows = windows[:-1]

            for window in baseline_windows:
                stats = compute_rolling_stats(window)
                if not stats:
                    continue

                slope = compute_slope(window)

                store_baseline(
                    series_key,
                    window_type,
                    stats,
                    slope
                )






"""
from scripts.run_windowing import run_windowing
from baselines.rolling_stats import compute_rolling_stats
from baselines.slope_models import compute_slope
from baselines.baseline_store import store_baseline

def run_baselines():
    windowed_series = run_windowing()

    for series_key, windows_by_type in windowed_series.items():
        for window_type, windows in windows_by_type.items():
            for window in windows:
                stats = compute_rolling_stats(window)
                slope = compute_slope(window)

                if stats:
                    store_baseline(
                        series_key,
                        window_type,
                        stats,
                        slope
                    )

if __name__ == "__main__":
    run_baselines()


"""    
