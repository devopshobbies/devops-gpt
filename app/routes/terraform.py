from app.app_instance import app
from app.gpt_services import gpt_service
from app.services import (
        write_installation,
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
        IaCTemplateGenerationEFS
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
import os

@app.post("/api/IaC-basic/")
async def IaC_basic_generation(request:IaCBasicInput) -> Output:
        if os.environ.get("TEST"):
            return Output(output='Terraform developed by hashicorp and it is very usefull')
        generated_prompt = IaC_basics_generator(request)
        output = gpt_service(generated_prompt)
        return Output(output=output)
   
@app.post("/api/IaC-bugfix/")
async def IaC_bugfix_generation(request:IaCBugfixInput) -> Output:
        if os.environ.get("TEST"):
            return Output(output='fix this bug by adding x to the y')
        generated_prompt = IaC_bugfix_generator(request)
        output = gpt_service(generated_prompt)
        return Output(output=output)


@app.post("/api/IaC-install/")
async def IaC_install_generation(request:IaCInstallationInput) -> Output:
        if os.environ.get("TEST"):
            return Output(output='apt-get install xyz \n apt-get update (covert them to shell file output)')
        generated_prompt = IaC_installation_generator(request)
        output = gpt_service(generated_prompt)
        return Output(output=output)

@app.post("/api/IaC-template/docker")
async def IaC_template_generation_docker(request:IaCTemplateGenerationDocker) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output (nothing special)')
        generated_prompt = IaC_template_generator_docker(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')

@app.post("/api/IaC-template/aws/ec2")
async def IaC_template_generation_aws_ec2(request:IaCTemplateGenerationEC2) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output (nothing special)')

        generated_prompt = IaC_template_generator_ec2(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')

@app.post("/api/IaC-template/aws/s3")
async def IaC_template_generation_aws_s3(request:IaCTemplateGenerationS3) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output (nothing special)')
        generated_prompt = IaC_template_generator_s3(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')

@app.post("/api/IaC-template/aws/iam")
async def IaC_template_generation_aws_iam(request:IaCTemplateGenerationIAM) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output (nothing special)')
        generated_prompt = IaC_template_generator_iam(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')


@app.post("/api/IaC-template/argocd")
async def IaC_template_generation_argocd(request:IaCTemplateGenerationArgoCD) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output (nothing special)')
        generated_prompt = IaC_template_generator_argocd(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')



@app.post("/api/IaC-template/aws/elb")
async def IaC_template_generation_aws_elb(request:IaCTemplateGenerationELB) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output (nothing special)')
        generated_prompt = IaC_template_generator_elb(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')

@app.post("/api/IaC-template/aws/efs")
async def IaC_template_generation_aws_efs(request:IaCTemplateGenerationEFS) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output (nothing special)')
        generated_prompt = IaC_template_generator_efs(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')
