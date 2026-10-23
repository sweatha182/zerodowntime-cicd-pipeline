from app import check_health
from deployment import verify_deployment
from deployment_strategy import choose_deployment
from canary_deployment import evaluate_canary
from database_migration import migration_plan
from compliance_gate import evaluate_compliance

def test_health_to_deployment_verification():
    health = check_health()
    result = verify_deployment(health["status"])
    assert result["deployment"] == "successful"
    assert result["rollback_required"] is False

def test_canary_failure_blocks_release():
    canary = evaluate_canary(0.05)
    compliance = evaluate_compliance(
    True, True, True, canary["decision"] == "continue")
    assert canary["decision"] == "rollback"
    assert compliance["release_approved"] is False

def test_migration_stops_when_new_schema_is_invalid():
    result = migration_plan(True, False)
    assert result["safe_to_continue"] is False

def test_compliance_blocks_release_when_automated_tests_fail():
    result = evaluate_compliance(
    True,   # SAST passed
    True,   # Dependency scan passed
    True,   # Independent approval
    False,  # Automated tests failed
    )
    assert result["release_approved"] is False
    assert "automated_tests" in result["failed_checks"]

def test_blue_green_keeps_old_version_on_failure():
    result = choose_deployment("blue", "green", False)

assert result["active_version"] == "blue"
assert result["traffic_switched"] is False
```
