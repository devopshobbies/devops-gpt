from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError

class BasicAuth(BaseModel):
    basicAuthUser:str
    basicAuthPassword:str
    
        
class AlertManagerInput(BaseModel):
    implementation:str
    handleGrafanaManagedAlerts:bool = True
    editable: bool = True
    basic_auth:Optional[BasicAuth]
    
    @validator("implementation")
    def validator_implementation(cls,value):
        valid = ['prometheus','cortex','mimir']
        if value not in valid:
            raise ValueError(f"implementation must be in {valid}")
        return value
    
   
    
   
