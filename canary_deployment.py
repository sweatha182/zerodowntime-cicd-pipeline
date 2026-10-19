
def evaluate_canary(error_rate, threshold=0.02):
    """Decide whether to continue or roll back a canary release."""
    if error_rate < 0 or error_rate > 1:
        raise ValueError("error_rate must be between 0 and 1")

    if error_rate > threshold:
        return {
            "decision": "rollback",
            "traffic_percent": 0,
        }

    return {
        "decision": "continue",
        "traffic_percent": 10,
    }


if __name__ == "__main__":
    print(evaluate_canary(0.01))
    print(evaluate_canary(0.05))
