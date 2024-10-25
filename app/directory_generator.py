import os

def create_terraform_project():
    project_name = "MyTerraform"
    base_dir = f"app/media/{project_name}"
    os.makedirs(base_dir, exist_ok=True)

    # main.tf
    main_tf = f"""provider "aws" {{
  region = "us-west-2"
}}

module "ec2_instance" {{
  source = "./modules/ec2"

  instance_type = "t2.micro"
  ami           = "ami-0c55b159cbfafe01e"
  tags = {{
    Name = "{project_name}-instance"
  }}
}}
"""
    with open(os.path.join(base_dir, "main.tf"), "w") as f:
        f.write(main_tf)

    # variables.tf
    variables_tf = """variable "instance_type" {
  description = "EC2 instance type"
  type        = string
}

variable "ami" {
  description = "AMI ID for EC2 instance"
  type        = string
}

variable "tags" {
  description = "Tags for the EC2 instance"
  type        = map(string)
}
"""
    with open(os.path.join(base_dir, "variables.tf"), "w") as f:
        f.write(variables_tf)

    # outputs.tf
    outputs_tf = """output "instance_id" {
  value = module.ec2_instance.instance_id
}

output "public_ip" {
  value = module.ec2_instance.public_ip
}
"""
    with open(os.path.join(base_dir, "outputs.tf"), "w") as f:
        f.write(outputs_tf)

    # Create modules directory
    modules_dir = os.path.join(base_dir, "modules")
    os.makedirs(modules_dir, exist_ok=True)

    # Create EC2 module directory
    ec2_module_dir = os.path.join(modules_dir, "ec2")
    os.makedirs(ec2_module_dir, exist_ok=True)

    # ec2/main.tf
    ec2_main_tf = """resource "aws_instance" "this" {
  ami           = var.ami
  instance_type = var.instance_type

  tags = var.tags
}
"""
    with open(os.path.join(ec2_module_dir, "main.tf"), "w") as f:
        f.write(ec2_main_tf)

    # ec2/variables.tf
    ec2_variables_tf = """variable "instance_type" {
  description = "EC2 instance type"
  type        = string
}

variable "ami" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "tags" {
  description = "Tags for the EC2 instance"
  type        = map(string)
}
"""
    with open(os.path.join(ec2_module_dir, "variables.tf"), "w") as f:
        f.write(ec2_variables_tf)

    # ec2/outputs.tf
    ec2_outputs_tf = """output "instance_id" {
  value = aws_instance.this.id
}

output "public_ip" {
  value = aws_instance.this.public_ip
}
"""
    with open(os.path.join(ec2_module_dir, "outputs.tf"), "w") as f:
        f.write(ec2_outputs_tf)

create_terraform_project()