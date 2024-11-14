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
       )

from fastapi import Response

from app.prompt_generators import (IaC_basics_generator, 
        IaC_bugfix_generator,
        IaC_installation_generator, 
       )
from app.template_generators.terraform.docker import (IaC_template_generator_docker)


@app.post("/IaC-basic/")
async def IaC_basic_generation(request:IaCBasicInput) -> Output:

        generated_prompt = IaC_basics_generator(request)
        output = gpt_service(generated_prompt)
        return Output(output=output)
   
@app.post("/IaC-bugfix/")
async def IaC_bugfix_generation(request:IaCBugfixInput) -> Output:

        generated_prompt = IaC_bugfix_generator(request)
        output = gpt_service(generated_prompt)
        return Output(output=output)


@app.post("/IaC-install/")
async def IaC_install_generation(request:IaCInstallationInput) -> Output:

        generated_prompt = IaC_installation_generator(request)
        output = gpt_service(generated_prompt)
        return Output(output=output)

@app.post("/IaC-template/docker")
async def IaC_template_generation_docker(request:IaCTemplateGenerationDocker) -> Output:

        generated_prompt = IaC_template_generator_docker(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')

@app.post("/IaC-template/aws/ec2")
async def IaC_template_generation_aws_ec2(request:IaCTemplateGenerationEC2) -> Output:

        generated_prompt = IaC_template_generator_docker(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')

@app.post("/IaC-template/aws/s3")
async def IaC_template_generation_aws_s3(request:IaCTemplateGenerationS3) -> Output:

        generated_prompt = IaC_template_generator_docker(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')

@app.post("/IaC-template/aws/iam")
async def IaC_template_generation_aws_iam(request:IaCTemplateGenerationIAM) -> Output:

        generated_prompt = IaC_template_generator_docker(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("terraform_generator",output)
        execute_pythonfile("MyTerraform","terraform_generator")
        return Output(output='output')


