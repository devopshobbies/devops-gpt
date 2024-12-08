from unittest.mock import MagicMock, patch


class TestIaCBasic:
    def setup_method(self):
        mock_client_instance = MagicMock()
        mock_client_instance.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content='Mocked OpenAI Response'))]
        )

        self.mock_gpt_service = patch('app.main.gpt_service', return_value='Mocked GPT Response').start()
        self.mock_openai = patch('app.gpt_services.OpenAI', return_value=mock_client_instance).start()

        self.url = '/api/IaC-basic/'

    def teardown_method(self):
        patch.stopall()

    def test_iac_basic_generation(self, client, iac_basic_sample_input):
        response = client.post(self.url, json=iac_basic_sample_input)
        assert response.status_code == 200

    def test_basic_generation_invalid_service(self, client, iac_basic_invalid_sample_input):
        response = client.post(self.url, json=iac_basic_invalid_sample_input)
        assert response.status_code == 422
