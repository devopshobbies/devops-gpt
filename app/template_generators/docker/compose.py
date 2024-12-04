import yaml
from app.models.compose_models import DockerCompose

def docker_compose_generator(input):
    
    compose_total = input.model_dump(mode="json")
    
    file=open("app/media/MyCompose/docker-compose.yaml","w")
    yaml.dump(compose_total,file)
    file.close()
   