from unittest.mock import MagicMock, patch, mock_open


class TestHelmTemplate:
    def setup_method(self):
        mock_client_instance = MagicMock()
        mock_client_instance.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content='Mocked OpenAI Response'))]
        )

        self.mock_execute_python_file = patch('app.main.execute_pythonfile').start()
        self.mock_edit_directory_generator = patch('app.main.edit_directory_generator').start()
        self.mock_gpt_service = patch('app.main.gpt_service', return_value='Mocked GPT Response').start()
        self.mock_openai = patch('app.gpt_services.OpenAI', return_value=mock_client_instance).start()
        self.mock_builtin_open = patch('builtins.open', mock_open()).start()
        self.mock_shutil_rm = patch('shutil.rmtree').start()

        self.url = '/api/Helm-template/'

    def teardown_method(self):
        patch.stopall()

    def test_helm_template_generation(self, client, helm_template_sample_input):
        response = client.post(self.url, json=helm_template_sample_input)
        assert response.status_code == 200

    def test_helm_invalid_api(self, client, helm_template_invalid_sample_input):
        resource = client.post(self.url, json=helm_template_invalid_sample_input)
        assert resource.status_code == 422

    def test_helm_invalid_port(self, client, helm_template_invalid_sample_input):
        helm_template_invalid_sample_input['pods'][0]['target_port'] = 70000
        resource = client.post(self.url, json=helm_template_invalid_sample_input)
        assert resource.status_code == 422
