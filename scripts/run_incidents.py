# scripts/run_incidents.py

from scripts.run_detection import run_detection
from incidents.anomaly_grouper import group_anomalies
from incidents.incident_builder import build_incident


def run_incidents(debug: bool = True):
    """
    Stage 6 entry point:
    - Runs detection (Stage 5)
    - Groups anomalies
    - Builds incidents
    """

    print("\n[STAGE 6] Running anomaly detection...")
    anomalies = run_detection()

    if not anomalies:
        print("[STAGE 6] No anomalies detected.")
        return []

    print(f"[STAGE 6] Detected {len(anomalies)} anomalies")

    # --- Group anomalies ---
    groups = group_anomalies(anomalies)

    print(f"[STAGE 6] Grouped into {len(groups)} incident candidates\n")

    incidents = []

    for idx, group in enumerate(groups, start=1):
        incident = build_incident(group)
        incidents.append(incident)

        if debug:
            print("=" * 80)
            print(f"INCIDENT #{idx}")
            print(f"Series          : {incident['series']}")
            print(f"Severity        : {incident['severity']}")
            print(f"Confidence      : {incident['confidence']}")
            print(f"Duration (sec)  : {round(incident['duration_sec'], 2)}")
            print(f"Anomaly count   : {incident['anomaly_count']}")
            print(f"Window types   : {incident['window_types']}")
            print(f"Dominant signal: {incident['dominant_detector']}")
            print(f"Trend direction: {incident['trend_direction']}")
            print("=" * 80)
            print()

    return incidents


if __name__ == "__main__":
    run_incidents()
