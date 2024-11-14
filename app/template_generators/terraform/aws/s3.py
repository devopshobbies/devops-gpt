def IaC_template_generator_s3(input) -> str:

    s3 = ['aws_s3_bucket', 'aws_s3_bucket_versioning']

    aws_s3_create_bucket = 'true' if input.s3_bucket else 'false'
    aws_s3_create_bucket_versioning = 'true' if input.bucket_versioning else 'false'

    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions {s3} resources ensuring a modular, flexible structure to enable users
              to configure all essential settings at the root level. Only provide Python code, no explanations or
              markdown formatting. The project should be organized as follows:
              1. Root Directory Structure:
                  - main.tf:
                      - Define the provider block as follows:
                            ```
                            provider "aws" {{
                              host = "us-east-1"
                            }}
                            ```
                      - Defines a module block that references "s3" from a subdirectory within modules.
                        This module block should expose all variables that {s3} resources require, allowing
                        configuration at the root level rather than directly within the module.
                      - Every variable defined in {s3} resources should be passed through the module block,
                        ensuring that users can adjust all critical parameters of {s3} resources by modifying
                        root main.tf. Avoid using any other parameters. just use the parameters of {s3} resources with the same keys
                  - variables.tf:
                      - Sets these variables names for aws_s3_bucket resource:
                          s3_create_bucket(bool), s3_bucket_name(string), s3_bucket_force_destroy(bool), s3_bucket_tags(map(string))
                      - Sets these variables names for aws_s3_bucket_versioning resource:
                          s3_create_bucket_versioning(bool), s3_bucket_versioning_status(string)
                  - terraform.tfvars:
                      - Structure as follows:
                          s3_create_bucket = {aws_s3_create_bucket}
                          s3_bucket_name = "UniqueName"
                          s3_bucket_force_destroy = false
                          s3_bucket_tags = {{
                            Name        = "My bucket"
                            Environment = "Dev"
                          }}
                          s3_create_bucket_versioning = {aws_s3_create_bucket_versioning}
                          s3_bucket_versioning_status = "Enabled"
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
              2. Module Directory Structure (modules/s3):
                  - main.tf:
                      - Set the following parameters for aws_s3_bucket resource (name its terraform resource to "s3_bucket")and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.s3_create_bucket ? 1 : 0
                               ```
                           - 2. bucket (type: string): Specifies the bucket name.
                           - 3. force_destroy (type: boolean): Indicates all objects should be deleted from the bucket when the bucket is destroyed
                           - 4. tags (map(string) type): Includes the following fields:
                               - Name (type: string): A tag for the bucket.
                               - Environment (type: string): A tag for the bucket
                      - Set the following parameters for aws_s3_bucket_versioning resource (name its terraform resource to "s3_bucket_versioning")and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.s3_create_bucket && var.s3_create_bucket_versioning ? 1 : 0
                               ```
                           - 2. bucket: it must points to the s3_bucket resource like the following syntax:
                               ```
                               bucket = aws_s3_bucket.s3_bucket[0].id
                               ```
                           - 3. versioning_configuration: this is a block which has a key/value pair as follows:
                               ```
                               versioning_configuration {{
                                 status = var.s3_bucket_versioning_status
                               }}
                               ```
                  - variables.tf:
                      - Sets these variables names for aws_s3_bucket resource:
                          s3_create_bucket(bool), s3_bucket_name(string), s3_bucket_force_destroy(bool), s3_bucket_tags(map(string))
                      - Sets these variables names for aws_s3_bucket_versioning resource:
                          s3_create_bucket_versioning(bool), s3_bucket_versioning_status(string)
                  - terraform.tfvars:
                      - Structure as follows:
                          s3_create_bucket = {aws_s3_create_bucket}
                          s3_bucket_name = "UniqueName"
                          s3_bucket_force_destroy = false
                          s3_bucket_tags = {{
                            Name        = "My bucket"
                            Environment = "Dev"
                          }}
                          s3_create_bucket_versioning = {aws_s3_create_bucket_versioning}
                          s3_bucket_versioning_status = "Enabled"
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
              Ensure this project structure supports {s3}’s configurability, extensibility, and
              reusability across diverse Terraform providers, empowering users to manage their resources through a
              single, customizable root configuration while keeping module internals robustly modular.

              finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry. and we dont need any base directory in the python code. the final
              terraform template must work very well without any error!

              Python code you give me, must have structure like that:

              import os
              project_name = "app/media/MyTerraform"
              modules_dir = os.path.join(project_name, "modules")
              s3_dir = os.path.join(modules_dir, "s3")

              # Create project directories
              os.makedirs(s3_dir, exist_ok=True)

              # Create main.tf
              with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                  # any thing you need

            """
    return prompt
