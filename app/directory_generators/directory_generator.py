import os

project_name = "MyTerraform"
base_dir = "app/media/"
terraform_dir = os.path.join(base_dir, project_name, "terraform")
modules_dir = os.path.join(terraform_dir, "modules")
ci_dir = os.path.join(base_dir, project_name, ".github", "workflows")

os.makedirs(terraform_dir, exist_ok=True)
os.makedirs(modules_dir, exist_ok=True)
os.makedirs(ci_dir, exist_ok=True)

# Create main.tf
with open(os.path.join(terraform_dir, "main.tf"), 'w') as f:
    f.write(f'''provider "aws" {{
  region = "us-west-2"
}}

module "ec2_instance" {{
  source = "./modules/ec2"

  instance_type = "t2.micro"
  ami           = "ami-0c55b159cbfafe1f0"  # Update with a valid AMI ID
}}
''')

# Create variables.tf
with open(os.path.join(terraform_dir, "variables.tf"), 'w') as f:
    f.write('''variable "instance_type" {
  description = "Type of EC2 instance"
  type        = string
  default     = "t2.micro"
}

variable "ami" {
  description = "AMI ID for the EC2 instance"
  type        = string
}
''')

# Create outputs.tf
with open(os.path.join(terraform_dir, "outputs.tf"), 'w') as f:
    f.write('''output "instance_id" {
  value = module.ec2_instance.instance_id
}
''')

# Create EC2 module directory
ec2_module_dir = os.path.join(modules_dir, "ec2")
os.makedirs(ec2_module_dir, exist_ok=True)

# Create ec2/main.tf for the module
with open(os.path.join(ec2_module_dir, "main.tf"), 'w') as f:
    f.write('''resource "aws_instance" "this" {
  ami           = var.ami
  instance_type = var.instance_type

  tags = {
    Name = "TerraformEC2Instance"
  }
}

output "instance_id" {
  value = aws_instance.this.id
}
''')

# Create CI pipeline file
with open(os.path.join(ci_dir, "terraform.yml"), 'w') as f:
    f.write('''name: Terraform

on:
  push:
    branches:
      - main

jobs:
  terraform:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
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
''')