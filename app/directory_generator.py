import os

project_name = "app/MyTerraform"
ci_integration = True

# Directory structure
dirs = [
    f"{project_name}/",
    f"{project_name}/.github/workflows/",
    f"{project_name}/modules/",
    f"{project_name}/environments/",
    f"{project_name}/variables/",
    f"{project_name}/main.tf",
    f"{project_name}/variables.tf",
    f"{project_name}/outputs.tf",
    f"{project_name}/terraform.tfvars"
]

# Create directory structure
for dir in dirs:
    os.makedirs(os.path.dirname(dir), exist_ok=True)
    if dir.endswith('.tf'):
        with open(dir, 'w') as f:
            if dir == f"{project_name}/main.tf":
                f.write('provider "azurerm" {\n  features {}\n}\n\n')
                f.write('resource "azurerm_resource_group" "example" {\n  name     = "example-resources"\n  location = "East US"\n}\n')
            elif dir == f"{project_name}/variables.tf":
                f.write('variable "region" {\n  description = "The Azure region to deploy to"\n  default     = "East US"\n}\n')
            elif dir == f"{project_name}/outputs.tf":
                f.write('output "resource_group_name" {\n  value = azurerm_resource_group.example.name\n}\n')
            elif dir == f"{project_name}/terraform.tfvars":
                f.write('region = "East US"\n')

if ci_integration:
    with open(f"{project_name}/.github/workflows/terraform.yml", 'w') as f:
        f.write('name: Terraform\n\n')
        f.write('on:\n  push:\n    branches:\n      - main\n\n')
        f.write('jobs:\n  terraform:\n    runs-on: ubuntu-latest\n    steps:\n')
        f.write('      - name: Checkout code\n        uses: actions/checkout@v2\n\n')
        f.write('      - name: Set up Azure CLI\n        uses: azure/setup-azure@v1\n\n')
        f.write('      - name: Terraform Init\n        run: |\n          az login --service-principal --username ${{ secrets.AZURE_CLIENT_ID }} --password ${{ secrets.AZURE_CLIENT_SECRET }} --tenant ${{ secrets.AZURE_TENANT_ID }}\n          terraform init\n\n')
        f.write('      - name: Terraform Plan\n        run: terraform plan\n\n')
        f.write('      - name: Terraform Apply\n        run: terraform apply -auto-approve\n')