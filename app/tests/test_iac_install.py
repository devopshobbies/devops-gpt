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
def test_iac_install_generation(mock_gpt_service, valid_installation_data):
    """
    Test the /IaC-install/ endpoint with valid input data to ensure correct output.
    """
    response = client.post("/IaC-install/", json=valid_installation_data.model_dump())
    assert response.status_code == 200
    assert response.json() == {"output": mocked_gpt_response}

    expected_prompt = """
        generate a clear shell acript about installation terraform in ubuntu based on terraform document.
        without any additional note. just script for installation.
    """
    actual_prompt = " ".join(mock_gpt_service.call_args[0][0].split())
    normalized_expected_prompt = " ".join(expected_prompt.split())
    assert actual_prompt == normalized_expected_prompt
