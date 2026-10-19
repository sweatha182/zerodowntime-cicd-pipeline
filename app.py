
from datetime import datetime, timezone


def check_health():
    """Return a health status for deployment verification."""
    return {
        "status": "healthy",
        "service": "NovaPay",
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    print(check_health())
