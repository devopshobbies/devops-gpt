import yaml
import os

def mysql_template(input):
    
        if input.tls is None:
            json_template = {
                "apiVersion": 1,
                "datasources": [
                    {
                    "name": input.name,
                    "type": "mysql",
                    "url": input.url,
                    "user": input.user,
                    "editable": input.editable,
                    "jsonData": {
                       
                        "database": input.database,
                        "maxOpenConns": input.maxOpenConns,
                        "maxIdleConns":input.maxIdleConns,
                        "maxIdleConnsAuto": input.maxIdleConnsAuto,
                        "connMaxLifetime": input.connMaxLifetime
                    },
                    "secureJsonData": {
                        "password": input.password,
                        
                    }
                    }
                ]
                }

            dir = "app/media/MyGrafana"
            os.makedirs(dir)
            os.path.join(dir, 'mysql.yml') 
                
            file=open("app/media/MyGrafana/mysql.yml","w")
            yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        
        else:
            json_template = {
                    "apiVersion": 1,
                    "datasources": [
                        {
                        "name": input.name,
                        "type": "mysql",
                        "url": input.url,
                        "user": input.user,
                        "editable": input.editable,
                        "jsonData": {
                            "tlsAuth": input.tls.tlsAuth, 
                            "tlsSkipVerify": input.tls.tlsSkipVerify,
                            "database": input.database,
                            "maxOpenConns": input.maxOpenConns,
                            "maxIdleConns":input.maxIdleConns,
                            "maxIdleConnsAuto": input.maxIdleConnsAuto,
                            "connMaxLifetime": input.connMaxLifetime
                        },
                        "secureJsonData": {
                            
                            "password": input.password,
                            "tlsClientCert": input.tls.tlsClientCert, 
                            "tlsCACert": input.tls.tlsCACert
                        }
                        }
                    ]
                    }
            dir = "app/media/MyGrafana"
            os.makedirs(dir)
            os.path.join(dir, 'mysql.yml') 
                
        file=open("app/media/MyGrafana/mysql.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
        
        
   