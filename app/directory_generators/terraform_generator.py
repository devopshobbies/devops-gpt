import os

project_name = "MyTerraform"
modules = ["ec2"]

# Create project structure
os.makedirs(f"app/media/{project_name}", exist_ok=True)
os.makedirs(f"app/media/{project_name}/modules/{modules[0]}", exist_ok=True)

# Create main.tf
with open(f"app/media/{project_name}/main.tf", "w") as f:
    f.write(f"""
terraform {{
  required_providers {{
    aws = {{
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }}
  }}

  required_version = ">= 0.12"
}}

provider "aws" {{
  region = "us-east-1"
}}

module "{modules[0]}" {{
  source = "./modules/{modules[0]}"
  instance_type = "t2.micro"
  ami = "ami-0c55b159cbfafe1f0" # Example AMI
}}
""")

# Create modules/ec2/variables.tf
with open(f"app/media/{project_name}/modules/{modules[0]}/variables.tf", "w") as f:
    f.write(f"""
variable "instance_type" {{
  description = "The type of instance to create"
  type        = string
  default     = "t2.micro"
}}

variable "ami" {{
  description = "The AMI to use for the instance"
  type        = string
  default     = "ami-0c55b159cbfafe1f0" # Example AMI
}}
""")

# Create modules/ec2/main.tf
with open(f"app/media/{project_name}/modules/{modules[0]}/main.tf", "w") as f:
    f.write(f"""
resource "aws_instance" "app_instance" {{
  ami           = var.ami
  instance_type = var.instance_type

  tags = {{
    Name = "MyTerraformInstance"
  }}
}}
""")

# Create .github/workflows/ci.yml
os.makedirs(f"app/media/{project_name}/.github/workflows", exist_ok=True)
with open(f"app/media/{project_name}/.github/workflows/ci.yml", "w") as f:
    f.write(f"""
name: Terraform CI

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
        uses: hashicorp/setup-terraform@v2.0.0
        with:
          terraform_version: 1.0.0

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: terraform plan

      - name: Terraform Apply
        run: terraform apply -auto-approve
""")