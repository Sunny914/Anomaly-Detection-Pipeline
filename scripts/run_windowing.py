# scripts/run_windowing.py

from windows.window_config import WINDOW_DEFINITIONS
from windows.window_builder import group_by_series, build_windows
from scripts.run_normalization import run_normalization

def run_windowing():
    normalized_samples = run_normalization()
    series_map = group_by_series(normalized_samples)

    windowed_series = {}

    for series_key, samples in series_map.items():
        windowed_series[series_key] = {}

        print("\nSeries:", series_key)

        for window_name, cfg in WINDOW_DEFINITIONS.items():
            windows = build_windows(
                samples,
                cfg["duration_sec"],
                cfg["slide_sec"]
            )

            windowed_series[series_key][window_name] = windows

            print(
                f"  {window_name} windows:",
                len(windows)
            )

    return windowed_series   # 🔥 THIS IS THE FIX

if __name__ == "__main__":
    run_windowing()






"""
from windows.window_config import WINDOW_DEFINITIONS
from windows.window_builder import group_by_series, build_windows
from scripts.run_normalization import run_normalization

def run_windowing():
    normalized_samples = run_normalization()

    series_map = group_by_series(normalized_samples)

    for series_key, samples in series_map.items():
        print("\nSeries:", series_key)

        for window_name, cfg in WINDOW_DEFINITIONS.items():
            windows = build_windows(
                samples,
                cfg["duration_sec"],
                cfg["slide_sec"]
            )

            print(
                f"  {window_name} windows:",
                len(windows)
            )

if __name__ == "__main__":
    run_windowing()
"""