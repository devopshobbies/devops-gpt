import yaml
import os
import ruamel.yaml
from ruamel.yaml.scalarstring import ScalarString
import re

class SingleQuotedScalarString(ScalarString):
    def __new__(cls, value):
        return ScalarString.__new__(cls, value)
    
def pormetheus_template(input):
       
            
        json_template = {
            "apiVersion": 1,
            "datasources": [
                {
                "name": input.name,
                "uid": "prometheus",
                "type": "prometheus",
                "access": "proxy",
                "url": input.url,
                "editable": input.editable,
                "jsonData": {
                    "httpMethod": input.httpMethod,
                    "manageAlerts": input.manageAlerts,
                    "prometheusType": input.prometheusType,
                    "prometheusVersion": input.prometheusVersion,
                    "cacheLevel": input.cacheLevel,
                    "disableRecordingRules": input.disableRecordingRules,
                    "incrementalQueryOverlapWindow": input.incrementalQueryOverlapWindow,
                   
                }
                }
            ]
            }

        
        dir = "app/media/MyGrafana"
        os.makedirs(dir)
        os.path.join(dir, 'prometheus.yml')   
        file=open("app/media/MyGrafana/prometheus.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        

    