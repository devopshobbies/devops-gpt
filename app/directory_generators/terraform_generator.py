import os
project_name = "app/media/MyTerraform"
modules_dir = os.path.join(project_name, "modules")
ec2_dir = os.path.join(modules_dir, "ec2")

# Create project directories
os.makedirs(ec2_dir, exist_ok=True)

# Create main.tf
with open(os.path.join(project_name, "main.tf"), "w") as main_file:
    main_file.write('''
provider "aws" {
  region = "us-east-1"
}

module "ec2" {
  source = "./modules/ec2"

  key_pair_create = var.key_pair_create
  key_pair_name = var.key_pair_name

  security_group_create = var.security_group_create
  security_group_name = var.security_group_name
  security_group_ingress_rules = var.security_group_ingress_rules
  security_group_egress_rule = var.security_group_egress_rule

  instance_create = var.instance_create
  instance_type = var.instance_type

  ami_from_instance_create = var.ami_from_instance_create
  ami_name = var.ami_name
}
''')

# Create variables.tf
with open(os.path.join(project_name, "variables.tf"), "w") as variables_file:
    variables_file.write('''
variable "key_pair_create" {
  type = bool
}

variable "key_pair_name" {
  type = string
}

variable "security_group_create" {
  type = bool
}

variable "security_group_name" {
  type = string
}

variable "security_group_ingress_rules" {
  type = map(object({
    description = string
    from_port = number
    to_port = number
    protocol = string
    cidr_blocks = list(string)
  }))
}

variable "security_group_egress_rule" {
  type = object({
    from_port = number
    to_port = number
    protocol = string
    cidr_blocks = list(string)
  })
}

variable "instance_create" {
  type = bool
}

variable "instance_type" {
  type = string
}

variable "ami_from_instance_create" {
  type = bool
}

variable "ami_name" {
  type = string
}
''')

# Create terraform.tfvars
with open(os.path.join(project_name, "terraform.tfvars"), "w") as tfvars_file:
    tfvars_file.write('''
key_pair_create = true
key_pair_name = "ec2"

security_group_create = true
security_group_name = "my_rules"
security_group_ingress_rules = {
  ssh_rule = {
    description = "SSH Ingress"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  },
  http_rule = {
    description = "HTTP Ingress"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
security_group_egress_rule = {
  from_port   = 0
  to_port     = 0
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]
}

instance_create = false
instance_type = "t2.micro"

ami_from_instance_create = true
ami_name = "my-own-ami"
''')

# Create versions.tf
with open(os.path.join(project_name, "versions.tf"), "w") as versions_file:
    versions_file.write('''
terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.20"
    }
  }
}
''')

# Create ec2 module files
with open(os.path.join(ec2_dir, "terraform.pub"), "w") as pub_file:
    pass

with open(os.path.join(ec2_dir, "main.tf"), "w") as ec2_main_file:
    ec2_main_file.write('''
data "aws_ami" "linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023*kernel-6.1-x86_64"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_key_pair" "key_pair" {
  count = var.key_pair_create ? 1 : 0
  key_name = var.key_pair_name
  public_key = file("${path.module}/terraform.pub")
}

resource "aws_security_group" "security_group" {
  count = var.security_group_create ? 1 : 0
  name  = var.security_group_name

  dynamic "ingress" {
    for_each = var.security_group_ingress_rules
    content {
      description = ingress.value["description"]
      from_port   = ingress.value["from_port"]
      to_port     = ingress.value["to_port"]
      protocol    = ingress.value["protocol"]
      cidr_blocks = ingress.value["cidr_blocks"]
    }
  }

  egress {
    from_port   = var.security_group_egress_rule["from_port"]
    to_port     = var.security_group_egress_rule["to_port"]
    protocol    = var.security_group_egress_rule["protocol"]
    cidr_blocks = var.security_group_egress_rule["cidr_blocks"]
  }
}

resource "aws_instance" "instance" {
  count = var.instance_create ? 1 : 0
  ami = data.aws_ami.linux.id
  instance_type = var.instance_type
  key_name = var.key_pair_create ? aws_key_pair.key_pair[0].key_name : null
  vpc_security_group_ids = var.security_group_create ? [aws_security_group.security_group[0].id] : null
}

resource "aws_ami_from_instance" "ami" {
  count = var.instance_create && var.ami_from_instance_create ? 1 : 0
  name = var.ami_name
  source_instance_id = aws_instance.instance[0].id
}
''')

with open(os.path.join(ec2_dir, "variables.tf"), "w") as ec2_variables_file:
    ec2_variables_file.write('''
variable "key_pair_create" {
  type = bool
}

variable "key_pair_name" {
  type = string
}

variable "security_group_create" {
  type = bool
}

variable "security_group_name" {
  type = string
}

variable "security_group_ingress_rules" {
  type = map(object({
    description = string
    from_port = number
    to_port = number
    protocol = string
    cidr_blocks = list(string)
  }))
}

variable "security_group_egress_rule" {
  type = object({
    from_port = number
    to_port = number
    protocol = string
    cidr_blocks = list(string)
  })
}

variable "instance_create" {
  type = bool
}

variable "instance_type" {
  type = string
}

variable "ami_from_instance_create" {
  type = bool
}

variable "ami_name" {
  type = string
}
''')

with open(os.path.join(ec2_dir, "terraform.tfvars"), "w") as ec2_tfvars_file:
    ec2_tfvars_file.write('''
key_pair_create = true
key_pair_name = "ec2"

security_group_create = true
security_group_name = "my_rules"
security_group_ingress_rules = {
  ssh_rule = {
    description = "SSH Ingress"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  },
  http_rule = {
    description = "HTTP Ingress"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
security_group_egress_rule = {
  from_port   = 0
  to_port     = 0
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]
}

instance_create = false
instance_type = "t2.micro"

ami_from_instance_create = true
ami_name = "my-own-ami"
''')

with open(os.path.join(ec2_dir, "versions.tf"), "w") as ec2_versions_file:
    ec2_versions_file.write('''
terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.20"
    }
  }
}
''')