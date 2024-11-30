from .docker import ansible_docker_install
from .nginx import ansible_nginx_install
from .kuber import ansible_kuber_install
from fastapi import HTTPException

def ansible_install_template(input_, tool:str):
    
    match tool:
        
        case 'nginx':
            return ansible_nginx_install(input_)
        
        case 'docker':
            return ansible_docker_install(input_)
        
        case 'kuber':
            return ansible_kuber_install(input_)
        
        case _: 
            raise HTTPException(400,"please select a valid tool for installation")