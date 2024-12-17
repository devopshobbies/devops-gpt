from typing import List, Optional
from pydantic import BaseModel, validator, ValidationError



        
class PostgresInput(BaseModel):
    name:str = "Postgres"
    url:str = "localhost:5432"
    user:str = "grafana"
    editable: bool = True
    database:str = "grafana"
    sslmode:str = "disable"
    password:str = "Password!"
    maxOpenConns:int = 100 
    maxIdleConns:int = 100
    maxIdleConnsAuto:bool = True 
    connMaxLifetime:int = 14400 
    postgresVersion:int = 903
    timescaledb:bool = False
    
    