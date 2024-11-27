
def ansible_nginx_install_ubuntu(input):
    prompt = ""
    return prompt
    
    
def ansible_nginx_install(input):
    
    if input.os == 'ubuntu':
        return ansible_nginx_install_ubuntu(input)
    
    