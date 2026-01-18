# windows/window_config.py

# windows/window_config.py

"""
Window definitions for sliding window construction.

NOTE:
These values are intentionally SMALL to allow:
- fast iteration
- visible Stage 5 anomalies
- local testing with limited Prometheus history

They will be increased for production.
"""

WINDOW_DEFINITIONS = {
    # Fast reaction window (CPU spikes, short-term load)
    "short": {
        "duration_sec": 60,    # 1 minute window
        "slide_sec": 15        # slide every 15 seconds
    },

    # Stability window (sustained behavior)
    "medium": {
        "duration_sec": 300,   # 5 minutes window
        "slide_sec": 60        # slide every 1 minute
    },

    # Trend window (slow degradation, leaks)
    "long": {
        "duration_sec": 600,   # 10 minutes window
        "slide_sec": 120       # slide every 2 minutes
    }
}








"""
WINDOW_DEFINITIONS = {
    "short": {
        "duration_sec": 30,     # 5 minutes
        "slide_sec": 10          # slide every 1 minute
    },
    "medium": {
        "duration_sec": 3600,    # 1 hour
        "slide_sec": 300         # slide every 5 minutes
    },
    "long": {
        "duration_sec": 86400,   # 24 hours
        "slide_sec": 3600        # slide every 1 hour
    }
}

"""