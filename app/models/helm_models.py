from pydantic import BaseModel
from typing import List, Optional

class Pod(BaseModel):
    name:str
    image:str
    target_port:int

class HelmTemplateGeneration(BaseModel):
    api_version:int = 1
    pods:List[Pod]
    
