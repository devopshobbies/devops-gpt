from unittest.mock import MagicMock, patch, mock_open


class TestIaCTemplates:
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

        self.iac_template_docker_url = '/api/IaC-template/docker'
        self.iac_template_ec2_url = '/api/IaC-template/aws/ec2'
        self.iac_template_s3_url = '/api/IaC-template/aws/s3'
        self.iac_template_iam_url = '/api/IaC-template/aws/iam'
        self.iac_template_argocd_url = '/api/IaC-template/argocd'
        self.iac_template_elb_url = '/api/IaC-template/aws/elb'
        self.iac_template_efs_url = '/api/IaC-template/aws/efs'

    def teardown_method(self):
        patch.stopall()

    def test_iac_template_docker(self, client, iac_template_docker_sample_input):
        response = client.post(self.iac_template_docker_url, json=iac_template_docker_sample_input)
        assert response.status_code == 200

    def test_iac_template_ec2(self, client, iac_template_ec2_sample_input):
        response = client.post(self.iac_template_ec2_url, json=iac_template_ec2_sample_input)
        assert response.status_code == 200

    def test_iac_template_s3(self, client, iac_template_s3_sample_input):
        response = client.post(self.iac_template_s3_url, json=iac_template_s3_sample_input)
        assert response.status_code == 200

    def test_iac_template_iam(self, client, iac_template_iam_sample_input):
        response = client.post(self.iac_template_iam_url, json=iac_template_iam_sample_input)
        assert response.status_code == 200

    def test_iac_template_argocd(self, client, iac_template_argocd_sample_input):
        response = client.post(self.iac_template_argocd_url, json=iac_template_argocd_sample_input)
        assert response.status_code == 200

    def test_iac_template_elb(self, client, iac_template_elb_sample_input):
        response = client.post(self.iac_template_elb_url, json=iac_template_elb_sample_input)
        assert response.status_code == 200

    def test_iac_template_efs(self, client, iac_template_efs_sample_input):
        response = client.post(self.iac_template_efs_url, json=iac_template_efs_sample_input)
        assert response.status_code == 200
