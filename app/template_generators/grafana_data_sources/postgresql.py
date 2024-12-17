import yaml
import os

def postgres_template(input):
        json_template = {
            "apiVersion": 1,
            "datasources": [
                {
                "name": input.name,
                "type": "postgres",
                "url": input.url,
                "user": input.user,
                "editable": input.editable,
                "secureJsonData": {
                    "password": input.password
                },
                "jsonData": {
                    "database": input.database,
                    "sslmode": input.sslmode,
                    "maxOpenConns": input.maxOpenConns,
                    "maxIdleConns": input.maxIdleConns,
                    "maxIdleConnsAuto": input.maxIdleConnsAuto,
                    "connMaxLifetime": input.connMaxLifetime,
                    "postgresVersion": input.postgresVersion,
                    "timescaledb": input.timescaledb
                }
                }
            ]
            }

        
        dir = "app/media/MyGrafana"
        os.makedirs(dir)
        os.path.join(dir, 'postgresql.yml') 
                
        file=open("app/media/MyGrafana/postgresql.yml","w")
        yaml.dump(json_template,file,default_flow_style=False,sort_keys=False)
    