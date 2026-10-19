
def evaluate_compliance(sast_passed, dependency_scan_passed,
                        approval_present, tests_passed):
    """Block release when required compliance checks fail."""
    checks = {
        "sast": sast_passed,
        "dependency_scan": dependency_scan_passed,
        "independent_approval": approval_present,
        "automated_tests": tests_passed,
    }

    failed_checks = [
        name for name, passed in checks.items() if not passed
    ]

    return {
        "release_approved": len(failed_checks) == 0,
        "failed_checks": failed_checks,
    }


if __name__ == "__main__":
    print(evaluate_compliance(True, True, True, True))
    print(evaluate_compliance(True, False, True, True))
