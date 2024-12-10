import os
import shutil


def create_MyBash_directory():
    
    dir = 'app/media/MyBash'
    
    
    if not os.path.exists(dir): 
        os.makedirs(dir)
        os.path.join(dir, 'bash.sh') 
    
    
        
def docker_installation_selection(input):
    
    create_MyBash_directory()
    
    match input.os:
        
        case "Ubuntu":
            
            source = 'app/media/Installation_base/Docker/ubuntu.sh'
            dest = 'app/media/MyBash/bash.sh'
            
            shutil.copyfile(source, dest)
            
                
        case "Fedora":
            source = 'app/media/Installation_base/Docker/fedora.sh'
            dest = 'app/media/MyBash/bash.sh'
            shutil.copyfile(source, dest)
        
        case "Centos":
            source = 'app/media/Installation_base/Docker/centos.sh'
            dest = 'app/media/MyBash/bash.sh'
            shutil.copyfile(source, dest)
        
        case "RHEL":
            source = 'app/media/Installation_base/Docker/RHEL.sh'
            dest = 'app/media/MyBash/bash.sh'
            shutil.copyfile(source, dest)
        case _:
            raise ValueError()