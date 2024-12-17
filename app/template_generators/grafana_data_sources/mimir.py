import yaml
import os

def mimir_template(input):
        if input.multi_tenancy is not None:
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
                        "httpHeaderValue1": input.multi_tenancy.tenant_name
                    }
                    }
                ]
                }

            dir = "app/media/MyGrafana"
            os.makedirs(dir)
            os.path.join(dir, 'mimir.yml') 
                
            file=open("app/media/MyGrafana/mimir.yml","w")
            yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        
        
        else:
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
                   
                    }
                ]
                }

            dir = "app/media/MyGrafana"
            os.makedirs(dir)
            os.path.join(dir, 'mimir.yml') 
                
            file=open("app/media/MyGrafana/mimir.yml","w")
            yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        
   
        
   