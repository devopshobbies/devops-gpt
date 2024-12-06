from typing import Dict, List, Optional,Union
from pydantic import BaseModel, model_validator

class Build(BaseModel):
    context: str = "."
    dockerfile: str = "DockerFile"
    args: Optional[Dict[str, str]] = {"foo":"bar"}
class Service(BaseModel):
    build: Optional[Build] = Build()
    image: Optional[str] = "nginx:latest"
    container_name: Optional[str] = "web_server"
    command: Optional[str] = "command..."
    volumes: Optional[List[str]] = ["./foo:bar"]
    environment: Optional[Dict[str, str]] = {"foo":"bar"}
    ports: Optional[List[str]] = ["80:80"]
    networks: Optional[List[str]] = ["app_network"]
    
    depends_on: Optional[List[str]] = ['service 0']

    @model_validator(mode="after")
    def validator(self):
        if self.build == None and self.image == None:
            raise ValueError(f"one of the build or image sections must be present!")
        return self
    
class Network(BaseModel):
    driver: str = "bridge"

class PreCreatedNetwork(BaseModel):
    name:str = "net1"
    external:bool = True
class DockerCompose(BaseModel):
    version: str = "3"
    services: Dict[str, Service] = {"web":Service(), "web2":Service()}
    networks: Union[Optional[Dict[str, PreCreatedNetwork]],Optional[Dict[str, Network]]] = {"app_network": {"driver":"bridge"}}

