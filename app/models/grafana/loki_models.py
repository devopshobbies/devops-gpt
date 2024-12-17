from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError

class BasicAuth(BaseModel):
    basicAuthUser:str
    basicAuthPassword:str
       
class LokiInput(BaseModel):
    name:str = "Loki"
    uid:str = "loki"
    url:str = "http://localhost:3100"
    editable: bool = True
    timeout:int = 60
    maxLines:int = 1000
    basic_auth:Optional[BasicAuth]
    
    
    
    
    