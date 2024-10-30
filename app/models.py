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

class IaCInstallationInput(BaseModel):
    os:str = "ubuntu"
    service:Optional[str] = 'terraform'

class IaCTemplateGeneration(BaseModel):
    CI_integration:bool = True
    base_config:str = 'ec2'
    service:str = 'terraform'

class HelmTemplateGeneration(BaseModel):
    CI_integration:bool = True
    api_version:int = 1
    templates:list[str]
    images:list[str]


    


class Output(BaseModel):
    output:str
