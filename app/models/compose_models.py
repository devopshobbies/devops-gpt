from typing import Dict, List, Optional
from pydantic import BaseModel

class Build(BaseModel):
    context: str
    dockerfile: str

class Service(BaseModel):
    build: Optional[Build] = None
    image: Optional[str] = None
    container_name: Optional[str] = None
    command: Optional[str] = None
    volumes: Optional[List[str]] = None
    environment: Optional[Dict[str, str]] = None
    ports: Optional[List[str]] = None
    networks: Optional[List[str]] = None
    args: Optional[Dict[str, str]] = None
    depends_on: Optional[List[str]] = None

class Network(BaseModel):
    driver: str

class DockerCompose(BaseModel):
    version: str
    services: Dict[str, Service]
    networks: Optional[Dict[str, Network]] = None

