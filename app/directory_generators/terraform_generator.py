import os
project_name = "app/media/MyTerraform"
modules_dir = os.path.join(project_name, "modules")
docker_container_dir = os.path.join(modules_dir, "docker_container")

# Create project directories
os.makedirs(docker_container_dir, exist_ok=True)

# Create main.tf
with open(os.path.join(project_name, "main.tf"), "w") as main_file:
    main_file.write('''
provider "docker" {
  host = var.docker_host
}

module "docker_container" {
  source = "./modules/docker_container"

  image = var.image
  name  = var.name
  ports = var.ports
  env   = var.env
}

''')

# Create variables.tf
with open(os.path.join(project_name, "variables.tf"), "w") as vars_file:
    vars_file.write('''
variable "docker_host" {
  description = "Docker host URL."
  type        = string
}

variable "image" {
  description = "Docker image to use."
  type        = string
}

variable "name" {
  description = "Name of the container."
  type        = string
}

variable "ports" {
  description = "List of ports to expose."
  type        = list(string)
}

variable "env" {
  description = "Environment variables for the container."
  type        = map(string)
}
''')

# Create terraform.tfvars
with open(os.path.join(project_name, "terraform.tfvars"), "w") as tfvars_file:
    tfvars_file.write('''
docker_host = "tcp://localhost:2375"
image      = "nginx:latest"
name       = "my-nginx-container"
ports      = ["80:80"]
env        = { "MY_ENV_VAR" = "value" }
''')

# Create versions.tf
with open(os.path.join(project_name, "versions.tf"), "w") as versions_file:
    versions_file.write('''
terraform {
  required_version = ">= 1.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = ">= 2.8.0"
    }
  }
}

''')

# Create outputs.tf
with open(os.path.join(project_name, "outputs.tf"), "w") as outputs_file:
    outputs_file.write('''
output "container_id" {
  description = "The ID of the Docker container."
  value       = module.docker_container.container_id
}

output "container_ip" {
  description = "The IP address of the Docker container."
  value       = module.docker_container.container_ip
}
''')

# Create module files
# Create docker_container/main.tf
with open(os.path.join(docker_container_dir, "main.tf"), "w") as module_main_file:
    module_main_file.write('''
resource "docker_container" "app" {
  image = var.image
  name  = var.name
  ports {
    internal = 80
    external = var.ports[0]
  }
  env = var.env
}
''')

# Create docker_container/variables.tf
with open(os.path.join(docker_container_dir, "variables.tf"), "w") as module_vars_file:
    module_vars_file.write('''
variable "image" {
  description = "Docker image."
  type        = string
}

variable "name" {
  description = "Container name."
  type        = string
}

variable "ports" {
  description = "List of exposed ports."
  type        = list(string)
}

variable "env" {
  description = "Map of environment variables."
  type        = map(string)
}
''')

# Create docker_container/terraform.tfvars
with open(os.path.join(docker_container_dir, "terraform.tfvars"), "w") as module_tfvars_file:
    module_tfvars_file.write('''
image = "nginx:latest"
name  = "my-nginx-container"
ports = ["80:80"]
env   = { "MY_ENV_VAR" = "value" }
''')

# Create docker_container/versions.tf
with open(os.path.join(docker_container_dir, "versions.tf"), "w") as module_versions_file:
    module_versions_file.write('''
terraform {
  required_version = ">= 1.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = ">= 2.8.0"
    }
  }
}
''')

# Create docker_container/outputs.tf
with open(os.path.join(docker_container_dir, "outputs.tf"), "w") as module_outputs_file:
    module_outputs_file.write('''
output "container_id" {
  description = "The ID of the Docker container."
  value       = docker_container.app.id
}

output "container_ip" {
  description = "The IP address of the Docker container."
  value       = docker_container.app.ip_address
}
''')