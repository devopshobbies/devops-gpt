```python
fastapi_gpt  | import os
fastapi_gpt  | 
fastapi_gpt  | def create_folder_structure(base_path):
fastapi_gpt  |     project_name = "MyTerraform"
fastapi_gpt  |     paths = [
fastapi_gpt  |         f"{base_path}/{project_name}/",
fastapi_gpt  |         f"{base_path}/{project_name}/.github/workflows/",
fastapi_gpt  |         f"{base_path}/{project_name}/modules/",
fastapi_gpt  |         f"{base_path}/{project_name}/environments/dev/",
fastapi_gpt  |         f"{base_path}/{project_name}/environments/prod/",
fastapi_gpt  |         f"{base_path}/{project_name}/variables/",
fastapi_gpt  |         f"{base_path}/{project_name}/terraform/"
fastapi_gpt  |     ]
fastapi_gpt  |     
fastapi_gpt  |     for path in paths:
fastapi_gpt  |         os.makedirs(path, exist_ok=True)
fastapi_gpt  | 
fastapi_gpt  |     with open(f"{base_path}/{project_name}/main.tf", 'w') as f:
fastapi_gpt  |         f.write("""provider "aws" {
fastapi_gpt  |   region = "us-east-1"
fastapi_gpt  | }
fastapi_gpt  | 
fastapi_gpt  | resource "aws_instance" "my_instance" {
fastapi_gpt  |   ami           = "ami-0c55b159cbfafe01c"
fastapi_gpt  |   instance_type = "t2.micro"
fastapi_gpt  | }
fastapi_gpt  | 
fastapi_gpt  | output "instance_id" {
fastapi_gpt  |   value = aws_instance.my_instance.id
fastapi_gpt  | }
fastapi_gpt  | """)
fastapi_gpt  | 
fastapi_gpt  |     with open(f"{base_path}/{project_name}/.github/workflows/terraform.yml", 'w') as f:
fastapi_gpt  |         f.write("""name: Terraform CI
fastapi_gpt  | 
fastapi_gpt  | on:
fastapi_gpt  |   push:
fastapi_gpt  |     branches:
fastapi_gpt  |       - main
fastapi_gpt  | 
fastapi_gpt  | jobs:
fastapi_gpt  |   terraform:
fastapi_gpt  |     runs-on: ubuntu-latest
fastapi_gpt  | 
fastapi_gpt  |     steps:
fastapi_gpt  |     - name: Checkout code
fastapi_gpt  |       uses: actions/checkout@v2
fastapi_gpt  | 
fastapi_gpt  |     - name: Setup Terraform
fastapi_gpt  |       uses: hashicorp/setup-terraform@v1
fastapi_gpt  |       with:
fastapi_gpt  |         terraform_version: 1.0.0
fastapi_gpt  | 
fastapi_gpt  |     - name: Terraform Init
fastapi_gpt  |       run: terraform init
fastapi_gpt  | 
fastapi_gpt  |     - name: Terraform Plan
fastapi_gpt  |       run: terraform plan
fastapi_gpt  | 
fastapi_gpt  |     - name: Terraform Apply
fastapi_gpt  |       run: terraform apply -auto-approve
fastapi_gpt  | """)
fastapi_gpt  | 
fastapi_gpt  |     with open(f"{base_path}/{project_name}/terraform/variables.tf", 'w') as f:
fastapi_gpt  |         f.write("""variable "instance_type" {
fastapi_gpt  |   description = "The type of instance to create"
fastapi_gpt  |   default     = "t2.micro"
fastapi_gpt  | }
fastapi_gpt  | 
fastapi_gpt  | variable "region" {
fastapi_gpt  |   description = "The AWS region to deploy in"
fastapi_gpt  |   default     = "us-east-1"
fastapi_gpt  | }
fastapi_gpt  | """)
fastapi_gpt  | 
fastapi_gpt  | if __name__ == "__main__":
fastapi_gpt  |     base_path = "./"
fastapi_gpt  |     create_folder_structure(base_path)