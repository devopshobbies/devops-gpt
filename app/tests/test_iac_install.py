# import pytest
# from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
# from app.main import app
# from app.models import IaCInstallationInput

# client = TestClient(app)

class TestIaCInastall:
    def setup_method(self):
        mock_client_instance = MagicMock()
        mock_client_instance.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content='Mocked OpenAI Response'))]
        )

        self.mock_gpt_service = patch('app.main.gpt_service', return_value='Mocked GPT Response').start()
        self.mock_openai = patch('app.gpt_services.OpenAI', return_value=mock_client_instance).start()

        self.url = '/IaC-install/'

    def teardown_method(self):
        patch.stopall()
    
    def test_iac_install(self, client, iac_install_sample_input):
        response = client.post(self.url, json=iac_install_sample_input)
        assert response.status_code == 200
    
    def test_iac_install_invalid_input(self, client, iac_install_invalid_sample_input):
        response = client.post(self.url, json=iac_install_invalid_sample_input)
        assert response.status_code == 422

# @pytest.fixture
# def valid_installation_data():
#     return IaCInstallationInput(
#         os="ubuntu",
#         service="terraform",
#         min_tokens=100,
#         max_tokens=500
#     )

# @patch('app.main.gpt_service')
# def test_install(mock_gpt_service, valid_installation_data):
#     """
#     Test the /IaC-install/ endpoint with valid input data to ensure it returns a 200 status code.
#     """
#     mock_gpt_service.return_value = "Mocked shell script for installing terraform on Ubuntu."

#     response = client.post("/IaC-install/", json=valid_installation_data.model_dump())
#     assert response.status_code == 200


# @patch('app.main.gpt_service')
# def test_install_invalid(mock_gpt_service):
#     """
#     Test the /IaC-install/ endpoint with an invalid 'os' value to ensure it returns a 422 status code.
#     """
#     invalid_input = {
#         "os": "Kali",  # Unsupported OS
#         "service": "terraform",
#         "min_tokens": 100,
#         "max_tokens": 500
#     }

#     response = client.post("/IaC-install/", json=invalid_input)
#     assert response.status_code == 422
