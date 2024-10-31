from pydantic import BaseModel
from typing import List, Optional

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

class Pod(BaseModel):
    name:str
    image:str
    target_port:int

class HelmTemplateGeneration(BaseModel):
    api_version:int = 1
    pods:List[Pod]
    

    


class Output(BaseModel):
    output:str
