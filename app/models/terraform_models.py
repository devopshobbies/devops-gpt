from pydantic import BaseModel, validator, ValidationError
from typing import List, Optional
from .utils import BasicInput


class IaCBasicInput(BasicInput):
    input:str
    token:str

    @validator("input")
    def validate_input(cls, value):
        if not value:
            raise ValueError("Input cannot be empty.")
        return value

    

class IaCBugfixInput(BasicInput):
    bug_description:str
    token:str

    @validator("bug_description")
    def validate_bug_description(cls, value):
        if not value:
            raise ValueError("Bug description cannot be empty.")
        return value

   

class IaCInstallationInput(BaseModel):
    os:str = "Ubuntu"
    environment:str = "Linux"
    
    @validator("os")
    def validate_os(cls, value):
        allowed_os = ['Ubuntu', 'Centos', 'Fedora', 'Amazon_linux']
        if value not in allowed_os:
            raise ValueError(f"OS must be one of {allowed_os}.")
        return value
    
    @validator("environment")
    def validate_environment(cls, value):
        allowed_os = ['Linux']
        if value not in allowed_os:
            raise ValueError(f"Environment must be one of {allowed_os}.")
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
    
class IaCTemplateGenerationALB(BaseModel):
    
    alb_resources:bool = True
    security_group:bool = True

class IaCTemplateGenerationCloudFront(BaseModel):
    
    distribution:bool = True
    origin_access_identity:bool = True
    origin_access_control:bool = False
    monitoring_subscription:bool = False
    vpc_origin:bool = False

class IaCTemplateGenerationSNS(BaseModel):
    
    sns_topic:bool = True
    fifo_topic:bool = False
    topic_policy:bool = True
    subscription:bool = True

class IaCTemplateGenerationAutoScaling(BaseModel):
    
    autoscaling_group:bool = True
    launch_template:bool = True
    schedule:bool = True
    scaling_policy:bool = True
    iam_instance_profile:bool = True
