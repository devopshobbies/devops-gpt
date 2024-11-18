def IaC_template_generator_ec2(input) -> str:
    
    ec2 = ['aws_key_pair', 'aws_security_group', 'aws_instance', 'aws_ami_from_instance']

    aws_ec2_create_key_pair = 'true' if input.key_pair else 'false'
    aws_ec2_create_security_group = 'true' if input.security_group else 'false'
    aws_ec2_create_instance = 'true' if input.aws_instance else 'false'
    aws_ec2_create_ami_from_instance = 'true' if input.ami_from_instance else 'false'


    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions {ec2} resources ensuring a modular, flexible structure to enable users
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
                      - Defines a module block that references "ec2" from a subdirectory within modules.
                        Don't forget to use source parameter to call ec2 module. this is so important.
                        This module block should expose all variables that {ec2} resources require, allowing
                        configuration at the root level rather than directly within the module.
                      - Every variable defined in {ec2} resources should be passed through the module block,
                        ensuring that users can adjust all critical parameters of {ec2} resources by modifying
                        root main.tf. Avoid using any other parameters. just use the parameters of {ec2} resources with the same keys
                  - variables.tf:
                      - Sets these variables names for aws_key_pair resource:
                          key_pair_create(bool), key_pair_name(string)
                      - Sets these variables names for aws_security_group resource:
                          security_group_create(bool), security_group_name(string), security_group_ingress_rules(map(object)), security_group_egress_rule(object())
                      - Sets these variables names for aws_instance resource:
                          instance_create(bool), instance_type(string)
                      - Sets these variables names for aws_ami_from_instance resource:
                          ami_from_instance_create(bool), ami_name(string)
                  - terraform.tfvars:
                      - Structure as follows:
                          key_pair_create = {aws_ec2_create_key_pair}
                          key_pair_name = "ec2"

                          security_group_create = {aws_ec2_create_security_group}
                          security_group_name = "my_rules"
                          security_group_ingress_rules = {{
                            ssh_rule = {{
                            description = "SSH Ingress"
                            from_port   = 22
                            to_port     = 22
                            protocol    = "tcp"
                            cidr_blocks = ["0.0.0.0/0"]
                            }},
                            http_rule = {{
                            description = "HTTP Ingress"
                            from_port   = 80
                            to_port     = 80
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

                          instance_create = {aws_ec2_create_instance}
                          instance_type = "t2.micro"

                          ami_from_instance_create = {aws_ec2_create_ami_from_instance}
                          ami_name = "my-own-ami"
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
              2. Module Directory Structure (modules/ec2):
                  - create an empty file called "terraform.pub" to store the public key for key_pair resource
                  - main.tf:
                      - Create the below data block:
                          ```
                          data "aws_ami" "linux" {{
                            most_recent = true
                            owners      = ["amazon"]

                            filter {{
                              name   = "name"
                              values = ["al2023-ami-2023*kernel-6.1-x86_64"]
                            }}

                            filter {{
                              name   = "root-device-type"
                              values = ["ebs"]
                            }}

                            filter {{
                              name   = "virtualization-type"
                              values = ["hvm"]
                            }}
                          }}
                          ```
                      - Set the following parameters for aws_key_pair resource (name its terraform resource to "key_pair") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.key_pair_create ? 1 : 0
                               ```
                           - 2. key_name (type: string): follow the below syntax for key_name:
                               ```
                               key_name = var.key_pair_name
                               ```
                           - 3. public_key (type: string): follow the below syntax for public_key, avoid generating double brackets {{}} for path.module in the below syntax:
                               ```
                               public_key = file("${{path.module}}/terraform.pub")
                               ```
                      - Set the following parameters for aws_security_group resource (name its terraform resource to "security_group") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.security_group_create ? 1 : 0
                               ```
                           - 2. name: follow the below syntax for name:
                               ```
                               name = var.security_group_name
                               ```
                           - 3. create a dynamic block for ingress rules as follows:
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
                           - 4. create a block for egress rule as follows:
                               ```
                               egress {{
                                 from_port   = var.security_group_egress_rule["from_port"]
                                 to_port     = var.security_group_egress_rule["to_port"]
                                 protocol    = var.security_group_egress_rule["protocol"]
                                 cidr_blocks = var.security_group_egress_rule["cidr_blocks"]
                               }}
                               ```
                      - Set the following parameters for aws_instance resource (name its terraform resource to "instance") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.instance_create ? 1 : 0
                               ```
                           - 2. ami (type: string): follow the below syntax for ami, it uses the data block:
                               ```
                               ami = data.aws_ami.linux.id
                               ```
                           - 3. instance_type (type: string): follow the below syntax for instance_type:
                               ```
                               instance_type = var.instance_type
                               ```
                           - 4. key_name: follow the below syntax for key_name:
                               ```
                               key_name = var.key_pair_create ? aws_key_pair.key_pair[0].key_name : null
                               ```
                           - 5. vpc_security_group_ids: follow the below syntax for vpc_security_group_ids:
                               ```
                               vpc_security_group_ids = var.security_group_create ? [aws_security_group.security_group[0].id] : null
                               ```
                      - Set the following parameters for aws_ami_from_instance resource (name its terraform resource to "ami") and avoid using any other parameters:
                           - 1. count (type: number): follow the below syntax for count:
                               ```
                               count = var.instance_create && var.ami_from_instance_create ? 1 : 0
                               ```
                           - 2. name (type: string): follow the below syntax for name:
                               ```
                               name = var.ami_name
                               ```
                           - 3. source_instance_id: follow the below syntax for source_instance_id:
                               ```
                               source_instance_id = aws_instance.instance[0].id
                               ```
                  - variables.tf:
                      - Sets these variables names for aws_key_pair resource:
                          key_pair_create(bool), key_pair_name(string)
                      - Sets these variables names for aws_security_group resource:
                          security_group_create(bool), security_group_name(string), security_group_ingress_rules(map(object)), security_group_egress_rule(object())
                      - Sets these variables names for aws_instance resource:
                          instance_create(bool), instance_type(string)
                      - Sets these variables names for aws_ami_from_instance resource:
                          ami_from_instance_create(bool), ami_name(string)
                  - terraform.tfvars:
                      - Structure as follows:
                          key_pair_create = {aws_ec2_create_key_pair}
                          key_pair_name = "ec2"

                          security_group_create = {aws_ec2_create_security_group}
                          security_group_name = "my_rules"
                          security_group_ingress_rules = {{
                            ssh_rule = {{
                            description = "SSH Ingress"
                            from_port   = 22
                            to_port     = 22
                            protocol    = "tcp"
                            cidr_blocks = ["0.0.0.0/0"]
                            }},
                            http_rule = {{
                            description = "HTTP Ingress"
                            from_port   = 80
                            to_port     = 80
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

                          instance_create = {aws_ec2_create_instance}
                          instance_type = "t2.micro"

                          ami_from_instance_create = {aws_ec2_create_ami_from_instance}
                          ami_name = "my-own-ami"
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
              Ensure this project structure supports {ec2}’s configurability, extensibility, and
              reusability across diverse Terraform providers, empowering users to manage their resources through a
              single, customizable root configuration while keeping module internals robustly modular.

              finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry. and we dont need any base directory in the python code. the final
              terraform template must work very well without any error!

              Python code you give me, must have structure like that:

              import os
              project_name = "app/media/MyTerraform"
              modules_dir = os.path.join(project_name, "modules")
              ec2_dir = os.path.join(modules_dir, "ec2")

              # Create project directories
              os.makedirs(ec2_dir, exist_ok=True)

              # Create main.tf
              with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                  # any thing you need

            """
    return prompt
