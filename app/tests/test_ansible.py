from unittest.mock import MagicMock, patch, mock_open

class TestAnsibleInstall:
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
        self.mock_os_makedirs = patch('os.makedirs').start()
        self.mock_os_path_join = patch('os.path.join', side_effect=lambda *args: '/'.join(args)).start()
        self.mock_shutil_copy = patch('shutil.copy').start()
        self.mock_shutil_rmtree = patch('shutil.rmtree').start()

        self.ansible_nginx_url = '/api/ansible-install/nginx/'
        self.ansible_docker_url = '/api/ansible-install/docker/'
        self.ansible_kuber_url = '/api/ansible-install/kuber/'

    def test_ansible_nginx_input(self, client, ansible_nginx_sample_input):
        response = client.post(self.ansible_nginx_url, json=ansible_nginx_sample_input)
        assert response.status_code == 200

    def test_ansible_nginx_invalid_input(self, client, ansible_nginx_invalid_sample_input):
        response = client.post(self.ansible_nginx_url, json=ansible_nginx_invalid_sample_input)
        assert response.status_code == 422

    def test_ansible_docker_input(self, client, ansible_docker_sample_input):
        response = client.post(self.ansible_docker_url, json=ansible_docker_sample_input)
        assert response.status_code == 200

    def test_ansible_docker_invalid_input(self, client, ansible_docker_invalid_sample_input):
        response = client.post(self.ansible_docker_url, json=ansible_docker_invalid_sample_input)
        assert response.status_code == 422

    def test_ansible_kuber_input(self, client, ansible_kuber_sample_input):
        response = client.post(self.ansible_kuber_url, json=ansible_kuber_sample_input)
        assert response.status_code == 200

    def test_ansible_kuber_invalid_input(self, client, ansible_kuber_invalid_sample_input):
        response = client.post(self.ansible_kuber_url, json=ansible_kuber_invalid_sample_input)
        assert response.status_code == 422
