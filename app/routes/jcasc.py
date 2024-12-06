from app.app_instance import app
from app.gpt_services import gpt_service
from app.services import (write_installation,edit_directory_generator,execute_pythonfile)
from app.models import (Jcasc,Output)
from app.template_generators.jenkins.jcasc import jcasc_template_generator
import os

@app.post("/api/jcasc-template/")
async def jcasc_template_generation(request:Jcasc) -> Output:
        if os.environ.get("TEST"):
            return Output(output='output')
        generated_prompt = jcasc_template_generator(request)
        output = gpt_service(generated_prompt)
        edit_directory_generator("jcasc_generator",output)
        execute_pythonfile("MyJcasc","jcasc_generator")
        return Output(output='output')