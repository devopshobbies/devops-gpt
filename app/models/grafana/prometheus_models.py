from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError


class TraceID(BaseModel):
    datasourceUid:str = "my_jaeger_uid"
    name:str = "traceID"
class PrometheusInput(BaseModel):
    name:str = "Prometheus"
    url:str = "http://localhost:9090"
    editable: bool = True
    httpMethod:str = "POST"
    manageAlerts:bool = True
    prometheusType:str = "Prometheus"
    prometheusVersion:str = "2.44.0"
    cacheLevel:str = 'High'
    disableRecordingRules:bool = False
    incrementalQueryOverlapWindow:str = "10m"
    trace_id: TraceID