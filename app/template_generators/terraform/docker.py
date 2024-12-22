def IaC_template_generator_docker(input) -> str:

    
    create_docker_image = 'true' if input.docker_image else 'false'
    create_docker_container = 'true' if input.docker_container else 'false'
    image_build = """{
  context = "./"
  tag    = ["my-image:latest"]
}
"""
    tfvars_file = f"""create_image = {create_docker_image}
image_name = "my-image"
image_force_remove = true
image_build = {image_build}

create_container = {create_docker_container}
container_image = "my-image"
container_name = "my-container"
container_hostname = "my-host"
container_restart = "always"
    
    
    """
    return tfvars_file