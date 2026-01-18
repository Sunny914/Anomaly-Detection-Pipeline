# windows/window_config.py

WINDOW_DEFINITIONS = {
    "short": {
        "duration_sec": 300,     # 5 minutes
        "slide_sec": 60          # slide every 1 minute
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
