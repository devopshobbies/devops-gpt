from app.app_instance import app
from app.models import (DockerCompose,DockerInstallationInput,Output)
from app.template_generators.docker.compose import docker_compose_generator
from app.template_generators.docker.installation import docker_installation_selection
import os

@app.post("/api/docker-compose/")
async def docker_compose_template(request:DockerCompose) -> Output:
    
        if os.environ.get("TEST"):
            return Output(output='output')
        docker_compose_generator(request)

        return Output(output='output')
    
    
@app.post("/api/docker/installation")
async def docker_installation(request:DockerInstallationInput) -> Output:
        
        docker_installation_selection(request)

        return Output(output='output')