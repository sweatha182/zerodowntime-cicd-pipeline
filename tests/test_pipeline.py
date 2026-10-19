
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
