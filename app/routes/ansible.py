from app.app_instance import app
from app.gpt_services import gpt_service
from app.services import (write_installation,edit_directory_generator,execute_pythonfile)
from app.models import (AnsibleInstallNginx,Output)
from app.template_generators.ansible.install.main import ansible_install_template
import os

@app.post("/ansible-install/nginx/")
async def ansible_install_generation_nginx(request:AnsibleInstallNginx) -> Output:
    
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = ansible_install_template(request,"nginx")
        output = gpt_service(generated_prompt)
        edit_directory_generator("ansible_generator",output)
        execute_pythonfile("MyAnsible","ansible_generator")
        return Output(output='output')