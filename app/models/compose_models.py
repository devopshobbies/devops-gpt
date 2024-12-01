from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError

class Port(BaseModel):
    machine_port:int = 80
    container_port:int = 80
    
class Network(BaseModel):
    name:str = 'app_network'

class EnvironmentVariable(BaseModel):
    name:str = 'foo'
    value:str = "bar"
    
class Volume(BaseModel):
    local_dir: str = './nginx/nginx.conf'
    container_dir:str = '/etc/nginx/nginx.conf'
    
class Service(BaseModel):
    image:str = 'nginx'
    version:str = 'latest'
    volumes:List[Volume]
    depends_on:List[str]
    ports:List[Port]
    networks:List[Network]
    environments:List[EnvironmentVariable]
    
      
class DockerCompose(BaseModel):
    services: List[Service]
    network:Network
    