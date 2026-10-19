
from pathlib import Path


def test_readme_exists():
    assert Path("README.md").is_file()


def test_workflow_exists():
    assert Path(".github/workflows/ci-cd.yml").is_file()


def test_readme_is_not_empty():
    assert Path("README.md").stat().st_size > 0
