import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from app.models import HelmTemplateGeneration, Pod, Persistance, Ingress, Environment

client = TestClient(app)
@pytest.fixture
def sample_helm_template_input():
    """
    Provides a valid HelmTemplateGeneration object as input for tests.
    """
    return HelmTemplateGeneration(
        api_version=3,
        pods=[
            Pod(
                name="nginx",
                image="nginx:latest",
                target_port=80,
                replicas=2,
                persistance=Persistance(enabled=False),
                environment=[Environment(name="DEBUG", value="true")],
                stateless=True,
                ingress=Ingress(enabled=True)
            ),
            Pod(
                name="redis",
                image="redis:latest",
                target_port=6379,
                replicas=1,
                persistance=Persistance(enabled=True),
                environment=[],
                stateless=False,
                ingress=Ingress(enabled=False)
            )
        ]
    )

@pytest.fixture
def invalid_input():
    """
    Provides an invalid input dictionary for tests, containing various validation errors.
    """
    return {
        "api_version": 0,  
        "pods": [
            {
                "name": "",  
                "image": "nginx:latest",
                "target_port": 70000,
                "replicas": 0, 
                "persistance": {"size": "invalid_size", "accessModes": "InvalidMode"},  
                "environment": [{"name": "", "value": ""}],  
                "stateless": True,
                "ingress": {"enabled": True, "host": ""} 
            }
        ]
    }

@patch("app.main.execute_pythonfile")
@patch("app.main.edit_directory_generator")
@patch("app.main.gpt_service")
def test_helm_template_generation(
    mock_gpt_service,
    mock_edit_directory_generator,
    mock_execute_pythonfile,
    sample_helm_template_input
):
    """
    Tests the /Helm-template/ endpoint with valid input.
    """
    
    mock_gpt_service.return_value = "Generated Python Code"
    response = client.post("/Helm-template/", json=sample_helm_template_input.model_dump())
    assert response.status_code == 200
    mock_gpt_service.assert_called_once()
    mock_edit_directory_generator.assert_called_once_with("helm_generator", "Generated Python Code")
    mock_execute_pythonfile.assert_called_once_with("MyHelm", "helm_generator")

def test_helm_invalid_api(invalid_input):
    """
    Tests the /Helm-template/ endpoint with an invalid API version.
    """
    invalid_input = invalid_input.copy()
    invalid_input["api_version"] = 0  


    response = client.post("/Helm-template/", json=invalid_input)

    assert response.status_code == 422


@patch("app.main.execute_pythonfile")
@patch("app.main.edit_directory_generator")
@patch("app.main.gpt_service")
def test_helm_invalid_port(
    mock_gpt_service,
    mock_edit_directory_generator,
    mock_execute_pythonfile,
    invalid_input
):
    """
    Tests the /Helm-template/ endpoint with an invalid target port.
    """
    invalid_input = invalid_input.copy()
    invalid_input["pods"][0]["target_port"] = 70000  
    response = client.post("/Helm-template/", json=invalid_input)
    assert response.status_code == 422
    mock_gpt_service.assert_not_called()
    mock_edit_directory_generator.assert_not_called()
    mock_execute_pythonfile.assert_not_called()
