from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError

class AnsibleBase(BaseModel):
    ansible_user:str = 'root'
    ansible_port:int = 22
    
class AnsibleInstallNginx(AnsibleBase):

    os: str = 'ubuntu'
    hosts:List[str] = ['www.example.com']
    version:str = 'latest'
    
    @validator("os")
    def validator_os(cls, value):
        valid_oss = ['ubuntu']
        if value not in valid_oss:
            raise ValueError(f"your selected OS must be in {valid_oss}")
        return value
    
    
class AnsibleInstallDocker(AnsibleBase):
    os: str = 'ubuntu'
    hosts:List[str] = ['www.example.com']
    
    
    @validator("os")
    def validator_os(cls, value):
        valid_oss = ['ubuntu']
        if value not in valid_oss:
            raise ValueError(f"your selected OS must be in {valid_oss}")
        return value
    
    
   
class AnsibleInstallKuber(AnsibleBase):
    os: str = 'ubuntu'
    k8s_worker_nodes: List[str]
    k8s_master_nodes: List[str]
    version:str = "1.31"
    
    
    @validator("os")
    def validator_os(cls, value):
        valid_oss = ['ubuntu']
        if value not in valid_oss:
            raise ValueError(f"your selected OS must be in {valid_oss}")
        return value
    