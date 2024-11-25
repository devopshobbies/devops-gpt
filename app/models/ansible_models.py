from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError


class AnsibleToolInstall(BaseModel):
    tool:str = 'nginx'
    
    @validator("tool")
    def validate_tool(cls, value):
        allowed_tools = ['nginx']
        if not value in allowed_tools :
            raise ValueError(f"Tool must be one of {allowed_tools}.")
        return value