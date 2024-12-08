
def select_install(input):
    
    match input.os:
        
        case "Ubuntu":
            with open("app/media/Installation_base/Terraform/ubuntu.sh", 'r') as file:
                file_content = file.read()

            return file_content
                
        case "Fedora":
            with open("app/media/Installation_base/Terraform/fedora.sh", 'r') as file:
                file_content = file.read()

            return file_content
        
        case "Centos":
            with open("app/media/Installation_base/Terraform/centos.sh", 'r') as file:
                file_content = file.read()

            return file_content
        
        case "Amazon_linux":
            with open("app/media/Installation_base/Terraform/amazon_linux.sh", 'r') as file:
                file_content = file.read()

            return file_content
        case _:
            raise ValueError()
        
        
       