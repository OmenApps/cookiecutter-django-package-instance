"""Test cases for the cookiecutter-django-package-instance package."""

import pytest
from click.testing import CliRunner
from django.apps import apps
from django.conf import settings


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    assert 0 == 0


def test_settings(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    assert settings.USE_TZ is True


def test_apps(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    assert "cookiecutter_django_package_instance" in apps.get_app_config("cookiecutter_django_package_instance").name
