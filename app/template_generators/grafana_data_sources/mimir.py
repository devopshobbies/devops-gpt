import yaml
import os

def mimir_template(input):
    
        json_template = {
            "apiVersion": 1,
            "datasources": [
                {
                "name": input.name,
                "uid": input.uid,
                "type": "prometheus",
                "access": "proxy",
                "orgId": 1,
                "url": input.url,
                "editable": input.editable,
                "version": 1,
                "jsonData": {
                    "httpHeaderName1": input.httpHeaderName1,
                    "alertmanagerUid": input.alertmanagerUid
                },
                "secureJsonData": {
                    "httpHeaderValue1": input.httpHeaderValue1
                }
                }
            ]
            }

        dir = "app/media/MyGrafana"
        os.makedirs(dir)
        os.path.join(dir, 'mimir.yml') 
            
        file=open("app/media/MyGrafana/mimir.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        
   