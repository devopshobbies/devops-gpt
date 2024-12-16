from app.app_instance import app
from app.models import (AlertManagerInput,Output)
from app.template_generators.grafana_data_sources.alertmanager import alert_manager_template
import shutil
import os

@app.post("/api/grafana/alertmanager")
async def alertmanager_template(request:AlertManagerInput) -> Output:
    
        dir = 'app/media/MyGrafana'
        if os.path.exists(dir):     
            shutil.rmtree(dir) 
            
        alert_manager_template(request)

        return Output(output='output')
    
