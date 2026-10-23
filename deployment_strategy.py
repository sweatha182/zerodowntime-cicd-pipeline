
def choose_deployment(active_version, new_version, new_version_healthy):
    """
    Decide whether to switch from the active version to the new version.

    This function models a blue-green deployment decision.
    It does not perform real traffic switching.
    """

    if not active_version or not new_version:
        raise ValueError("Active and new versions must be provided")

    if active_version == new_version:
        raise ValueError("Active and new versions must be different")

    if not isinstance(new_version_healthy, bool):
        raise TypeError("new_version_healthy must be a boolean")

    if not new_version_healthy:
        return {
            "active_version": active_version,
            "traffic_switched": False,
            "rollback_required": True,
            "status": "deployment_failed",
        }

    return {
        "active_version": new_version,
        "traffic_switched": True,
        "rollback_required": False,
        "status": "deployment_successful",
    }


if __name__ == "__main__":
    # Scenario 1: New version is healthy
    print("Healthy deployment:")
    print(choose_deployment("blue", "green", True))

    # Scenario 2: New version is unhealthy
    print("\nFailed deployment:")
    print(choose_deployment("blue", "green", False))

