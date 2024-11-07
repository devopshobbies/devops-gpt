from pydantic import BaseModel, validator, ValidationError
from typing import List, Optional

class Output(BaseModel):
    output:str

class BasicInput(BaseModel):

    max_tokens:int = 500
    min_tokens:int = 100
    service:str

    @validator("max_tokens")
    def validate_max_tokens(cls, value):
        if value <= 0:
            raise ValueError("max_tokens must be a positive integer.")
        return value

    @validator("min_tokens")
    def validate_min_tokens(cls, value, values):
        if value <= 0:
            raise ValueError("min_tokens must be a positive integer.")
            
        
        max_tokens = values.get('max_tokens')
        if max_tokens is not None and value > max_tokens:
            raise ValueError("min_tokens cannot be greater than max_tokens.")
        return value

    @validator("service")
    def validate_service(cls, value):
        if not value:
            raise ValueError("service cannot be empty.")
        if not isinstance(value, str):
            raise ValueError("service must be a string.")
        return value