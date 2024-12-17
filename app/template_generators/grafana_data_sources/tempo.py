import yaml
import os

def remove_none_values(d):
    if isinstance(d, dict):
        return {k: remove_none_values(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_none_values(i) for i in d if i is not None]
    return d

def tempo_template(input):
    dir = 'app/media/MyGrafana'
    compose_total = input.dict(exclude_none=True)
   
    
    os.makedirs(dir)
    os.path.join(dir, 'tempo.yaml') 
            
    file=open("app/media/MyGrafana/tempo.yaml","w")
    yaml.dump(compose_total,file,default_flow_style=False, sort_keys=False)
    file.close()
        
  