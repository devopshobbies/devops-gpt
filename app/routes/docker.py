from app.app_instance import app
from app.gpt_services import gpt_service
from app.services import (write_installation,edit_directory_generator,execute_pythonfile)
from app.models import (DockerCompose,Output)
from app.template_generators.docker.compose import docker_compose_generator
import os

@app.post("/docker-compose/")
async def docker_compose_template(request:DockerCompose) -> Output:
    
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = docker_compose_generator(request)

        output = gpt_service(generated_prompt)
        edit_directory_generator("compose_generator",output)
        execute_pythonfile("MyCompose","compose_generator")
        return Output(output='output')
    