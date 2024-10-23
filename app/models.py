from pydantic import BaseModel
from typing import Optional


class BasicInput(BaseModel):

    max_tokens:int = 500
    min_tokens:int = 100
    service:str

class IaCBasicInput(BasicInput):
    input:str
    service:Optional[str] = 'terraform'

class IaCBugfixInput(BasicInput):
    bug_description:str
    version:str = 'latest'
    service:Optional[str] = 'terraform'

class IaCInstallationInput(BasicInput):
    os:str = "ubuntu"
    service:Optional[str] = 'terraform'

class IaCTemplateGeneration(BasicInput):
    CI_integration:bool = True

class Output(BaseModel):
    output:str
