# scripts/run_incidents.py

from scripts.run_detection import run_detection
from incidents.anomaly_grouper import group_anomalies
from incidents.incident_builder import build_incident
from incidents.incident_correlator import correlate_incidents


def run_incidents(debug: bool = True):
    """
    Stage 6 — Incident Management
    - Runs detection (Stage 5)
    - Groups anomalies (Stage 6)
    - Builds raw incidents
    - Correlates incidents (Stage 6.1)
    """

    print("\n[STAGE 6] Running anomaly detection...")
    anomalies = run_detection()

    if not anomalies:
        print("[STAGE 6] No anomalies detected.")
        return []

    print(f"[STAGE 6] Detected {len(anomalies)} anomalies")

    # --- Group anomalies into incident candidates ---
    groups = group_anomalies(anomalies)
    print(f"[STAGE 6] Grouped into {len(groups)} incident candidates")

    # --- Build raw incidents ---
    raw_incidents = []
    for group in groups:
        incident = build_incident(group)
        raw_incidents.append(incident)

    print(f"[STAGE 6] Built {len(raw_incidents)} raw incidents")

    # --- Correlate incidents (Stage 6.1) ---
    incidents = correlate_incidents(raw_incidents)
    print(f"[STAGE 6] Correlated into {len(incidents)} final incidents\n")

    # --- Debug output ---
    if debug:
        for idx, incident in enumerate(incidents, start=1):
            print("=" * 80)
            print(f"INCIDENT #{idx}")
            print(f"Series          : {incident['series']}")
            print(f"Incident type   : {incident.get('incident_type', 'unknown')}")
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














"""
# scripts/run_incidents.py

from scripts.run_detection import run_detection
from incidents.anomaly_grouper import group_anomalies
from incidents.incident_builder import build_incident


def run_incidents(debug: bool = True):
    
    #Stage 6 entry point:
    #- Runs detection (Stage 5)
    #- Groups anomalies
    #- Builds incidents
    

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
"""