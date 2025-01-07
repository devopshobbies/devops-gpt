from app.app_instance import app
from app.gpt_services import gpt_service
from fastapi.responses import FileResponse
from app.services import (
        
        edit_directory_generator,execute_pythonfile)
from app.models import (IaCBasicInput,
        IaCBugfixInput, 
        Output,
        IaCInstallationInput,
        IaCTemplateGenerationDocker,
        IaCTemplateGenerationEC2,
        IaCTemplateGenerationS3,
        IaCTemplateGenerationIAM,
        IaCTemplateGenerationArgoCD,
        IaCTemplateGenerationELB,
        IaCTemplateGenerationEFS,
        IaCTemplateGenerationALB,
        IaCTemplateGenerationCloudFront,
        IaCTemplateGenerationSNS,
        IaCTemplateGenerationAutoScaling
       )

from fastapi import Response

from app.prompt_generators import (IaC_basics_generator, 
        IaC_bugfix_generator,
        IaC_installation_generator, 
       )
from app.template_generators.terraform.docker import (IaC_template_generator_docker)
from app.template_generators.terraform.aws.ec2 import (IaC_template_generator_ec2)
from app.template_generators.terraform.aws.IAM import (IaC_template_generator_iam)
from app.template_generators.terraform.aws.s3 import (IaC_template_generator_s3)
from app.template_generators.terraform.argocd import (IaC_template_generator_argocd)
from app.template_generators.terraform.aws.ELB import (IaC_template_generator_elb)
from app.template_generators.terraform.aws.EFS import (IaC_template_generator_efs)
from app.template_generators.terraform.aws.ALB import (IaC_template_generator_alb)
from app.template_generators.terraform.aws.CloudFront import (IaC_template_generator_cloudfront)
from app.template_generators.terraform.aws.SNS import (IaC_template_generator_sns)
from app.template_generators.terraform.aws.AutoScaling import (IaC_template_generator_autoscaling)
from app.template_generators.terraform.Installation.main import (select_install)
import os

@app.post("/api/IaC-basic/")
async def IaC_basic_generation(request:IaCBasicInput) -> Output:
        if os.environ.get("TEST"):
            return Output(output='Terraform developed by hashicorp and it is very usefull')
        generated_prompt = IaC_basics_generator(request)
        output = gpt_service(generated_prompt,request.token)
        return Output(output=output)
   
@app.post("/api/IaC-bugfix/")
async def IaC_bugfix_generation(request:IaCBugfixInput) -> Output:
        if os.environ.get("TEST"):
            return Output(output='fix this bug by adding x to the y')
        generated_prompt = IaC_bugfix_generator(request)
        output = gpt_service(generated_prompt,request.token)
        return Output(output=output)


@app.post("/api/IaC-install/")
async def IaC_install_generation(request:IaCInstallationInput) -> Output:
        if os.environ.get("TEST"):
            return Output(output='nothing special')
        select_install(request)   
        return Output(output="pk")

@app.post("/api/IaC-template/docker")
async def IaC_template_generation_docker(request:IaCTemplateGenerationDocker) -> Output:
        
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_docker(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")

@app.post("/api/IaC-template/aws/ec2")
async def IaC_template_generation_aws_ec2(request:IaCTemplateGenerationEC2) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_ec2(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")


@app.post("/api/IaC-template/aws/s3")
async def IaC_template_generation_aws_s3(request:IaCTemplateGenerationS3) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_s3(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")


@app.post("/api/IaC-template/aws/iam")
async def IaC_template_generation_aws_iam(request:IaCTemplateGenerationIAM) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_iam(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")



@app.post("/api/IaC-template/argocd")
async def IaC_template_generation_argocd(request:IaCTemplateGenerationArgoCD) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_argocd(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")



@app.post("/api/IaC-template/aws/elb")
async def IaC_template_generation_aws_elb(request:IaCTemplateGenerationELB) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_elb(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")


@app.post("/api/IaC-template/aws/efs")
async def IaC_template_generation_aws_efs(request:IaCTemplateGenerationEFS) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_efs(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")


@app.post("/api/IaC-template/aws/alb")
async def IaC_template_generation_aws_alb(request:IaCTemplateGenerationALB) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_alb(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")


@app.post("/api/IaC-template/aws/cloudfront")
async def IaC_template_generation_aws_cloudfront(request:IaCTemplateGenerationCloudFront) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_cloudfront(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")


@app.post("/api/IaC-template/aws/sns")
async def IaC_template_generation_aws_sns(request:IaCTemplateGenerationSNS) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_sns(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")


@app.post("/api/IaC-template/aws/autoscaling")
async def IaC_template_generation_aws_autoscaling(request:IaCTemplateGenerationAutoScaling) -> Output:
         
        dir = 'app/media/terraform.tfvars'
        
        file_response = IaC_template_generator_autoscaling(request)
        with open(dir,'w')as f:
            f.write(file_response)
        
        return FileResponse(dir, media_type='application/zip', filename=f"terraform.tfvars")

