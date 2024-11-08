import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.models import IaCBasicInput

client = TestClient(app)
mocked_gpt_response = "Mocked GPT response for IaC-basic"

@pytest.fixture
def valid_iac_basic_data():
    return IaCBasicInput(
        input="How do I manage state effectively in Terraform?",
        service="terraform",
        min_tokens=100,
        max_tokens=500
    )

@patch('app.main.gpt_service', return_value=mocked_gpt_response)
def test_iac_basic_generation(mock_gpt_service, valid_iac_basic_data):
    """
    Test the /IaC-basic/ endpoint with valid input data to ensure correct output.
    """
    response = client.post("/IaC-basic/", json=valid_iac_basic_data.model_dump())
    assert response.status_code == 200
    assert response.json() == {"output": mocked_gpt_response}
    
@patch('app.main.gpt_service')  
def test_basic_generation(mock_gpt_service):
    """
    Test the /IaC-basic/ endpoint with an invalid service to ensure proper validation.
    """
    invalid_input = {
        "input": "Create a basic configuration",
        "service": "invalid_service",  # Unsupported service (invalid)
        "min_tokens": 100,
        "max_tokens": 500
    }

    response = client.post("/IaC-basic/", json=invalid_input)
    assert response.status_code == 422, f"Expected status code 422, got {response.status_code}"
    assert "detail" in response.json(), "Response JSON does not contain 'detail'"
    errors = response.json()["detail"]
    expected_error_loc = ["body", "service"]
    expected_error_msg = "Service must be one of ['terraform']."
    assert any(
        error["loc"] == expected_error_loc and error_msg in error["msg"]
        for error in errors
        for error_msg in [expected_error_msg]
    ), f"Expected error message '{expected_error_msg}' at location {expected_error_loc}, but not found."

    mock_gpt_service.assert_not_called()
