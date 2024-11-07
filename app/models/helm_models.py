from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError

class Persistance(BaseModel):
    size: str = "1Gi"
    accessModes: str = "ReadWriteOnce"
    
    @validator("size")
    def validate_size(cls, value):
        
        if not isinstance(value, str) or not value.endswith(('Gi', 'Mi', 'Ti')) or value[:-2].isdigit() == False:
            raise ValueError("Size must be a valid string ending with 'Gi', 'Mi', or 'Ti'.")
        return value

    @validator("accessModes")
    def validate_access_modes(cls, value):
        allowed_modes = ['ReadWriteOnce', 'ReadOnlyMany', 'ReadWriteMany']
        if value not in allowed_modes:
            raise ValueError(f"Access mode must be one of {allowed_modes}.")
        return value

class Environment(BaseModel):
    name: str = "ENV1"
    value: str = "Hi"
    
    @validator("name")
    def validate_name(cls, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        return value

    @validator("value")
    def validate_value(cls, value):
        if not value:
            raise ValueError("Value cannot be empty.")
        return value

class Ingress(BaseModel):
    enabled: bool = False
    host: str = "www.example.com"
    
    @validator("host")
    def validate_host(cls, value):
        if not value:
            raise ValueError("Host cannot be empty.")
        if not isinstance(value, str):
            raise ValueError("Host must be a string.")
        return value

class Pod(BaseModel):
    name: str = "web"
    image: str = "nginx"
    target_port: int = 80
    replicas: int = 1
    persistance: Persistance
    environment: List[Environment]
    stateless: bool = True
    ingress: Ingress
    
    @validator("name")
    def validate_name(cls, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        return value

    @validator("image")
    def validate_image(cls, value):
        if not value:
            raise ValueError("Image cannot be empty.")
        return value
    
    @validator("target_port")
    def validate_target_port(cls, value):
        if value <= 0 or value > 65535:
            raise ValueError("Target port must be between 1 and 65535.")
        return value

    @validator("replicas")
    def validate_replicas(cls, value):
        if value < 1:
            raise ValueError("Replicas must be at least 1.")
        return value

class HelmTemplateGeneration(BaseModel):
    api_version: int = 2
    pods: List[Pod]
    
    @validator("api_version")
    def validate_api_version(cls, value):
        if value < 1:
            raise ValueError("API version must be a positive integer.")
        return value

    @validator("pods", each_item=True)
    def validate_pods(cls, value):
        if not isinstance(value, Pod):
            raise ValueError("Each item in pods must be a Pod instance.")
        return value