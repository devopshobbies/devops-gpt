from app.app_instance import app
from app.gpt_services import gpt_service
from app.services import (edit_directory_generator,execute_pythonfile)
from app.models import (HelmTemplateGeneration,Output)
from app.prompt_generators import (helm_template_generator)
import os
@app.post("/api/Helm-template/")
async def Helm_template_generation(request:HelmTemplateGeneration) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = helm_template_generator(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("helm_generator",output)
        execute_pythonfile("MyHelm","helm_generator")
        return Output(output='output')