from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError

class AnsibleInstall(BaseModel):
    os: str = 'ubuntu'
    tool: str = 'nginx'