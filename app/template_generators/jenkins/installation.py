import os
import shutil


def create_directory(folder:str,filename:str):
    
    dir = f"app/media/{folder}"
    
    
    if not os.path.exists(dir): 
        os.makedirs(dir)
        os.path.join(dir, filename) 
            
        
    
def select_install_jenkins(input):
    
    create_directory("MyBash",'bash.sh')
    create_directory("MyCompose",'docker-compose.yaml')
    
    if input.environment == 'Docker':
        
        source = 'app/media/Installation_base/Jenkins/docker-compose.yml'
        dest = 'app/media/MyCompose/docker-compose.yaml'
        shutil.copyfile(source, dest)
        
    else:
    
        match input.os:
            
            
            case "Ubuntu":
                source = 'app/media/Installation_base/Jenkins/ubuntu.sh'
                dest = 'app/media/MyBash/bash.sh'
                shutil.copyfile(source, dest)
            
            case "Fedora":
                source = 'app/media/Installation_base/Jenkins/fedora.sh'
                dest = 'app/media/MyBash/bash.sh'
                shutil.copyfile(source, dest)
        
            
            case "RHEL":
                source = 'app/media/Installation_base/Jenkins/RHEL.sh'
                dest = 'app/media/MyBash/bash.sh'
                shutil.copyfile(source, dest)       
            
            case _:
                raise ValueError()
            
            
    
        
        
       