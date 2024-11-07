import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from app.models import HelmTemplateGeneration, Pod, Persistance, Ingress

client = TestClient(app)

@pytest.fixture
def sample_helm_template_input():
    return HelmTemplateGeneration(
        api_version="3",
        pods=[
            Pod(name="nginx", image="nginx:latest", target_port=80, replicas=2, persistance=Persistance(enabled=False), environment=[{"name": "DEBUG", "value": "true"}], stateless=True, ingress=Ingress(enabled=True)),
            Pod(name="redis", image="redis:latest", target_port=6379, replicas=1, persistance=Persistance(enabled=True), environment=[], stateless=False, ingress=Ingress(enabled=False))
        ]
    )

@patch("app.main.gpt_service")
@patch("app.main.edit_directory_generator")
@patch("app.main.execute_pythonfile")
def test_helm_template_generation(mock_execute_pythonfile, mock_edit_directory_generator, mock_gpt_service, sample_helm_template_input):
    mock_gpt_service.return_value = "Generated Python Code"

    response = client.post("/Helm-template/", json=sample_helm_template_input.dict())

    assert response.status_code == 200
    assert response.json()["output"] == "output"

    mock_gpt_service.assert_called_once()
    mock_edit_directory_generator.assert_called_once_with("helm_generator", "Generated Python Code")
    mock_execute_pythonfile.assert_called_once_with("MyHelm", "helm_generator")
