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
    """
    Test the /IaC-template/ endpoint with valid input data to ensure it returns a 200 status code.
    """
    mock_gpt_service.return_value = "Generated Python Code"

    response = client.post("/IaC-template/", json=sample_iac_template_input.model_dump())
    assert response.status_code == 200


@patch("app.main.gpt_service")
@patch("app.main.edit_directory_generator")
@patch("app.main.execute_pythonfile")
def test_template_invalid(mock_execute_pythonfile, mock_edit_directory_generator, mock_gpt_service):
    """
    Test the /IaC-template/ endpoint with an invalid 'base_config' value to ensure it returns a 422 status code.
    """
    invalid_input = {
        "CI_integration": True,
        "base_config": "k8s",  # Unsupported base_config
        "service": "terraform"
    }
    response = client.post("/IaC-template/", json=invalid_input)
    assert response.status_code == 422
