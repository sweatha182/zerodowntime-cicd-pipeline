
from pathlib import Path


def test_readme_exists():
    assert Path("README.md").is_file()


def test_workflow_exists():
    assert Path(".github/workflows/ci-cd.yml").is_file()


def test_readme_is_not_empty():
    assert Path("README.md").stat().st_size > 0
from app import check_health


def test_health_check_returns_healthy():
    result = check_health()
    assert result["status"] == "healthy"
    assert result["service"] == "NovaPay"

from deployment import verify_deployment


def test_healthy_deployment_does_not_require_rollback():
    result = verify_deployment("healthy")
    assert result["deployment"] == "successful"
    assert result["rollback_required"] is False


def test_unhealthy_deployment_requires_rollback():
    result = verify_deployment("unhealthy")
    assert result["deployment"] == "failed"
    assert result["rollback_required"] is True

from deployment_strategy import choose_deployment


def test_blue_green_switches_when_green_is_healthy():
    result = choose_deployment("blue", "green", True)
    assert result["active_version"] == "green"
    assert result["traffic_switched"] is True
    assert result["rollback_required"] is False


def test_blue_green_keeps_blue_when_green_is_unhealthy():
    result = choose_deployment("blue", "green", False)
    assert result["active_version"] == "blue"
    assert result["traffic_switched"] is False
    assert result["rollback_required"] is True

from canary_deployment import evaluate_canary


def test_canary_continues_when_error_rate_is_low():
    result = evaluate_canary(0.01)
    assert result["decision"] == "continue"
    assert result["traffic_percent"] == 10

from database_migration import migration_plan


def test_expand_keeps_old_schema_supported():
    result = migration_plan(True, True)
    assert result["phase"] == "expand"
    assert result["action"] == "add_new_schema_keep_old"
    assert result["safe_to_continue"] is True


def test_invalid_new_schema_stops_migration():
    result = migration_plan(True, False)
    assert result["safe_to_continue"] is False
    assert result["action"] == "stop"


def test_contract_is_allowed_after_old_schema_support_ends():
    result = migration_plan(False, True)
    assert result["phase"] == "contract"
    assert result["safe_to_continue"] is True


def test_canary_rolls_back_when_error_rate_is_high():
    result = evaluate_canary(0.05)
    assert result["decision"] == "rollback"
    assert result["traffic_percent"] == 0

