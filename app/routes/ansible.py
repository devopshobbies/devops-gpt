from app.app_instance import app
from app.gpt_services import gpt_service
from app.services import (write_installation,edit_directory_generator,execute_pythonfile)
from app.models import (AnsibleInstall,Output)
from app.template_generators.ansible.install.main import ansible_install_template
import os

@app.post("/ansible-install/")
async def ansible_install_generation(request:AnsibleInstall) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = ansible_install_template(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("ansible_generator",output)
        execute_pythonfile("MyAnsible","ansible_generator")
        return Output(output='output')