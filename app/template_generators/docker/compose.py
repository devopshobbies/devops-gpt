import yaml
from app.models.compose_models import DockerCompose
import os

def remove_none_values(d):
    if isinstance(d, dict):
        return {k: remove_none_values(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_none_values(i) for i in d if i is not None]
    return d


def docker_compose_generator(input):
    dir = 'app/media/MyCompose'
    
    compose_total = input.model_dump(mode="json")
    compose_total = remove_none_values(compose_total)
    if not os.path.exists(dir): 
        os.makedirs(dir)
        os.path.join(dir, 'docker-compose.yaml') 
            
        file=open("app/media/MyCompose/docker-compose.yaml","w")
        yaml.dump(compose_total,file,default_flow_style=False)
        file.close()
        
    file=open("app/media/MyCompose/docker-compose.yaml","w")
    yaml.dump(compose_total,file,default_flow_style=False,sort_keys=False)
    file.close()
   