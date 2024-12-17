from typing import Optional, List
from pydantic import BaseModel,PrivateAttr,Field

class TracesToLogsV2(BaseModel):
    datasourceUid: str = 'loki'
    spanStartTimeShift: str = '-2m'
    spanEndTimeShift: str = '2m'
    filterByTraceID: bool = True
    filterBySpanID: bool = True

class ServiceMap(BaseModel):
    datasourceUid: str = 'Mimir-OtelMetrics-Tenant'

class NodeGraph(BaseModel):
    enabled: bool = True

class JsonData(BaseModel):
    httpMethod: str = 'GET'
    tracesToLogsV2: Optional[TracesToLogsV2] = TracesToLogsV2()
    serviceMap: Optional[ServiceMap] = ServiceMap()
    nodeGraph: Optional[NodeGraph] = NodeGraph()

class Datasource(BaseModel):
    name: str = 'Tempo'
    type: str = Field(default='tempo')
    access: str = Field(default="proxy")
    orgId: int = Field(default=1)
    url: str = 'http://tempo-query-frontend.tempo.svc.cluster.local:3100'
    basicAuth: bool = False
    version: int = Field(default=1)
    editable: bool = True
    apiVersion: int = Field(default=1)
    uid: str = Field(default="tempo")
    jsonData: JsonData = JsonData()

class TempoInput(BaseModel):
    apiVersion: int = Field(default=1)
    datasources: List[Datasource] = [Datasource()]
  
