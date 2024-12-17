from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError,field_validator



class PrometheusInput(BaseModel):
    name:str = "Prometheus"
    url:str = "http://localhost:9090"
    editable: bool = True
    httpMethod:str = "POST"
    manageAlerts:bool = True
    prometheusType:str = "Prometheus"
    prometheusVersion:str = "2.44.0"
    cacheLevel:str = "High"
    disableRecordingRules:bool = False
    incrementalQueryOverlapWindow:str = "10m"
    