def docker_compose_generator(input):
    compose_services = input.services
    services = [i.container_name for i in compose_services]
    images = [{i.container_name:i.image_full} for i in compose_services]
    volumes = [{i.container_name:i.volumes_full} for i in compose_services]
    depends_on = [{i.container_name:i.depends_on} for i in compose_services]
    ports = [{i.container_name:i.ports} for i in compose_services]
    env = [{i.container_name:i.environments} for i in compose_services]
    networks = [{i.container_name:i.networks} for i in compose_services]
   
    
    prompt = f"""

        generate a python code (with out any ```python entry or additionals) with generates a docker-compose.yaml file in the directory 'app/media/MyCompose'
        
        
            
        
        finally just give me a python code without any note that can generate a project folder with the
                    given schema without ```python entry. and we dont need any base directory in the python code.
                    the final ansible template must work very well without any error!
                    
                    the python code you give me, must have structure like that:
                    
                    import os
                    project_name = "app/media/MyCompose"
                    foo_dir = os.path.join(project_name, "bar")
                    x_dir = os.path.join(modules_dir, "y")

                    # Create project directories
                    os.makedirs(compose_dir, exist_ok=True)

                    # Create main.tf
                    with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                        # any thing you need
    
    
    
    """
    return prompt