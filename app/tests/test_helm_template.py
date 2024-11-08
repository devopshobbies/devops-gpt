import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from app.models import HelmTemplateGeneration, Pod, Persistance, Ingress, Environment, Output

client = TestClient(app)

@pytest.fixture
def sample_helm_template_input():
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
    return {
        "api_version": 0,  # Invalid api_version
        "pods": [
            {
                "name": "",  # Invalid: empty name
                "image": "nginx:latest",
                "target_port": 70000,  # Invalid: exceeds 65535
                "replicas": 0,  # Invalid: less than 1
                "persistance": {"size": "invalid_size", "accessModes": "InvalidMode"},  # Invalid size and accessModes
                "environment": [{"name": "", "value": ""}],  # Invalid: empty name and value
                "stateless": True,
                "ingress": {"enabled": True, "host": ""}  # Invalid: empty host
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
    mock_gpt_service.return_value = "Generated Python Code"

    response = client.post("/Helm-template/", json=sample_helm_template_input.model_dump())

    assert response.status_code == 200
    assert response.json()["output"] == "output"

    mock_gpt_service.assert_called_once()
    mock_edit_directory_generator.assert_called_once_with("helm_generator", "Generated Python Code")
    mock_execute_pythonfile.assert_called_once_with("MyHelm", "helm_generator")

@patch("app.main.execute_pythonfile")
@patch("app.main.edit_directory_generator")
@patch("app.main.gpt_service")
def test_helm_invalid_api(
    mock_gpt_service,
    mock_edit_directory_generator,
    mock_execute_pythonfile,
    invalid_input
):
    invalid_input = invalid_input.copy()
    invalid_input["api_version"] = 0  
    response = client.post("/Helm-template/", json=invalid_input)
    assert response.status_code == 422  
    assert "detail" in response.json()
    errors = response.json()["detail"]
    assert any(
        error["loc"] == ["body", "api_version"] and "API version must be a positive integer." in error["msg"]
        for error in errors
    )
    mock_gpt_service.assert_not_called()
    mock_edit_directory_generator.assert_not_called()
    mock_execute_pythonfile.assert_not_called()

@patch("app.main.execute_pythonfile")
@patch("app.main.edit_directory_generator")
@patch("app.main.gpt_service")
def test_helm_invalid_port(
    mock_gpt_service,
    mock_edit_directory_generator,
    mock_execute_pythonfile,
    invalid_input):

    invalid_input = invalid_input.copy()
    invalid_input["pods"][0]["target_port"] = 70000  # Invalid target_port
    response = client.post("/Helm-template/", json=invalid_input)
    assert response.status_code == 422
    assert "detail" in response.json()
    errors = response.json()["detail"]
    assert any(
        error["loc"] == ["body", "pods", 0, "target_port"] and "Target port must be between 1 and 65535." in error["msg"]
        for error in errors
    )
    mock_gpt_service.assert_not_called()
    mock_edit_directory_generator.assert_not_called()
    mock_execute_pythonfile.assert_not_called()
