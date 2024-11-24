from unittest.mock import patch


class TestTerraformTemplates:
    def setup_method(self):
        self.mock_execute_pythonfile = patch('app.main.execute_pythonfile').start()
        self.mock_edit_directory_generator = patch('app.main.edit_directory_generator').start()
        self.mock_gpt_service = patch('app.main.gpt_service').start()
        self.mock_gpt_service.return_value = 'Generated Python Code'

        self.iac_template_docker_url = '/IaC-template/docker'
        self.iac_template_ec2_url = '/IaC-template/aws/ec2'
        self.iac_template_s3_url = '/IaC-template/aws/s3'
        self.iac_template_iam_url = '/IaC-template/aws/iam'
        self.iac_template_argocd_url = '/IaC-template/argocd'
        self.iac_template_elb_url = '/IaC-template/aws/elb'
        self.iac_template_efs_url = '/IaC-template/aws/efs'

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
