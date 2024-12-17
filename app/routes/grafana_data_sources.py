from app.app_instance import app
from app.models import (AlertManagerInput,Output,ElasticSearchInput,LokiInput,MimirInput,MysqlInput)
from app.template_generators.grafana_data_sources.alertmanager import alert_manager_template
from app.template_generators.grafana_data_sources.elasticsearch import elasticsearch_template
from app.template_generators.grafana_data_sources.loki import loki_template
from app.template_generators.grafana_data_sources.mimir import mimir_template
from app.template_generators.grafana_data_sources.mysql import mysql_template
import shutil
import os

@app.post("/api/grafana/alertmanager")
async def alertmanager_template_route(request:AlertManagerInput) -> Output:
    
        dir = 'app/media/MyGrafana'
        if os.path.exists(dir):     
            shutil.rmtree(dir) 
            
        alert_manager_template(request)

        return Output(output='output')
    
@app.post("/api/grafana/elasticsearch")
async def elastic_template_route(request:ElasticSearchInput) -> Output:
    
        dir = 'app/media/MyGrafana'
        if os.path.exists(dir):     
            shutil.rmtree(dir) 
            
        elasticsearch_template(request)

        return Output(output='output')
    
@app.post("/api/grafana/loki")
async def loki_template_route(request:LokiInput) -> Output:
    
        dir = 'app/media/MyGrafana'
        if os.path.exists(dir):     
            shutil.rmtree(dir) 
            
        loki_template(request)

        return Output(output='output')
    
    
@app.post("/api/grafana/mimir")
async def mimir_template_route(request:MimirInput) -> Output:
    
        dir = 'app/media/MyGrafana'
        if os.path.exists(dir):     
            shutil.rmtree(dir) 
            
        mimir_template(request)

        return Output(output='output')
    
@app.post("/api/grafana/mysql")
async def mysql_template_route(request:MysqlInput) -> Output:
    
        dir = 'app/media/MyGrafana'
        if os.path.exists(dir):     
            shutil.rmtree(dir) 
            
        mysql_template(request)

        return Output(output='output')