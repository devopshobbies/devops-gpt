from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError, computed_field

class Port(BaseModel):
    machine_port:int = 80
    container_port:int = 80
    
class Network(BaseModel):
    name:str = 'app_network'

class EnvironmentVariable(BaseModel):
    name:str = 'foo'
    value:str = "bar"
    
    @computed_field
    @property
    def env_full(self) -> int:
        return f"{self.name}:{self.value}"
    
class Volume(BaseModel):
    local_dir: str = './nginx/nginx.conf'
    container_dir:str = '/etc/nginx/nginx.conf'
    
    @computed_field
    @property
    def volume(self) -> int:
        return f"{self.local_dir}:{self.container_dir}"

class Build(BaseModel):
    context:str
    dockerfile:str
class Service(BaseModel):
    image:str = 'nginx'
    name:str = 'web_server'
    container_name:str = 'web_server'
    build: Build | None = None
    version:str = 'latest'
    volumes:List[Volume] | None = None
    depends_on:List[str] | None = None
    ports:List[Port]
    networks:List[Network] | None = None
    environments:List[EnvironmentVariable] | None = None
    
    @computed_field
    @property
    def image_full(self) -> int:
        return f"{self.image}:{self.version}"
    
    @computed_field
    @property
    def volumes_full(self) -> int:
        return [i.volume for i in self.volumes]
    
    
      
class DockerCompose(BaseModel):
    services: List[Service]
    network:Network
    