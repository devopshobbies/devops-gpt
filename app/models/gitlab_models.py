from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError


    
class GitLabInstallation(BaseModel):

    
    environment:str = 'Docker'
    
    
    @validator("environment")
    def validator_environment(cls, value):
        env = ['Docker']
        if value not in env:
            raise ValueError(f"your selected Environemnt must be in {env}")
        return value