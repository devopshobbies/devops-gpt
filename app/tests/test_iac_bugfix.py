import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.models import IaCBugfixInput

client = TestClient(app)
mocked_gpt_response = "Mocked GPT response for IaC-bugfix"

@pytest.fixture
def valid_bugfix_data():
    return IaCBugfixInput(
        bug_description="Application fails to start on version latest",
        version="latest",
        service="terraform",
        min_tokens=100,
        max_tokens=500
    )

@patch('app.main.gpt_service', return_value=mocked_gpt_response)
def test_bugfix(mock_gpt_service, valid_bugfix_data):
    """
    Test the /IaC-bugfix/ endpoint with valid input data to ensure correct output.
    """
    response = client.post("/IaC-bugfix/", json=valid_bugfix_data.model_dump())
    assert response.status_code == 200
    assert response.json() == {"output": mocked_gpt_response}

    expected_prompt = """
    Write a clear answer to debug terraform
    focusing on the version latest of terraform and based on this bug:Application fails to start on version latest,
    generate a correct code that help us to solve this bug.
    minimum length of answer is 100 and maximum length is 500
    """


    actual_prompt = " ".join(mock_gpt_service.call_args[0][0].split())
    normalized_expected_prompt = " ".join(expected_prompt.split())
    assert actual_prompt == normalized_expected_prompt


@patch('app.main.gpt_service') 
def test_bugfix_invalid(mock_gpt_service):
    """
    Test the /IaC-bugfix/ endpoint with a single invalid input to ensure proper validation.
    """
    invalid_input = {
        "bug_description": "",  # Emptydescription
        "version": "latest",
        "service": "terraform",
        "min_tokens": 100,
        "max_tokens": 500
    }
    response = client.post("/IaC-bugfix/", json=invalid_input)
    assert response.status_code == 422, f"Expected status code 422, got {response.status_code}"
    assert "detail" in response.json(), "Response JSON does not contain 'detail'"
    errors = response.json()["detail"]
    expected_error_loc = ["body", "bug_description"]
    expected_error_msg = "Bug description cannot be empty."
    assert any(
        error["loc"] == expected_error_loc and expected_error_msg in error["msg"]
        for error in errors
    ), f"Expected error message '{expected_error_msg}' at location {expected_error_loc}, but not found."
    mock_gpt_service.assert_not_called()
