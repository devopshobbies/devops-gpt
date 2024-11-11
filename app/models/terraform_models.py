from pydantic import BaseModel, validator, ValidationError
from typing import List, Optional

from .utils import BasicInput


class IaCBasicInput(BasicInput):
    input:str
    service:Optional[str] = 'terraform'

    @validator("input")
    def validate_input(cls, value):
        if not value:
            raise ValueError("Input cannot be empty.")
        return value

    @validator("service")
    def validate_service(cls, value):
        allowed_services = ['terraform']
        if value not in allowed_services:
            raise ValueError(f"Service must be one of {allowed_services}.")
        return value

class IaCBugfixInput(BasicInput):
    bug_description:str
    version:str = 'latest'
    service:Optional[str] = 'terraform'

    @validator("bug_description")
    def validate_bug_description(cls, value):
        if not value:
            raise ValueError("Bug description cannot be empty.")
        return value

    @validator("version")
    def validate_version(cls, value):
        if not value:
            raise ValueError("Version cannot be empty.")
        return value

    @validator("service")
    def validate_service(cls, value):
        allowed_services = ['terraform']
        if value not in allowed_services:
            raise ValueError(f"Service must be one of {allowed_services}.")
        return value

class IaCInstallationInput(BaseModel):
    os:str = "ubuntu"
    service:Optional[str] = 'terraform'

    @validator("os")
    def validate_os(cls, value):
        allowed_os = ['ubuntu', 'centos', 'debian']
        if value not in allowed_os:
            raise ValueError(f"OS must be one of {allowed_os}.")
        return value

    @validator("service")
    def validate_service(cls, value):
        allowed_services = ['terraform']
        if value not in allowed_services:
            raise ValueError(f"Service must be one of {allowed_services}.")
        return value

class IaCTemplateGeneration(BaseModel):
    CI_integration:bool = True
    base_config:str = 'ec2'
    service:str = 'terraform'

    @validator("base_config")
    def validate_base_config(cls, value):
        allowed_configs = ['ec2', 's3', 'rds','docker']
        if value not in allowed_configs:
            raise ValueError(f"Base config must be one of {allowed_configs}.")
        return value

    @validator("service")
    def validate_service(cls, value):
        allowed_services = ['terraform']
        if value not in allowed_services:
            raise ValueError(f"Service must be one of {allowed_services}.")
        return value