from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError


        
class ElasticSearchInput(BaseModel):
    name:str = "elasticsearch-v7-filebeat"
    url:str = "http://localhost:9200" 
    editable: bool = True
    index:str = "[filebeat-]YYYY.MM.DD"
    interval:str = "Daily"
    timeField:str = "@timestamp"
    logMessageField:str = "message"
    logLevelField:str = "fields.level"
    
    
    
    
   
    
   