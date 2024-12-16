import yaml
import os

def alert_manager_template(input):
    if input.basic_auth is None:
        json_template = {
            "apiVersion": 1,
            "datasources": [
                {
                "name": "Alertmanager",
                "uid": "alertmanager",
                "type": "alertmanager",
                "url": "http://localhost:9093",
                "access": "proxy",
                "orgId": 1,
                "jsonData": {
                    "implementation": input.implementation,
                    "handleGrafanaManagedAlerts": input.handleGrafanaManagedAlerts
                },
                "editable": input.editable,
               
                }
            ]
            }
        dir = "app/media/MyGrafana"
        os.makedirs(dir)
        os.path.join(dir, 'alertmanager.yml') 
            
        file=open("app/media/MyGrafana/alertmanager.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        
    else:
        json_template = {
            "apiVersion": 1,
            "datasources": [
                {
                "name": "Alertmanager",
                "uid": "alertmanager",
                "type": "alertmanager",
                "url": "http://localhost:9093",
                "access": "proxy",
                "orgId": 1,
                "jsonData": {
                    "implementation": input.implementation,
                    "handleGrafanaManagedAlerts": input.handleGrafanaManagedAlerts
                },
                "editable": input.editable,
                "basicAuth": True,
                "basicAuthUser": input.basic_auth.basicAuthUser,
                "secureJsonData": {
                    "basicAuthPassword": input.basic_auth.basicAuthPassword
                }
                }
            ]
            }
        dir = "app/media/MyGrafana"
        os.makedirs(dir)
        os.path.join(dir, 'alertmanager.yml') 
            
        file=open("app/media/MyGrafana/alertmanager.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
