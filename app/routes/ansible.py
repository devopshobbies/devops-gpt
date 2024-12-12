from app.app_instance import app
from app.gpt_services import gpt_service
from app.services import (write_installation,edit_directory_generator,execute_pythonfile)
from app.routes.utils import add_files_to_folder
from app.models import (AnsibleInstallNginx,AnsibleInstallDocker,Output,AnsibleInstallKuber)

from app.models import (AnsibleInstallNginx,Output)

from app.template_generators.ansible.install.main import ansible_install_template
import os

@app.post("/api/ansible-install/nginx/")
async def ansible_install_generation_nginx(request:AnsibleInstallNginx) -> Output:
    
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = ansible_install_template(request,"nginx")

        
        return Output(output='output')
    
    
@app.post("/api/ansible-install/docker/")
async def ansible_install_generation_docker(request:AnsibleInstallDocker) -> Output:
    
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = ansible_install_template(request,"docker")

        output = gpt_service(generated_prompt)
        edit_directory_generator("ansible_generator",output)
        execute_pythonfile("MyAnsible","ansible_generator")
        return Output(output='output')
    
    
@app.post("/api/ansible-install/kuber/")
async def ansible_install_generation_kuber(request:AnsibleInstallKuber) -> Output:
    
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = ansible_install_template(request,"kuber")

        output = gpt_service(generated_prompt)
        edit_directory_generator("ansible_generator",output)
        execute_pythonfile("MyAnsible","ansible_generator")
        add_files_to_folder(files = ['app/media/kuber_configs/resolv.conf.j2'] , folder='app/media/MyAnsible/roles/preinstall/templates/')
        add_files_to_folder(files = ['app/media/kuber_configs/kubeadmcnf.yml.j2'] , folder='app/media/MyAnsible/roles/init_k8s/templates/')
        add_files_to_folder(files = ['app/media/kuber_configs/kubeadmcnf-join.yml.j2'] , folder='app/media/MyAnsible/roles/join_master/templates/')
       
        
        return Output(output='output')