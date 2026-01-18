# scripts/run_detection.py

# scripts/run_detection.py

from scripts.run_windowing import run_windowing
from baselines.rolling_stats import compute_rolling_stats
from baselines.slope_models import compute_slope
from detectors.window_deviation import detect_window_deviation
from detectors.slope_deviation import detect_slope_deviation


MIN_CONFIDENCE = 0.6      # suppress weak signals
REQUIRE_BOTH = False     # if True → require both detectors


def _aggregate_severity(severities):
    if "high" in severities:
        return "high"
    if "medium" in severities:
        return "medium"
    return "low"


def _aggregate_confidence(confidences):
    return round(sum(confidences) / len(confidences), 2)


def run_detection(debug=False):
    """
    Stage 5 — Detection & Fusion
    Produces structured anomaly records.
    """

    windowed_series = run_windowing()
    anomalies = []

    for series_key, windows_by_type in windowed_series.items():
        for window_type, windows in windows_by_type.items():

            if len(windows) < 2:
                continue

            for i in range(1, len(windows)):
                baseline_windows = windows[:i]
                current_window = windows[i]

                baseline_stats = compute_rolling_stats(baseline_windows)
                baseline_slope = compute_slope(baseline_windows)

                if not baseline_stats:
                    continue

                signals = []

                # Detector A — Mean deviation
                mean_signal = detect_window_deviation(
                    series_key,
                    window_type,
                    current_window,
                    baseline_stats
                )
                if mean_signal:
                    signals.append(mean_signal)

                # Detector B — Slope deviation
                slope_signal = detect_slope_deviation(
                    series_key,
                    window_type,
                    current_window,
                    baseline_slope
                )
                if slope_signal:
                    signals.append(slope_signal)

                # --- Fusion logic ---
                if not signals:
                    continue

                if REQUIRE_BOTH and len(signals) < 2:
                    continue

                confidences = [s["confidence"] for s in signals]
                avg_confidence = _aggregate_confidence(confidences)

                if avg_confidence < MIN_CONFIDENCE:
                    continue

                severities = [s["severity"] for s in signals]
                final_severity = _aggregate_severity(severities)

                anomaly = {
                    "series": str(series_key),
                    "window_type": window_type,
                    "detectors_triggered": [s["detector"] for s in signals],
                    "severity": final_severity,
                    "confidence": avg_confidence,
                    "signals": signals
                }

                anomalies.append(anomaly)

                if debug:
                    print("ANOMALY:", anomaly)

    return anomalies


if __name__ == "__main__":
    run_detection(debug=True)














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