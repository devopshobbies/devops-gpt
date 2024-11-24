def IaC_template_generator_elb(input) -> str:
    # Define the list of ELB resources and their modules
    elb = [
        'aws_elb',
        'aws_elb_create_security_group',
        'aws_elb_create_target_group',
        'aws_elb_create_listener_rule',
        'aws_elb_create_launch_configuration',
        'aws_elb_create_autoscaling_group',
        'aws_elb_create_autoscaling_group_attachment',
        'aws_elb_create_autoscaling_policy'
    ]

    # Set boolean flags based on input
    aws_elb_create_security_group = 'true' if input.security_group else 'false'
    aws_elb_create_target_group = 'true' if input.target_group else 'false'
    aws_elb_create_listener = 'true' if input.listener else 'false'
    aws_elb_create_launch_config = 'true' if input.launch_configuration else 'false'
    aws_elb_create_asg = 'true' if input.autoscaling_group else 'false'
    aws_elb_create_asg_attachment = 'true' if input.asg_attachment else 'false'
    aws_elb_create_asg_policy = 'true' if input.asg_policy else 'false'

    tfvars_content = f"""
    # Resource creation flags
    create_security_group        = {aws_elb_create_security_group}
    create_target_group         = {aws_elb_create_target_group}
    create_listener_rule        = {aws_elb_create_listener}
    create_launch_configuration = {aws_elb_create_launch_config}
    create_autoscaling_group    = {aws_elb_create_asg}
    create_asg_attachment       = {aws_elb_create_asg_attachment}
    create_autoscaling_policy   = {aws_elb_create_asg_policy}
    """

    # Add variables definitions in variables.tf
    variables_content = """
    variable "create_security_group" {
      description = "Whether to create security group"
      type        = bool
      default     = true
    }

    variable "create_target_group" {
      description = "Whether to create target group"
      type        = bool
      default     = true
    }

    variable "create_listener_rule" {
      description = "Whether to create listener rule"
      type        = bool
      default     = true
    }

    variable "create_launch_configuration" {
      description = "Whether to create launch configuration"
      type        = bool
      default     = true
    }

    variable "create_autoscaling_group" {
      description = "Whether to create autoscaling group"
      type        = bool
      default     = true
    }

    variable "create_asg_attachment" {
      description = "Whether to create ASG attachment"
      type        = bool
      default     = true
    }

    variable "create_autoscaling_policy" {
      description = "Whether to create autoscaling policy"
      type        = bool
      default     = true
    }
    """

    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions ELB resources using a modular structure. Only provide Python code, no explanations or
              markdown formatting. The project should be organized as follows:

              1. terraform.tfvars with the following content:
              {tfvars_content}

              2. variables.tf with the following content:
              {variables_content}

              1. Root Directory Structure:
                  app/media/MyTerraform/
                  ├── main.tf
                  ├── variables.tf
                  ├── terraform.tfvars
                  ├── versions.tf
                  └── modules/
                      ├── security_group/
                      │   ├── main.tf
                      │   ├── variables.tf
                      │   └── outputs.tf
                      ├── target_group/
                      │   ├── main.tf
                      │   ├── variables.tf
                      │   └── outputs.tf
                      ├── listener/
                      │   ├── main.tf
                      │   ├── variables.tf
                      │   └── outputs.tf
                      ├── launch_configuration/
                      │   ├── main.tf
                      │   ├── variables.tf
                      │   └── outputs.tf
                      └── autoscaling/
                          ├── main.tf
                          ├── variables.tf
                          └── outputs.tf

              2. Root main.tf:
                  ```
                  provider "aws" {{
                    region = "us-east-1"
                  }}

                  # Data sources for VPC and Subnets
                  data "aws_vpc" "default" {{
                    default = true
                  }}

                  data "aws_subnets" "default" {{
                    filter {{
                      name   = "vpc-id"
                      values = [data.aws_vpc.default.id]
                    }}
                  }}

                  # Security Group Module
                  module "security_group" {{
                    source = "./modules/security_group"
                    count  = var.create_security_group ? 1 : 0

                    vpc_id               = data.aws_vpc.default.id
                    security_ingress_rules = var.security_ingress_rules
                  }}

                  # Target Group Module
                  module "target_group" {{
                    source = "./modules/target_group"
                    count  = var.create_target_group ? 1 : 0

                    name             = var.target_group.name
                    port             = var.target_group.port
                    protocol         = var.target_group.protocol
                    vpc_id           = data.aws_vpc.default.id
                    target_type      = var.target_group.type
                    protocol_version = var.target_group.protocol_version
                    stickiness      = var.stickiness
                  }}

                  # Listener Module
                  module "listener" {{
                    source = "./modules/listener"
                    count  = var.create_listener_rule && var.create_target_group ? 1 : 0

                    target_group_arn  = module.target_group[0].target_group_arn
                    port              = var.load_balancer_listener.port
                    protocol          = var.load_balancer_listener.protocol
                    rule_priority     = var.rule_priority
                  }}

                  # Launch Configuration Module
                  module "launch_configuration" {{
                    source = "./modules/launch_configuration"
                    count  = var.create_launch_configuration ? 1 : 0

                    name_prefix     = var.lc_name_prefix
                    instance_type   = var.lc_instance_type
                    security_groups = var.create_security_group ? [module.security_group[0].security_group_id] : []
                  }}

                  # Autoscaling Module
                  module "autoscaling" {{
                    source = "./modules/autoscaling"
                    count  = var.create_autoscaling_group ? 1 : 0

                    name                = var.autoscaling_group.name
                    max_size            = var.autoscaling_group.max_size
                    min_size            = var.autoscaling_group.min_size
                    desired_capacity    = var.autoscaling_group.desired_capacity
                    vpc_zone_identifier = data.aws_subnets.default.ids
                    target_group_arns   = var.create_target_group ? [module.target_group[0].target_group_arn] : []
                    launch_configuration_name = module.launch_configuration[0].launch_configuration_id

                    create_policy = var.create_autoscaling_policy
                    policy_config = var.autoscaling_policy
                  }}
                  ```

              3. Module Structure:

                  a. security_group/main.tf:
                  ```
                  resource "aws_security_group" "this" {{
                    name_prefix = "elb-sg-"
                    vpc_id     = var.vpc_id

                    dynamic "ingress" {{
                      for_each = var.security_ingress_rules
                      content {{
                        from_port   = ingress.value["from_port"]
                        to_port     = ingress.value["to_port"]
                        protocol    = ingress.value["protocol"]
                        cidr_blocks = ingress.value["cidr_blocks"]
                        description = ingress.value["description"]
                      }}
                    }}

                    egress {{
                      from_port   = 0
                      to_port     = 0
                      protocol    = "-1"
                      cidr_blocks = ["0.0.0.0/0"]
                    }}
                  }}
                  ```


                  b. target_group/main.tf:
                  ```
                  resource "aws_lb_target_group" "this" {{
                    name             = var.name
                    port             = var.port
                    protocol         = var.protocol
                    vpc_id           = var.vpc_id
                    target_type      = var.target_type
                    protocol_version = var.protocol_version

                    stickiness {{
                      type            = var.stickiness.type
                      cookie_duration = var.stickiness.cookie_duration
                      cookie_name     = var.stickiness.cookie_name
                      enabled         = var.stickiness.enabled
                    }}
                  }}
                  ```

                  c. listener/main.tf:
                  ```
                  resource "aws_lb_listener" "this" {{
                    load_balancer_arn = var.load_balancer_arn
                    port              = var.port
                    protocol          = var.protocol

                    default_action {{
                      type             = "forward"
                      target_group_arn = var.target_group_arn
                    }}
                  }}

                  resource "aws_lb_listener_rule" "this" {{
                    listener_arn = aws_lb_listener.this.arn
                    priority     = var.rule_priority

                    action {{
                      type = "fixed-response"
                      fixed_response {{
                        content_type = "text/plain"
                        message_body = "Custom Error, Page Not Found!"
                        status_code  = "404"
                      }}
                    }}

                    condition {{
                      path_pattern {{
                        values = ["/error"]
                      }}
                    }}
                  }}
                  ```

                  e. launch_configuration/main.tf:
                  ```
                  data "aws_ami" "amazon_linux_2" {{
                    most_recent = true
                    owners      = ["amazon"]

                    filter {{
                      name   = "name"
                      values = ["al2023-ami-2023*"]
                    }}

                    filter {{
                      name   = "virtualization-type"
                      values = ["hvm"]
                    }}
                  }}

                  resource "aws_launch_configuration" "this" {{
                    name_prefix     = var.name_prefix
                    image_id       = data.aws_ami.amazon_linux_2.id
                    instance_type  = var.instance_type
                    security_groups = var.security_groups

                    lifecycle {{
                      create_before_destroy = true
                    }}
                  }}
                  ```

                  f. autoscaling/main.tf:
                  ```
                  resource "aws_autoscaling_group" "this" {{
                    name                = var.name
                    max_size            = var.max_size
                    min_size            = var.min_size
                    desired_capacity    = var.desired_capacity
                    vpc_zone_identifier = var.vpc_zone_identifier
                    target_group_arns   = var.target_group_arns
                    launch_configuration = var.launch_configuration_name

                    tag {{
                      key                 = "Environment"
                      value               = "production"
                      propagate_at_launch = true
                    }}
                  }}

                  resource "aws_autoscaling_policy" "this" {{
                    count = var.create_policy ? 1 : 0

                    name                   = var.policy_config.autoscaling_policy_name
                    autoscaling_group_name = aws_autoscaling_group.this.name
                    policy_type           = var.policy_config.policy_type

                    target_tracking_configuration {{
                      predefined_metric_specification {{
                        predefined_metric_type = var.policy_config.predefined_metric_type
                      }}
                      target_value = var.policy_config.target_value
                    }}
                  }}
                  ```

              4. Each module should have its own variables.tf and outputs.tf files with appropriate variable definitions
                 and outputs that match the provided root variables.tf structure.

              5. Use the same versions.tf content across all modules:
                  ```
                  terraform {{
                    required_version = ">= 1.0"

                    required_providers {{
                      aws = {{
                        source  = "hashicorp/aws"
                        version = ">= 5.20"
                      }}
                    }}
                  }}
                  ```

              Create appropriate outputs.tf files for each module to expose necessary resource attributes.
              Use the provided variables.tf content as a base for module variables, breaking them down appropriately
              for each module. Ensure that each module only receives the variables it needs for its specific resources.

              Ensure this project structure supports {elb}'s configurebility, extensibility, and
              reusability across diverse Terraform providers. It empowers users to manage their resources through a
              single, customizable root configuration while maintaining modular module internals.
              finally, just give me a Python code without any note to generate a project folder with the given
              schema without ``a Python entry. and we don't need any base directory in the Python code. the final
              terraform template must work very well without any errors!

              The Python code you give me, must have a structure like this:

              import os
              project_name = "app/media/MyTerraform"
              modules_dir = os.path.join(project_name, "modules")
              ec2_dir = os.path.join(modules_dir, "elb")

              # Create project directories
              os.makedirs(elb_dir, exist_ok=True)

              # Create main.tf
              with open(os.path.join(project_name, "main.tf"), "w") as main_file:

              """

    return prompt
