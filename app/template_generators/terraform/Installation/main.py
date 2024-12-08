import os
import shutil


def create_MyBash_directory():
    
    dir = 'app/media/MyBash'
    
    
    if not os.path.exists(dir): 
        os.makedirs(dir)
        os.path.join(dir, 'bash.sh') 
            
        
    
def select_install(input):
    create_MyBash_directory()
    
    match input.os:
        
        
        case "Ubuntu":
            source = 'app/media/Installation_base/Terraform/ubuntu.sh'
            dest = 'app/media/MyBash/bash.sh'
            shutil.copyfile(source, dest)
                
        case "Fedora":
            source = 'app/media/Installation_base/Terraform/fedora.sh'
            dest = 'app/media/MyBash/bash.sh'
            shutil.copyfile(source, dest)
        
        case "Centos":
            source = 'app/media/Installation_base/Terraform/centos.sh'
            dest = 'app/media/MyBash/bash.sh'
            shutil.copyfile(source, dest)
        
        case "Amazon_linux":
            source = 'app/media/Installation_base/Terraform/amazon_linux.sh'
            dest = 'app/media/MyBash/bash.sh'
            shutil.copyfile(source, dest)
        case _:
            raise ValueError()
        
        
       