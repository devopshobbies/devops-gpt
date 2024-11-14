def IaC_template_generator_docker(input) -> str:

    docker = ['docker_container', 'docker_image']
    create_docker_image = 'true' if input.docker_image else 'false'
    create_docker_container = 'true' if input.docker_container else 'false'

    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions {docker} resources ensuring a modular, flexible structure to enable users
              to configure all essential settings at the root level. Only provide Python code, no explanations or
              markdown formatting. The project should be organized as follows:
              1. Root Directory Structure:
                  - main.tf:
                      - Define the provider block as follows:
                            ```
                            provider "docker" {{
                              host = "unix:///var/run/docker.sock"
                            }}
                            ```
                      - Defines a module block that references "docker" from a subdirectory within modules.
                        This module block should expose all variables that {docker} resources require, allowing
                        configuration at the root level rather than directly within the module.
                      - Every variable defined in {docker} resources should be passed through the module block,
                        ensuring that users can adjust all critical parameters of {docker} resources by modifying
                        root main.tf. Avoid using any other parameters. just use the parameters of {docker} resources with the same keys
                  - variables.tf:
                      - Sets these variables names for docker_image resource:
                          create_image(bool), image_name(string), image_force_remove(bool), image_build(object)
                      - Sets these variables names for docker_container resource:
                          create_container(bool), container_image(string), container_name(string), container_hostname(string), container_restart(string)
                  - terraform.tfvars:
                      - Structure as follows:
                          create_image = {create_docker_image}
                          image_name = "my-image"
                          image_force_remove = true
                          image_build = {{
                          context = "./"
                          tag    = ["my-image:latest"]
                          }}

                          create_container = {create_docker_container}
                          container_image = "my-image"
                          container_name = "my-container"
                          container_hostname = "my-host"
                          container_restart = "always"
                  - versions.tf:
                      - Structure as follows:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                docker = {{
                                  source  = "kreuzwerker/docker"
                                  version = ">= 2.8.0"
                               }}
                              }}
                            }}
              2. Module Directory Structure (modules/docker):
                  - main.tf:
                      - Set the following parameters for docker_image resource (name its terraform resource to "image") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.create_image ? 1 : 0
                               ```
                           - 2. name (type: string): Specifies the image name.
                           - 3. force_remove (type: boolean): Determines whether to forcibly remove intermediate containers.
                           - 4. build (block type): Includes the following required field:
                               - context (type: string, required): Specifies the build context for the image.
                               - tag(type: List of Strings, required): Specifices the image tag in the 'name:tag'
                                 format, (e.g., ["NAME:VERSION"])
                      - Set the following parameters for docker_container resource (name its terraform resource to "container") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.create_container ? 1 : 0
                               ```
                           - 2. image (type: string): Specifies the container image.
                           - 3. name (type: string): Sets the container name.
                           - 4. hostname (type: string): Configures the container hostname.
                           - 5. restart (type: string): Defines the container's restart policy (e.g., always, on-failure, no).
                  - variables.tf:
                      - Sets these variables names for docker_image resource:
                          create_image(bool), image_name(string), image_force_remove(bool), image_build(object)
                      - Sets these variables names for docker_container resource:
                          create_container(bool), container_image(string), container_name(string), container_hostname(string), container_restart(string)
                  - terraform.tfvars:
                      - Structure as follows:
                          create_image = {create_docker_image}
                          image_name = "my-image"
                          image_force_remove = true
                          image_build = {{
                          context = "./"
                          tag    = ["my-image:latest"]
                          }}

                          create_container = {create_docker_container}
                          container_image = "my-image"
                          container_name = "my-container"
                          container_hostname = "my-host"
                          container_restart = "always"
                  - versions.tf:
                      - Structure as follows:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                docker = {{
                                  source  = "kreuzwerker/docker"
                                  version = ">= 2.8.0"
                               }}
                              }}
                            }}
              Ensure this project structure supports {docker}’s configurability, extensibility, and
              reusability across diverse Terraform providers, empowering users to manage their resources through a
              single, customizable root configuration while keeping module internals robustly modular.

              finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry. and we dont need any base directory in the python code. the final
              terraform template must work very well without any error!

              Python code you give me, must have structure like that:

              import os
              project_name = "app/media/MyTerraform"
              modules_dir = os.path.join(project_name, "modules")
              docker_container_dir = os.path.join(modules_dir, "docker_container")

              # Create project directories
              os.makedirs(docker_container_dir, exist_ok=True)

              # Create main.tf
              with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                  # any thing you need

            """
    return prompt
