import yaml
import os
 
   
def elasticsearch_template(input):
    
        json_template = {
            "apiVersion": 1,
            "datasources": [
                {
                "name": input.name,
                "type": "elasticsearch",
                "url": input.url,
                "access": "proxy",
                
                "jsonData": {
                    "index": input.index,
                    "interval": input.interval,
                    "timeField": input.timeField,
                    "logMessageField": input.logMessageField,
                    "logLevelField": input.logLevelField,
                    
                },
                "editable": input.editable,
               
                }
            ]
            }
        dir = "app/media/MyGrafana"
        os.makedirs(dir)
        os.path.join(dir, 'elasticsearch.yml') 
            
        file=open("app/media/MyGrafana/elasticsearch.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        
 