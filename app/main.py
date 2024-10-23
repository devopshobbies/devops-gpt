from fastapi import FastAPI
from .gpt_services import gpt_service
from .services import write_basic,write_bugfix,write_installation
from .models import (IaCBasicInput,
        IaCBugfixInput, 
        Output,
        IaCInstallationInput,IaCTemplateGeneration)
from fastapi import Response
from .prompt_generators import (IaC_basics_generator, 
        IaC_bugfix_generator,
        IaC_installation_generator, 
        IaC_template_generator)

app = FastAPI()


@app.post("/IaC-basic/")
async def IaC_basic_generation(request:IaCBasicInput) -> Output:

        generated_prompt = IaC_basics_generator(request)
        output = gpt_service(generated_prompt)
        write_basic(request,output)
        return Output(output=output)
   
@app.post("/IaC-bugfix/")
async def IaC_bugfix_generation(request:IaCBugfixInput) -> Output:

        generated_prompt = IaC_bugfix_generator(request)
        output = gpt_service(generated_prompt)
        write_bugfix(request,output)
        return Output(output=output)


@app.post("/IaC-install/")
async def IaC_install_generation(request:IaCInstallationInput) -> Output:

        generated_prompt = IaC_installation_generator(request)
        output = gpt_service(generated_prompt)
        write_installation(request,output)
        return Output(output=output)

@app.post("/IaC-template/")
async def IaC_template_generation(request:IaCTemplateGeneration) -> Output:

        generated_prompt = IaC_template_generator(request)
        output = gpt_service(generated_prompt)
        return Output(output=output)