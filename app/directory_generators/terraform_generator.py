import os

project_name = "app/media/MyTerraform"
module_name = "ec2-module"

directories = [
    project_name,
    os.path.join(project_name, "modules"),
    os.path.join(project_name, "modules", module_name),
    os.path.join(project_name, "env"),
    os.path.join(project_name, "env", "dev"),
    os.path.join(project_name, "env", "prod"),
    os.path.join(project_name, ".github"),
    os.path.join(project_name, ".github", "workflows")
]

files = {
    os.path.join(project_name, "main.tf"): """terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
  required_version = ">= 0.12"
}

provider "aws" {
  region = var.aws_region
}

module "ec2_module" {
  source = "./modules/ec2-module"
  instance_type = var.instance_type
  ami = var.ami
  key_name = var.key_name
}
""",
    os.path.join(project_name, "variables.tf"): """variable "aws_region" {
  description = "The AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami" {
  description = "AMI to use for the EC2 instance"
  type        = string
}

variable "key_name" {
  description = "Key pair name to access the instance"
  type        = string
}
""",
    os.path.join(project_name, "outputs.tf"): """output "instance_id" {
  value = module.ec2_module.instance_id
}
""",
    os.path.join(project_name, "modules", module_name, "main.tf"): """resource "aws_instance" "example" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "MyInstance"
  }
}

output "instance_id" {
  value = aws_instance.example.id
}
""",
    os.path.join(project_name, "env", "dev", "terraform.tfvars"): """aws_region = "us-east-1"
instance_type = "t2.micro"
ami = "<your-ami-id>"
key_name = "<your-key-name>"
""",
    os.path.join(project_name, "env", "prod", "terraform.tfvars"): """aws_region = "us-east-1"
instance_type = "t2.micro"
ami = "<your-ami-id>"
key_name = "<your-key-name>"
""",
    os.path.join(project_name, ".github", "workflows", "terraform.yml"): """name: Terraform

on:
  push:
    branches:
      - main

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Terraform
        uses: hashicorp/setup-terraform@v1
        with:
          terraform_version: 1.0.0

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: terraform plan -var-file=env/dev/terraform.tfvars

      - name: Terraform Apply
        run: terraform apply -auto-approve -var-file=env/dev/terraform.tfvars
"""
}

for directory in directories:
    os.makedirs(directory, exist_ok=True)

for file_path, file_content in files.items():
    with open(file_path, 'w') as file:
        file.write(file_content)