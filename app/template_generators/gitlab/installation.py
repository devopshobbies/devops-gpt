import os
import shutil


def create_directory(folder:str,filename:str):
    
    dir = f"app/media/{folder}"
    
    
    if not os.path.exists(dir): 
        os.makedirs(dir)
        os.path.join(dir, filename) 
        
    
def select_install_gitlab(input):
    
    create_directory("MyCompose","docker-compose.yaml")
    
    
    match input.environment:
            
            case "Docker":
                source = 'app/media/Installation_base/Gitlab/docker-compose.yaml'
                dest = 'app/media/MyCompose/docker-compose.yaml'
                shutil.copyfile(source, dest)
              
            
            case _:
                raise ValueError()
            
            
    
        
        
       