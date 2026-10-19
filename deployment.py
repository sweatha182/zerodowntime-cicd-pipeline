
def verify_deployment(health_status):
    """Verify deployment health and decide whether rollback is needed."""
    if health_status == "healthy":
        return {
            "deployment": "successful",
            "rollback_required": False,
        }

    return {
        "deployment": "failed",
        "rollback_required": True,
    }


if __name__ == "__main__":
    print(verify_deployment("healthy"))
    print(verify_deployment("unhealthy"))
