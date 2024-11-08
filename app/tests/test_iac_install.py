import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.models import IaCInstallationInput

client = TestClient(app)
mocked_gpt_response = "Mocked shell script for installing terraform on Ubuntu."

@pytest.fixture
def valid_installation_data():
    return IaCInstallationInput(
        os="ubuntu",
        service="terraform",
        min_tokens=100,
        max_tokens=500
    )
@patch('app.main.gpt_service', return_value=mocked_gpt_response)
def test_install(mock_gpt_service, valid_installation_data):
    """
    Test the /IaC-install/ endpoint with valid input data to ensure correct output.
    """
    response = client.post("/IaC-install/", json=valid_installation_data.model_dump())
    assert response.status_code == 200
    assert response.json() == {"output": mocked_gpt_response}
    expected_prompt = """
        generate a clear shell script about installation terraform in ubuntu based on terraform document.
        without any additional note. just script for installation. please consider new lines without any additional comment.
    """
    actual_prompt = " ".join(mock_gpt_service.call_args[0][0].split()).strip()
    normalized_expected_prompt = " ".join(expected_prompt.split()).strip()
    if actual_prompt != normalized_expected_prompt:
        print("Expected Prompt:", repr(normalized_expected_prompt))
        print("Actual Prompt:", repr(actual_prompt))

    assert actual_prompt == normalized_expected_prompt

@patch('app.main.gpt_service')
def test_install_invalid(mock_gpt_service):
    """
    Test the /IaC-install/ endpoint with an invalid 'os' value to ensure proper validation.
    """
    invalid_input = {
        "os": "Kali",  
        "service": "terraform"
    }

    response = client.post("/IaC-install/", json=invalid_input)

    assert response.status_code == 422, f"Expected status code 422, got {response.status_code}"
    assert "detail" in response.json(), "Response JSON does not contain 'detail'"
    errors = response.json()["detail"]

    expected_error_loc = ["body", "os"]
    expected_error_msg = "OS must be one of ['ubuntu', 'centos', 'debian']."

    assert any(
        error["loc"] == expected_error_loc and error_msg in error["msg"]
        for error in errors
        for error_msg in [expected_error_msg]
    ), f"Expected error message '{expected_error_msg}' at location {expected_error_loc}, but not found."
    mock_gpt_service.assert_not_called()
