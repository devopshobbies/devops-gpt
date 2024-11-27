from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError


    
class AnsibleInstallNginx(BaseModel):

    os: str = 'ubuntu'
    hosts:List[str] = ['www.example.com']
    version:str = 'latest'
    
    @validator("os")
    def validator_os(cls, value):
        valid_oss = ['ubuntu']
        if value not in valid_oss:
            raise ValueError(f"your selected OS must be in {valid_oss}")
        return value
    
    
class AnsibleInstallDocker(BaseModel):
    os: str = 'ubuntu'
    hosts:List[str] = ['www.example.com']
    version:str = 'latest'
    
    @validator("os")
    def validator_os(cls, value):
        valid_oss = ['ubuntu']
        if value not in valid_oss:
            raise ValueError(f"your selected OS must be in {valid_oss}")
        return value