from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError


    
class AnsibleInstallNginx(BaseModel):
    os: str = 'ubuntu'
    hosts:List[str] = ['www.example.com']
    version:str = 'latest'
    
    @validator("os")
    def validator_os(cls, value):
        if value not in ['ubuntu']:
            raise ValueError("Size must be a valid string ending with 'Gi', 'Mi', or 'Ti'.")
        return value