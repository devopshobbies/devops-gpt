import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.models import IaCBasicInput

client = TestClient(app)
mocked_gpt_response = "Mocked GPT response for IaC-basic"

@pytest.fixture
def valid_basic_data():
    return IaCBasicInput(
        input="Create a basic configuration",
        service="terraform",
        min_tokens=100,
        max_tokens=500
    )

@patch('app.main.gpt_service', return_value=mocked_gpt_response)
def test_iac_basic_generation(mock_gpt_service, valid_basic_data):
    """
    Test the /IaC-basic/ endpoint with valid input data.
    """
    response = client.post("/IaC-basic/", json=valid_basic_data.model_dump())
    assert response.status_code == 200
    assert response.json() == {"output": mocked_gpt_response}

    expected_prompt = """
        Write a robust answer about terraform,
        focusing on the latest update of terraform and based on this question:Create a basic configuration,
        minimun length of answer is 100 and maximum length is 500
    """
    actual_prompt = " ".join(mock_gpt_service.call_args[0][0].split())
    normalized_expected_prompt = " ".join(expected_prompt.split())
    assert actual_prompt == normalized_expected_prompt
