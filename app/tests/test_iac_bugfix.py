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
        input="Fix the deployment issue",
        bug_description="Application fails to start on version 1.2.3",
        version="1.2.3",
        service="terraform",
        min_tokens=100,
        max_tokens=500
    )

@patch('app.main.gpt_service', return_value=mocked_gpt_response)
def test_iac_bugfix_generation(mock_gpt_service, valid_bugfix_data):
    """
    Test the /IaC-bugfix/ endpoint with valid input data to ensure correct output.
    """
    response = client.post("/IaC-bugfix/", json=valid_bugfix_data.model_dump())
    assert response.status_code == 200
    assert response.json() == {"output": mocked_gpt_response}

    expected_prompt = """
        Write a clear answer to debug terraform
        focusing on the version 1.2.3 of terraform and based on this bug:Application fails to start on version 1.2.3,
        generate a correct code that help us to solve this bug.
        minimun length of answer is 100 and maximum length is 500
    """
    actual_prompt = " ".join(mock_gpt_service.call_args[0][0].split())
    normalized_expected_prompt = " ".join(expected_prompt.split())
    assert actual_prompt == normalized_expected_prompt
