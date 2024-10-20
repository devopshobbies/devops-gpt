from pydantic import BaseModel

class IaCInput(BaseModel):
    input:str
    max_tokens:int
    min_tokens:int
    service:str

class IaCOutput(BaseModel):
    output:str
