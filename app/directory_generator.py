import os

project_name = "app/media/MyTerraform"
modules = 1

# Create project structure
os.makedirs(f"{project_name}/modules/module1", exist_ok=True)
os.makedirs(f"{project_name}/.github/workflows", exist_ok=True)

# Create main Terraform file
with open(f"{project_name}/main.tf", "w") as f:
    f.write("""
provider "aws" {
  region = "us-east-1"
}

module "module1" {
  source = "./modules/module1"
}
""")

# Create variables file
with open(f"{project_name}/variables.tf", "w") as f:
    f.write("""
variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "ami" {
  description = "AMI to use for the instance"
  default     = "ami-0c55b159cbfafe01f" # Update this to the desired AMI
}
""")

# Create outputs file
with open(f"{project_name}/outputs.tf", "w") as f:
    f.write("""
output "instance_id" {
  value = module.module1.instance_id
}
""")

# Create module files
with open(f"{project_name}/modules/module1/main.tf", "w") as f:
    f.write("""
resource "aws_instance" "this" {
  ami           = var.ami
  instance_type = var.instance_type

  tags = {
    Name = "MyTerraform-Instance"
  }
}

output "instance_id" {
  value = aws_instance.this.id
}
""")

# Create GitHub Actions workflow file
with open(f"{project_name}/.github/workflows/terraform.yml", "w") as f:
    f.write("""
name: Terraform

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
        uses: hashicorp/setup-terraform@v2
        with:
          terraform_version: 1.0.0

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: terraform plan

      - name: Terraform Apply
        run: terraform apply -auto-approve
""")