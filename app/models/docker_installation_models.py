from typing import Dict, List, Optional,Union
from pydantic import BaseModel, model_validator,validator

class DockerInstallationInput(BaseModel):
    os:str = "Ubuntu"
    environment:str = "Linux"
    
    @validator("os")
    def validate_os(cls, value):
        allowed_os = ['Ubuntu', 'Centos', 'Fedora', 'RHEL']
        if value not in allowed_os:
            raise ValueError(f"OS must be one of {allowed_os}.")
        return value
    
    @validator("environment")
    def validate_environment(cls, value):
        allowed_os = ['Linux']
        if value not in allowed_os:
            raise ValueError(f"Environment must be one of {allowed_os}.")
        return value