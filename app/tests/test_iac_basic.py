import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.models import IaCBasicInput

client = TestClient(app)

@pytest.fixture
def valid_iac_basic_data():
    return IaCBasicInput(
        input="How do I manage state effectively in Terraform?",
        service="terraform",
        min_tokens=100,
        max_tokens=500
    )

@patch('app.main.gpt_service')
def test_iac_basic_generation(mock_gpt_service, valid_iac_basic_data):
    """
    Test the /IaC-basic/ endpoint with valid input data to ensure it returns a 200 status code.
    """
    mock_gpt_service.return_value = "Mocked GPT response for IaC-basic"

    response = client.post("/IaC-basic/", json=valid_iac_basic_data.model_dump())
    assert response.status_code == 200


@patch('app.main.gpt_service')
def test_basic_generation_invalid_service(mock_gpt_service):
    """
    Test the /IaC-basic/ endpoint with an invalid service to ensure it returns a 422 status code.
    """
    invalid_input = {
        "input": "Create a basic configuration",
        "service": "invalid_service",  # Unsupported service (invalid)
        "min_tokens": 100,
        "max_tokens": 500
    }

    response = client.post("/IaC-basic/", json=invalid_input)
    assert response.status_code == 422
