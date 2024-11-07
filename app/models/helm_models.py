from pydantic import BaseModel
from typing import List, Optional

class Persistance(BaseModel):
    size:str = "1Gi"
    accessModes:str = "ReadWriteOnce"

class Environment(BaseModel):
    name:str = "ENV1"
    value:str = "VALUE1"

class Ingress(BaseModel):
    enabled:bool = False
    host:str = "www.example.com"

class Pod(BaseModel):
    name:str = "web"
    image:str = "nginx"
    target_port:int = 80
    replicas: int = 1
    persistance: Persistance
    environment: List[Environment]
    stateless:bool = True
    ingress: Ingress

class HelmTemplateGeneration(BaseModel):
    api_version:int = 2
    pods:List[Pod]
    
