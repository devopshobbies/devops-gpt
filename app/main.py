from fastapi import FastAPI
from .gpt_services import gpt_service_IaC
from .models import IaCInput, IaCOutput
from fastapi import Response
app = FastAPI()


@app.post("/IaC-text-gen/")
async def IaC_text_generation(request:IaCInput) -> IaCOutput:
   
        output = gpt_service_IaC(request.input, request.service,request.max_tokens,request.min_tokens)
        
        return IaCOutput(output=output)
   
