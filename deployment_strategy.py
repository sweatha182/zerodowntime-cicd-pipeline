
def choose_deployment(active_version, new_version, new_version_healthy):
    """Switch traffic only when the new version is healthy."""
    if not new_version_healthy:
        return {
            "active_version": active_version,
            "traffic_switched": False,
            "rollback_required": True,
        }

    return {
        "active_version": new_version,
        "traffic_switched": True,
        "rollback_required": False,
    }


if __name__ == "__main__":
    print(choose_deployment("blue", "green", True))
    print(choose_deployment("blue", "green", False))
