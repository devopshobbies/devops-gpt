from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError

 

class TLS(BaseModel):
        tlsClientCert:str = "${GRAFANA_TLS_CLIENT_CERT}"
        tlsCACert:str =  "${GRAFANA_TLS_CA_CERT}"
        tlsAuth:bool =  True
        tlsSkipVerify:bool = True
        
class MysqlInput(BaseModel):
    name:str = "MySQL"
    url:str = " localhost:3306"
    user:str = "grafana"
    editable: bool = True
    database:str = "grafana"
    maxOpenConns:int = 100
    maxIdleConns:int = 100
    maxIdleConnsAuto:bool = True 
    connMaxLifetime:int = 14400 
    password:str = "${GRAFANA_MYSQL_PASSWORD}"
    tls :Optional[TLS]
    
    