def docker_compose_generator(input):
    compose_network = input.network.name
    compose_services = input.services
    services = [i.name for i in compose_services]
    images = [{i.name:i.image_full} for i in compose_services]
    volumes = [{i.name:i.volumes_full} for i in compose_services]
    depends_on = [{i.name:i.depends_on} for i in compose_services]
    ports = [{i.name:i.ports} for i in compose_services]
    env = [{i.name:i.environments} for i in compose_services]
    networks = [{i.name:i.networks} for i in compose_services]
   
    
    prompt = f"""

        generate a python code (with out any ```python entry or additionals) with generates a docker-compose.yaml file in the directory 'app/media/MyCompose'
        
        the docker-compose.yaml, must following there instructions:
                    the version must be = 3
                    set services following this list: {services}
                    set images to serivce following this dict : {images}
                    set volumes to service following this dict : {volumes}
                    set depends_on to service following this dict : {depends_on}
                    set ports to service following this dict : {ports}
                    set environment to service following this dict : {env}
                    set netwotks to service following this dict : {networks}
                    
                    
                    finally, at the end of docker-compose file, add following block:
                    ```
                        networks:
                            {compose_network}:
                                driver: bridge
                    
                    ```
            
        
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