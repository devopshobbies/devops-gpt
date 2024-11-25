def IaC_template_generator_iam(input) -> str:

    iam = ['aws_iam_user', 'aws_iam_group']

    aws_iam_create_user = 'true' if input.iam_user else 'false'
    aws_iam_create_group = 'true' if input.iam_group else 'false'

    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions {iam} resources ensuring a modular, flexible structure to enable users
              to configure all essential settings at the root level. Only provide Python code, no explanations or
              markdown formatting. The project should be organized as follows:
              1. Root Directory Structure:
                  - main.tf:
                      - Define the provider block as follows:
                            ```
                            provider "aws" {{
                              region = "us-east-1"
                            }}
                            ```
                      - Defines a module block that references "iam" from a subdirectory within modules.
                        This module block should expose all variables that {iam} resources require, allowing
                        configuration at the root level rather than directly within the module.
                      - Every variable defined in {iam} resources should be passed through the module block,
                        ensuring that users can adjust all critical parameters of {iam} resources by modifying
                        root main.tf. Avoid using any other parameters. just use the parameters of {iam} resources with the same keys
                  - variables.tf:
                      - Sets these variables names for aws_iam_user resource:
                          iam_create_user(bool), iam_users(list(map(string)))
                      - Sets these variables names for aws_iam_group resource:
                          iam_create_group(bool), iam_groups(list(map(string)))
                  - terraform.tfvars:
                      - Structure as follows:
                          iam_create_user = {aws_iam_create_user}
                          iam_users = [
                            {{
                              name = "devopshobbies"
                              path = "/"
                            }}
                          ]

                          iam_create_group = {aws_iam_create_group}
                          iam_groups = [
                            {{
                              name = "developers"
                              path = "/"
                            }}
                          ]
                  - versions.tf:
                      - Structure as follows:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                aws = {{
                                  source  = "hashicorp/aws"
                                  version = ">= 5.20"
                               }}
                              }}
                            }}
              2. Module Directory Structure (modules/iam):
                  - main.tf:
                      - Set the following parameters for aws_iam_user resource (name its terraform resource to "users") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.iam_create_user ? length(var.iam_users) : 0
                               ```
                           - 2. name (type: string): follow the below syntax for name parameter:
                               ```
                               name  = var.iam_users[count.index]["name"]
                               ```
                           - 3. path (type: string): follow the below syntax for path parameter:
                               ```
                               path  = var.iam_users[count.index]["path"]
                               ```
                      - Set the following parameters for aws_iam_group resource (name its terraform resource to "groups") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.iam_create_group ? length(var.iam_groups) : 0
                               ```
                           - 2. name (type: string): follow the below syntax for name parameter:
                               ```
                               name  = var.iam_groups[count.index]["name"]
                               ```
                           - 3. path (type: string): follow the below syntax for path parameter:
                               ```
                               path  = var.iam_groups[count.index]["path"]
                               ```
                  - variables.tf:
                      - Sets these variables names for aws_iam_user resource:
                          iam_create_user(bool), iam_users(list(map(string)))
                      - Sets these variables names for aws_iam_group resource:
                          iam_create_group(bool), iam_groups(list(map(string)))
                  - terraform.tfvars:
                      - Structure as follows:
                          iam_create_user = {aws_iam_create_user}
                          iam_users = [
                            {{
                              name = "devopshobbies"
                              path = "/"
                            }}
                          ]

                          iam_create_group = {aws_iam_create_group}
                          iam_groups = [
                            {{
                              name = "developers"
                              path = "/"
                            }}
                          ]
                  - versions.tf:
                      - Structure as follows:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                aws = {{
                                  source  = "hashicorp/aws"
                                  version = ">= 5.20"
                               }}
                              }}
                            }}
              Ensure this project structure supports {iam}’s configurability, extensibility, and
              reusability across diverse Terraform providers, empowering users to manage their resources through a
              single, customizable root configuration while keeping module internals robustly modular.

              finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry. and we dont need any base directory in the python code. the final
              terraform template must work very well without any error!

              Python code you give me, must have structure like that:

              import os
              project_name = "app/media/MyTerraform"
              modules_dir = os.path.join(project_name, "modules")
              iam_dir = os.path.join(modules_dir, "iam")

              # Create project directories
              os.makedirs(iam_dir, exist_ok=True)

              # Create main.tf
              with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                  # any thing you need

            """
    return prompt
