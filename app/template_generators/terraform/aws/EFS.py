def IaC_template_generator_efs(input) -> str:
    
    efs = ['aws_security_group', 'aws_efs_file_system', 'aws_efs_mount_target', 'aws_efs_backup_policy']

    aws_efs_create_file_system = 'true' if input.efs_file_system else 'false'
    aws_efs_create_mount_target = 'true' if input.efs_mount_target else 'false'
    aws_efs_create_backup_policy = 'true' if input.efs_backup_policy else 'false'


    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions {efs} resources ensuring a modular, flexible structure to enable users
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
                      - Defines a module block that references "efs" from a subdirectory within modules.
                        Don't forget to use source parameter to call efs module as follows:
                        ```
                        source = "./modules/efs"
                        ```
                        This module block should expose all variables that {efs} resources require, allowing
                        configuration at the root level rather than directly within the module.
                      - Every variable defined in {efs} resources should be passed through the module block,
                        ensuring that users can adjust all critical parameters of {efs} resources by modifying
                        root main.tf. Avoid using any other parameters. just use the parameters of {efs} resources with the same keys
                  - variables.tf:
                      - Sets these variables names for aws_efs_file_system resource:
                          file_system_create(bool), efs(object)
                      - Sets these variables names for aws_efs_mount_target resource:
                          mount_target_create(bool)
                      - Sets these variables names for aws_efs_backup_policy resource:
                          backup_policy_create(bool)
                      - Sets these variables names for aws_security_group resource:
                          security_group_name(string), security_group_ingress_rules(map(object)), security_group_egress_rule(object())
                          Sets security_group_ingress_rules as follows:
                              ```
                              type = map(object({{
                                description = string
                                from_port   = number
                                to_port     = number
                                protocol    = string
                                cidr_blocks = list(string)
                              }}))
                              ```
                          Sets security_group_egress_rule as follows:
                              ```
                              type        = object({{
                                from_port   = number
                                to_port     = number
                                protocol    = string
                                cidr_blocks = list(string)
                              }})
                              ```
                          Sets efs as follows:
                          ```
                          type = object({{
                            creation_token   = string
                            encrypted        = bool
                            performance_mode = string
                            throughput_mode  = string
                            backup_policy    = string
                          }})
                          ```
                  - terraform.tfvars:
                      - Structure as follows:
                          security_group_name = "efs_rule"
                          security_group_ingress_rules = {{
                            efs_rule = {{
                            description = "EFS Ingress"
                            from_port   = 2049
                            to_port     = 2049
                            protocol    = "tcp"
                            cidr_blocks = ["0.0.0.0/0"]
                            }}
                          }}
                          security_group_egress_rule = {{
                            from_port   = 0
                            to_port     = 0
                            protocol    = "-1"
                            cidr_blocks = ["0.0.0.0/0"]
                          }}

                          file_system_create = {aws_efs_create_file_system}
                          efs = {{
                            creation_token   = "terraform"
                            encrypted        = true
                            performance_mode = "generalPurpose"
                            throughput_mode  = "elastic"
                            backup_policy    = "ENABLED"
                          }}

                          mount_target_create = {aws_efs_create_mount_target}
                          backup_policy_create = {aws_efs_create_backup_policy}
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
              2. Module Directory Structure (modules/efs):
                  - main.tf:
                      - Create a locals block as follows:
                          ```
                          locals {{
                            default_efs_lifecycle_policies = {{
                              transition_to_ia                    = "AFTER_14_DAYS",
                              transition_to_primary_storage_class = "AFTER_1_ACCESS",
                            }}
                          }}
                          ```
                      - Create these data blocks as follows:
                          ```
                          data "aws_availability_zones" "available_zones" {{
                            state = "available"
                          }}

                          data "aws_vpc" "default_vpc" {{
                            default = true
                          }}

                          data "aws_subnets" "subnets_ids" {{
                            filter {{
                              name   = "vpc-id"
                              values = [data.aws_vpc.default_vpc.id]
                            }}
                          }}
                          ```
                      - Set the following parameters for aws_security_group resource (name its terraform resource to "security_group") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.file_system_create && var.mount_target_create ? 1 : 0
                               ```
                           - 2. name: follow the below syntax for name:
                               ```
                               name = var.security_group_name
                               ```
                           - 3. description: follow the below syntax for description:
                               ```
                               description = "Security group for EFS mount targets"
                               ```
                           - 4. vpc_id: follow the below syntax for vpc_id:
                               ```
                               vpc_id = data.aws_vpc.default_vpc.id
                               ```
                           - 5. create a dynamic block for ingress rules as follows:
                               ```
                               dynamic "ingress" {{
                                 for_each = var.security_group_ingress_rules
                                 content {{
                                   description = ingress.value["description"]
                                   from_port   = ingress.value["from_port"]
                                   to_port     = ingress.value["to_port"]
                                   protocol    = ingress.value["protocol"]
                                   cidr_blocks = ingress.value["cidr_blocks"]
                                 }}
                               }}
                               ```
                           - 6. create a block for egress rule as follows:
                               ```
                               egress {{
                                 from_port   = var.security_group_egress_rule["from_port"]
                                 to_port     = var.security_group_egress_rule["to_port"]
                                 protocol    = var.security_group_egress_rule["protocol"]
                                 cidr_blocks = var.security_group_egress_rule["cidr_blocks"]
                               }}
                               ```
                      - Set the following parameters for aws_efs_file_system resource (name its terraform resource to "filesystem") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.file_system_create ? 1 : 0
                               ```
                           - 2. creation_token (type: string): follow the below syntax for creation_token:
                               ```
                               creation_token = var.efs["creation_token"]
                               ```
                           - 3. encrypted (type: string): follow the below syntax for encrypted:
                               ```
                               encrypted = var.efs["encrypted"]
                               ```
                           - 4. performance_mode: follow the below syntax for performance_mode:
                               ```
                               performance_mode = var.efs["performance_mode"]
                               ```
                           - 5. throughput_mode: follow the below syntax for throughput_mode:
                               ```
                               throughput_mode  = var.efs["throughput_mode"]
                               ```
                           - 6. create the below blocks as follows:
                               ```
                               lifecycle_policy {{
                                 transition_to_ia = lookup(local.default_efs_lifecycle_policies, "transition_to_ia", null)
                               }}

                               lifecycle_policy {{
                                 transition_to_primary_storage_class = lookup(local.default_efs_lifecycle_policies, "transition_to_primary_storage_class", null)
                               }}

                               tags = {{
                                 Name = "terraform-efs"
                               }}
                               ```
                      - Set the following parameters for aws_efs_mount_target resource (name its terraform resource to "mount_target") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.file_system_create && var.mount_target_create ? length(data.aws_availability_zones.available_zones.names) : 0
                               ```
                           - 2. file_system_id (type: string): follow the below syntax for file_system_id:
                               ```
                               file_system_id = aws_efs_file_system.filesystem[0].id
                               ```
                           - 3. subnet_id: follow the below syntax for subnet_id:
                               ```
                               subnet_id = data.aws_subnets.subnets_ids.ids[count.index]
                               ```
                           - 4. security_groups: follow the below syntax for security_groups:
                               ```
                               security_groups = [aws_security_group.security_group[0].id]
                               ```
                      - Set the following parameters for aws_efs_backup_policy resource (name its terraform resource to "backup_policy") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.file_system_create && var.backup_policy_create ? 1 : 0
                               ```
                           - 2. file_system_id: follow the below syntax for file_system_id:
                               ```
                               file_system_id = aws_efs_file_system.filesystem[0].id
                               ```
                           - 3. Create the below block as follows:
                               ```
                               backup_policy {{
                                 status = var.efs["backup_policy"]
                               }}
                               ```
                  - variables.tf:
                      - Sets these variables names for aws_efs_file_system resource:
                          file_system_create(bool), efs(object)
                      - Sets these variables names for aws_efs_mount_target resource:
                          mount_target_create(bool)
                      - Sets these variables names for aws_efs_backup_policy resource:
                          backup_policy_create(bool)
                      - Sets these variables names for aws_security_group resource:
                          security_group_name(string), security_group_ingress_rules(map(object)), security_group_egress_rule(object())
                          Sets security_group_ingress_rules as follows:
                              ```
                              type = map(object({{
                                description = string
                                from_port   = number
                                to_port     = number
                                protocol    = string
                                cidr_blocks = list(string)
                              }}))
                              ```
                          Sets security_group_egress_rule as follows:
                              ```
                              type        = object({{
                                from_port   = number
                                to_port     = number
                                protocol    = string
                                cidr_blocks = list(string)
                              }})
                              ```
                          Sets efs as follows:
                          ```
                          type = object({{
                            creation_token   = string
                            encrypted        = bool
                            performance_mode = string
                            throughput_mode  = string
                            backup_policy    = string
                          }})
                  - terraform.tfvars:
                      - Structure as follows:
                          security_group_name = "efs_rule"
                          security_group_ingress_rules = {{
                            efs_rule = {{
                            description = "EFS Ingress"
                            from_port   = 2049
                            to_port     = 2049
                            protocol    = "tcp"
                            cidr_blocks = ["0.0.0.0/0"]
                            }}
                          }}
                          security_group_egress_rule = {{
                            from_port   = 0
                            to_port     = 0
                            protocol    = "-1"
                            cidr_blocks = ["0.0.0.0/0"]
                          }}

                          file_system_create = {aws_efs_create_file_system}
                          efs = {{
                            creation_token   = "terraform"
                            encrypted        = true
                            performance_mode = "generalPurpose"
                            throughput_mode  = "elastic"
                            backup_policy    = "ENABLED"
                          }}

                          mount_target_create = {aws_efs_create_mount_target}
                          backup_policy_create = {aws_efs_create_backup_policy}
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
              Ensure this project structure supports {efs}’s configurability, extensibility, and
              reusability across diverse Terraform providers, empowering users to manage their resources through a
              single, customizable root configuration while keeping module internals robustly modular.

              finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry. and we dont need any base directory in the python code. the final
              terraform template must work very well without any error!

              Python code you give me, must have structure like that:

              import os
              project_name = "app/media/MyTerraform"
              modules_dir = os.path.join(project_name, "modules")
              efs_dir = os.path.join(modules_dir, "efs")

              # Create project directories
              os.makedirs(efs_dir, exist_ok=True)

              # Create main.tf
              with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                  # any thing you need

            """
    return prompt
