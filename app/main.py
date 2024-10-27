
from .gpt_services import gpt_service
from .services import (write_basic,
        write_bugfix,
        write_installation,
        edit_directory_generator,execute_pythonfile)
from .models import (IaCBasicInput,
        IaCBugfixInput, 
        Output,
        IaCInstallationInput,IaCTemplateGeneration)

from fastapi import FastAPI, HTTPException,Response
from fastapi.responses import FileResponse
from .prompt_generators import (IaC_basics_generator, 
        IaC_bugfix_generator,
        IaC_installation_generator, 
        IaC_template_generator)
import os
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
        edit_directory_generator(output)
        execute_pythonfile()
        return Output(output='output')


@app.get("/download/{filename}")
def download_file(filename: str):
    folder = "app/media/MyTerraform"  # specify your folder path here
    file_path = os.path.join(folder, filename)

    # Ensure the file exists
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found.")

    # Return the file response for download
    return FileResponse(file_path, media_type='application/octet-stream', filename=filename)

@app.get("/list-directory")
def list_directory(folder: str):
    # Ensure the folder exists
    if not os.path.isdir(folder):
        raise HTTPException(status_code=404, detail=f"{folder} does not exist.")

    # List the contents of the directory
    contents = os.listdir(folder)
    return {"folder": folder, "contents": contents}