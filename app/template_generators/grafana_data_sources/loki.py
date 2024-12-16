import yaml
import os

def loki_template(input):
    if input.basic_auth is None:
        json_template = {
            "apiVersion": 1,
            "datasources": [
                {
                "name": input.name,
                "uid": input.uid,
                "type": "loki",
                "orgId": 1,
                "url": input.url,
                "access": "proxy",
                
                "jsonData": {
                    "timeout": input.timeout,
                    "maxLines": input.maxLines
                },
                "editable": input.editable,
               
                }
            ]
            }
        dir = "app/media/MyGrafana"
        os.makedirs(dir)
        os.path.join(dir, 'loki.yml') 
            
        file=open("app/media/MyGrafana/loki.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        
    else:
        json_template = {
            "apiVersion": 1,
            "datasources": [
                {
                "name": input.name,
                "uid": input.uid,
                "type": "loki",
                "url": input.url,
                "access": "proxy",
                "orgId": 1,
                
                "jsonData": {
                    "timeout": input.timeout,
                    "maxLines": input.maxLines
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
        os.path.join(dir, 'loki.yml') 
            
        file=open("app/media/MyGrafana/loki.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)

