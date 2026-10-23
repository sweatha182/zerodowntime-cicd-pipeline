
from deployment_strategy import choose_deployment


def test_blue_green_switches_when_new_version_is_healthy():
    result = choose_deployment("blue", "green", True)

    assert result["active_version"] == "green"
    assert result["traffic_switched"] is True
    assert result["rollback_required"] is False
    assert result["status"] == "deployment_successful"


def test_blue_green_preserves_old_version_when_new_version_fails():
    result = choose_deployment("blue", "green", False)

    assert result["active_version"] == "blue"
    assert result["traffic_switched"] is False
    assert result["rollback_required"] is True
    assert result["status"] == "deployment_failed"


def test_blue_green_rejects_same_active_and_new_version():
    import pytest

    with pytest.raises(ValueError):
        choose_deployment("blue", "blue", True)


def test_blue_green_rejects_invalid_health_value():
    import pytest

    with pytest.raises(TypeError):
        choose_deployment("blue", "green", "healthy")

from canary_deployment import evaluate_canary


def test_canary_continues_when_error_rate_is_below_threshold():
    result = evaluate_canary(0.01)

    assert result["decision"] == "continue"
    assert result["traffic_percent"] == 10


def test_canary_rolls_back_when_error_rate_exceeds_threshold():
    result = evaluate_canary(0.05)

    assert result["decision"] == "rollback"
    assert result["traffic_percent"] == 0


def test_canary_accepts_error_rate_at_threshold():
    result = evaluate_canary(0.02)

    assert result["decision"] == "continue"
    assert result["traffic_percent"] == 10


def test_canary_rejects_negative_error_rate():
    import pytest

    with pytest.raises(ValueError):
        evaluate_canary(-0.01)


def test_canary_rejects_error_rate_above_one():
    import pytest

    with pytest.raises(ValueError):
        evaluate_canary(1.01)

from deployment import verify_deployment
import pytest


def test_deployment_succeeds_when_healthy():
    result = verify_deployment("healthy")

    assert result["deployment"] == "successful"
    assert result["rollback_required"] is False


def test_deployment_fails_when_unhealthy():
    result = verify_deployment("unhealthy")

    assert result["deployment"] == "failed"
    assert result["rollback_required"] is True


def test_deployment_rejects_unknown_health_status():
    with pytest.raises(ValueError):
        verify_deployment("unknown")


def test_deployment_rejects_non_string_health_status():
    with pytest.raises(TypeError):
        verify_deployment(None)
from database_migration import migration_plan

def test_migration_expands_when_new_schema_is_valid():
result = migration_plan(True, True)


assert result["phase"] == "expand"
assert result["action"] == "add_new_schema_keep_old"
assert result["safe_to_continue"] is True


def test_migration_contracts_when_old_schema_is_unsupported():
result = migration_plan(False, True)


assert result["phase"] == "contract"
assert result["action"] == "remove_old_schema"
assert result["safe_to_continue"] is True


def test_migration_stops_when_new_schema_is_invalid():
result = migration_plan(True, False)


assert result["phase"] == "expand"
assert result["action"] == "stop"
assert result["safe_to_continue"] is False


