from app.app_instance import app
from app.gpt_services import gpt_service
from app.services import (
        write_installation,
        edit_directory_generator,execute_pythonfile)
from app.models import (AnsibleToolInstall,Output)
from app.template_generators.ansible.installation_tool import ansible_tool_install
from fastapi import Response

import os

@app.post("/ansible-install-tool/")
async def Ansible_install_generation(request:AnsibleToolInstall) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = ansible_tool_install(request)
        output = gpt_service(generated_prompt)
        return Output(output=output)
   
