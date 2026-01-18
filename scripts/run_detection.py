# scripts/run_detection.py

# scripts/run_detection.py

from scripts.run_windowing import run_windowing
from baselines.rolling_stats import compute_rolling_stats
from baselines.slope_models import compute_slope
from detectors.window_deviation import detect_window_deviation
from detectors.slope_deviation import detect_slope_deviation


def run_detection():
    windowed_series = run_windowing()
    anomalies = []

    for series_key, windows_by_type in windowed_series.items():
        for window_type, windows in windows_by_type.items():

            # Need at least 2 windows to compare past vs present
            if len(windows) < 2:
                continue

            for i in range(1, len(windows)):
                baseline_windows = windows[:i]
                current_window = windows[i]

                baseline_stats = compute_rolling_stats(baseline_windows)
                baseline_slope = compute_slope(baseline_windows)

                if not baseline_stats:
                    continue

                # Detector A — Mean deviation
                anomaly_a = detect_window_deviation(
                    series_key,
                    window_type,
                    current_window,
                    baseline_stats
                )

                if anomaly_a:
                    anomalies.append(anomaly_a)
                    print("ANOMALY (MEAN):", anomaly_a)

                # Detector B — Slope deviation
                anomaly_b = detect_slope_deviation(
                    series_key,
                    window_type,
                    current_window,
                    baseline_slope
                )

                if anomaly_b:
                    anomalies.append(anomaly_b)
                    print("ANOMALY (SLOPE):", anomaly_b)

    return anomalies


if __name__ == "__main__":
    run_detection()







"""
from scripts.run_windowing import run_windowing
from baselines.rolling_stats import compute_rolling_stats
from baselines.slope_models import compute_slope
from detectors.window_deviation import detect_window_deviation
from detectors.slope_deviation import detect_slope_deviation

def run_detection():
    windowed_series = run_windowing()
    anomalies = []

    for series_key, windows_by_type in windowed_series.items():
        for window_type, windows in windows_by_type.items():
            for window in windows:
                baseline_stats = compute_rolling_stats(window)
                baseline_slope = compute_slope(window)

                if not baseline_stats:
                    continue

                # Detector A — Mean deviation
                anomaly_a = detect_window_deviation(
                    series_key,
                    window_type,
                    window,
                    baseline_stats
                )

                if anomaly_a:
                    anomalies.append(anomaly_a)
                    print("ANOMALY (MEAN):", anomaly_a)

                # Detector B — Slope deviation
                anomaly_b = detect_slope_deviation(
                    series_key,
                    window_type,
                    window,
                    baseline_slope
                )

                if anomaly_b:
                    anomalies.append(anomaly_b)
                    print("ANOMALY (SLOPE):", anomaly_b)

    return anomalies

if __name__ == "__main__":
    run_detection()

"""






"""
from scripts.run_windowing import run_windowing
from baselines.rolling_stats import compute_rolling_stats
from baselines.slope_models import compute_slope
from detectors.window_deviation import detect_window_deviation
from detectors.slope_deviation import detect_slope_deviation

def run_detection():
    windowed_series = run_windowing()

    anomaly_signals = []

    for series_key, windows_by_type in windowed_series.items():
        for window_type, windows in windows_by_type.items():
            if len(windows) < 2:
                continue

            baseline_window = windows[:-1]
            current_window = windows[-1]

            baseline_stats = compute_rolling_stats(
                baseline_window[-1]
            )
            baseline_slope = compute_slope(
                baseline_window[-1]
            )

            current_slope = compute_slope(current_window)

            level_signal = detect_window_deviation(
                current_window,
                baseline_stats
            )

            slope_signal = detect_slope_deviation(
                current_slope,
                baseline_slope
            )

            if level_signal["anomalous"] or slope_signal["anomalous"]:
                anomaly_signals.append({
                    "series": series_key,
                    "window": window_type,
                    "signals": [
                        level_signal,
                        slope_signal
                    ]
                })

    for signal in anomaly_signals:
        print(signal)

    return anomaly_signals

if __name__ == "__main__":
    run_detection()
"""