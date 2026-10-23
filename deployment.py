
def verify_deployment(health_status):
    """
    Verify deployment health and decide whether rollback is needed.

    This function returns a decision only.
    It does not perform an actual rollback.
    """
    if not isinstance(health_status, str):
        raise TypeError("health_status must be a string")

    if health_status == "healthy":
        return {
            "deployment": "successful",
            "rollback_required": False,
        }

    if health_status == "unhealthy":
        return {
            "deployment": "failed",
            "rollback_required": True,
        }

    raise ValueError("health_status must be 'healthy' or 'unhealthy'")


if __name__ == "__main__":
    print(verify_deployment("healthy"))
    print(verify_deployment("unhealthy"))
