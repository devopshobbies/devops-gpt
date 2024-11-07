import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from app.models import IaCTemplateGeneration

client = TestClient(app)

@pytest.fixture
def sample_iac_template_input():
    return IaCTemplateGeneration(
        service="MyService",
        CI_integration=True,
        base_config="BasicConfig"
    )

@patch("app.main.gpt_service")
@patch("app.main.edit_directory_generator")
@patch("app.main.execute_pythonfile")
def test_iac_template_generation(mock_execute_pythonfile, mock_edit_directory_generator, mock_gpt_service, sample_iac_template_input):
    mock_gpt_service.return_value = "Generated Python Code"

    response = client.post("/IaC-template/", json=sample_iac_template_input.dict())

    assert response.status_code == 200
    assert response.json()["output"] == "output"

    mock_gpt_service.assert_called_once()
    mock_edit_directory_generator.assert_called_once_with("terraform_generator", "Generated Python Code")
    mock_execute_pythonfile.assert_called_once_with("MyTerraform", "terraform_generator")
