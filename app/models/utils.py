from pydantic import BaseModel
from typing import List, Optional

class Output(BaseModel):
    output:str

class BasicInput(BaseModel):

    max_tokens:int = 500
    min_tokens:int = 100
    service:str