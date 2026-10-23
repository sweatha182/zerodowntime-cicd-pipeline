
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

