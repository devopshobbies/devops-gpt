import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from app.models import IaCTemplateGeneration

client = TestClient(app)

@pytest.fixture
def sample_iac_template_input():
    return IaCTemplateGeneration(
        service="terraform",        
        CI_integration=True,
        base_config="ec2"           
    )

@patch("app.main.gpt_service")
@patch("app.main.edit_directory_generator")
@patch("app.main.execute_pythonfile")
def test_template(mock_execute_pythonfile, mock_edit_directory_generator, mock_gpt_service, sample_iac_template_input):
    mock_gpt_service.return_value = "Generated Python Code"

    response = client.post("/IaC-template/", json=sample_iac_template_input.model_dump())

    assert response.status_code == 200
    assert response.json()["output"] == "output"

    mock_gpt_service.assert_called_once()
    mock_edit_directory_generator.assert_called_once_with("terraform_generator", "Generated Python Code")
    mock_execute_pythonfile.assert_called_once_with("MyTerraform", "terraform_generator")

@patch("app.main.gpt_service")
@patch("app.main.edit_directory_generator")
@patch("app.main.execute_pythonfile")
def test_template_invalid(mock_execute_pythonfile, mock_edit_directory_generator, mock_gpt_service):
    """
    Test the /IaC-template/ endpoint with an invalid 'base_config' to ensure proper validation.
    """
    invalid_input = {
        "CI_integration": True,
        "base_config": "k8s",  
        "service": "terraform"
    }
    response = client.post("/IaC-template/", json=invalid_input)
    assert response.status_code == 422, f"Expected status code 422, got {response.status_code}"
    assert "detail" in response.json(), "Response JSON does not contain 'detail'"
    errors = response.json()["detail"]
    expected_error_loc = ["body", "base_config"]
    expected_error_msg = "Base config must be one of ['ec2', 's3', 'rds','docker']."
    assert any(
        error["loc"] == expected_error_loc and expected_error_msg in error["msg"]
        for error in errors
    ), f"Expected error message '{expected_error_msg}' at location {expected_error_loc}, but not found."
    mock_gpt_service.assert_not_called()
    mock_edit_directory_generator.assert_not_called()
    mock_execute_pythonfile.assert_not_called()
