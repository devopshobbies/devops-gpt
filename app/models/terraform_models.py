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

class IaCTemplateGenerationDocker(BaseModel):
    docker_image: bool = True
    docker_container: bool = True

class IaCTemplateGenerationEC2(BaseModel):
    key_pair:bool = True
    security_group:bool = True
    aws_instance:bool = True
    ami_from_instance:bool = True

class IaCTemplateGenerationS3(BaseModel):
    s3_bucket:bool = True
    bucket_versioning:bool = True

class IaCTemplateGenerationIAM(BaseModel):
    iam_user:bool = True
    iam_group:bool = True

class SyncPolicy(BaseModel):
    auto_prune: bool = True
    self_heal: bool = True


class ArgoApplication(BaseModel):
    sync_policy: SyncPolicy | None = None
   

class IaCTemplateGenerationArgoCD(BaseModel):
    argocd_application:ArgoApplication | None = None
    argocd_repository:bool = True
    application_depends_repository:bool = True
   

class IaCTemplateGenerationELB(BaseModel):
    security_group:bool = True
    lb_target_group:bool = True
    lb:bool = True
    lb_listener:bool = True
    lb_listener_rule:bool = True
    key_pair:bool = True
    launch_configuration:bool = True
    autoscaling_group:bool = True
    autoscaling_attachment:bool = True
    autoscaling_policy:bool = True



class IaCTemplateGenerationEFS(BaseModel):
    
    efs_file_system:bool = True
    efs_mount_target:bool = True
    efs_backup_policy:bool = True
    