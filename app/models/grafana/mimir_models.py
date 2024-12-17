from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError



class MultiTenancy(BaseModel):
    tenant_name:str = "pods"
    
class MimirInput(BaseModel):
    name:str = "Mimir"
    uid:str = "mimir"
    url:str = "http://mimir-nginx.mimir.svc.cluster.local/prometheus"
    editable: bool = True
    httpHeaderName1:str = "X-Scope-OrgID"
    alertmanagerUid:str = "alertmanager"
    multi_tenancy:Optional[MultiTenancy]
    
   
