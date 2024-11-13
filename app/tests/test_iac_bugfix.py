import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.models import IaCBugfixInput

client = TestClient(app)

@pytest.fixture
def valid_bugfix_data():
    return IaCBugfixInput(
        bug_description="Application fails to start on version latest",
        version="latest",
        service="terraform",
        min_tokens=100,
        max_tokens=500
    )

@patch('app.main.gpt_service')
def test_bugfix(mock_gpt_service, valid_bugfix_data):
    """
    Test the /IaC-bugfix/ endpoint with valid input data to ensure it returns a 200 status code.
    """
    mock_gpt_service.return_value = "Mocked GPT response for IaC-bugfix"

    response = client.post("/IaC-bugfix/", json=valid_bugfix_data.model_dump())
    assert response.status_code == 200


@patch('app.main.gpt_service')
def test_bugfix_invalid(mock_gpt_service):
    """
    Test the /IaC-bugfix/ endpoint with invalid input data to ensure it returns a 422 status code.
    """
    invalid_input = {
        "bug_description": "",  # Empty description
        "version": "latest",
        "service": "terraform",
        "min_tokens": 100,
        "max_tokens": 500
    }

    response = client.post("/IaC-bugfix/", json=invalid_input)
    assert response.status_code == 422
