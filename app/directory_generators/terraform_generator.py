import os

project_name = "app/media/MyTerraform"
base_directory = project_name.replace("/", os.sep)
modules_directory = os.path.join(base_directory, "modules")
ci_directory = os.path.join(base_directory, ".github", "workflows")

os.makedirs(modules_directory, exist_ok=True)
os.makedirs(ci_directory, exist_ok=True)

terraform_main = f"""provider "aws" {{
  region = "us-east-1"
}}

resource "aws_instance" "web" {{
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {{
    Name = "MyEC2Instance"
  }}
}}
"""

terraform_variables = """variable "region" {{
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}}

variable "instance_type" {{
  description = "EC2 Instance type"
  type        = string
  default     = "t2.micro"
}}

variable "ami" {{
  description = "AMI ID"
  type        = string
  default     = "ami-0c55b159cbfafe1f0"
}}
"""

github_actions = """name: Terraform CI

on:
  push:
    branches:
      - main
  pull_request:
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
        run: terraform plan

      - name: Terraform Apply
        run: terraform apply -auto-approve
        env:
          TF_VAR_region: ${{ secrets.AWS_REGION }}
          TF_VAR_instance_type: ${{ secrets.AWS_INSTANCE_TYPE }}
          TF_VAR_ami: ${{ secrets.AWS_AMI }}
"""

with open(os.path.join(base_directory, "main.tf"), "w") as f:
    f.write(terraform_main)

with open(os.path.join(base_directory, "variables.tf"), "w") as f:
    f.write(terraform_variables)

with open(os.path.join(ci_directory, "terraform-ci.yml"), "w") as f:
    f.write(github_actions)