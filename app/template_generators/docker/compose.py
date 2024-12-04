import yaml
from app.models.compose_models import DockerCompose
import os

def docker_compose_generator(input):
    dir = 'app/media/MyCompose'
    compose_total = input.model_dump(mode="json")
    if not os.path.exists(dir): 
        os.makedirs(dir)
        os.path.join(dir, 'docker-compose.yaml') 
            
        file=open("app/media/MyCompose/docker-compose.yaml","w")
        yaml.dump(compose_total,file)
        file.close()
        
    file=open("app/media/MyCompose/docker-compose.yaml","w")
    yaml.dump(compose_total,file)
    file.close()
   