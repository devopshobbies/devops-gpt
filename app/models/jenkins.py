from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError


    
class JenkinsInstallation(BaseModel):

    os: str | None = 'Ubuntu'
    
    environment:str = 'Linux'
    
    @validator("os")
    def validator_os(cls, value):
        valid_oss = ['Ubuntu','Fedora','RHEL']
        if value not in valid_oss:
            raise ValueError(f"your selected OS must be in {valid_oss}")
        return value
    
    @validator("environment")
    def validator_environment(cls, value):
        env = ['Linux','Docker']
        if value not in env:
            raise ValueError(f"your selected Environemnt must be in {env}")
        return value