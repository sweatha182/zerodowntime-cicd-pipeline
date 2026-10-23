
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

from compliance_gate import evaluate_compliance


def test_compliance_passes_when_all_checks_pass():
    result = evaluate_compliance(True, True, True, True)

    assert result["release_approved"] is True
    assert result["failed_checks"] == []


def test_compliance_blocks_release_when_sast_fails():
    result = evaluate_compliance(False, True, True, True)

    assert result["release_approved"] is False
    assert "sast" in result["failed_checks"]


def test_compliance_blocks_release_when_dependency_scan_fails():
    result = evaluate_compliance(True, False, True, True)

    assert result["release_approved"] is False
    assert "dependency_scan" in result["failed_checks"]


def test_compliance_blocks_release_without_independent_approval():
    result = evaluate_compliance(True, True, False, True)

    assert result["release_approved"] is False
    assert "independent_approval" in result["failed_checks"]


def test_compliance_blocks_release_when_tests_fail():
    result = evaluate_compliance(True, True, True, False)

    assert result["release_approved"] is False
    assert "automated_tests" in result["failed_checks"]


def test_compliance_reports_all_failed_checks():
    result = evaluate_compliance(False, False, False, False)

    assert result["release_approved"] is False
    assert set(result["failed_checks"]) == {
        "sast",
        "dependency_scan",
        "independent_approval",
        "automated_tests",
    }
