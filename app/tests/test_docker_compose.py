

class TestDockerCompose:
    def setup_method(self):
        self.url = '/api/docker-compose/'

    def test_docker_compose_input(self, client, docker_compose_sample_input):
        response = client.post(self.url, json=docker_compose_sample_input)
        assert response.status_code == 200

    def test_docker_compose_invalid_input(self, client, docker_compose_invalid_sample_input):
        response = client.post(self.url, json=docker_compose_invalid_sample_input)
        assert response.status_code == 422
