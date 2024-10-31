from pydantic import BaseModel
from typing import List, Optional

from .utils import BasicInput


class IaCBasicInput(BasicInput):
    input:str
    service:Optional[str] = 'terraform'

class IaCBugfixInput(BasicInput):
    bug_description:str
    version:str = 'latest'
    service:Optional[str] = 'terraform'

class IaCInstallationInput(BaseModel):
    os:str = "ubuntu"
    service:Optional[str] = 'terraform'

class IaCTemplateGeneration(BaseModel):
    CI_integration:bool = True
    base_config:str = 'ec2'
    service:str = 'terraform'