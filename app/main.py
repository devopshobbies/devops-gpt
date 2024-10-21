from fastapi import FastAPI
from .gpt_services import gpt_service_IaC
from .models import IaCInput, IaCOutput
from fastapi import Response
from .utils import save_QA_to_mongo

app = FastAPI()


@app.post("/IaC-text-gen/")
def IaC_text_generation(request:IaCInput) -> IaCOutput:
        
        output = gpt_service_IaC(request.input, request.service,request.max_tokens,request.min_tokens)
        save_QA_to_mongo(str(request.input),str(output))
        return IaCOutput(output=output)
   
