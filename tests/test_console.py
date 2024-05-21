# tests/test_console.py
import click.testing
import pytest

from random_radon_transformation import console
    
from unittest.mock import Mock

from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture
import requests


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0

@pytest.fixture
def mock_random_radon_transformation(mocker):
    return mocker.patch("random_radon_transformation.random_radon_transformation.random_radon_transformation")


def test_random_radon_transformation_returns_right_shape(runner, mock_random_radon_transformation):
    runner.invoke(console.main)
    assert mock_random_radon_transformation.return_value.shape[0] == mock_random_radon_transformation.return_value.shape[1]


def test_input_right_shape(runner, mock_random_radon_transformation):
    runner.invoke(console.main)
    args, _ = mock_random_radon_transformation.call_args
    assert args[0].shape[0] == args[0].shape[1]


