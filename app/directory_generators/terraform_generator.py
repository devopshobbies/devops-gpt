import os
project_name = "app/media/MyTerraform"
modules_dir = os.path.join(project_name, "modules")
docker_dir = os.path.join(modules_dir, "docker")

# Create project directories
os.makedirs(docker_dir, exist_ok=True)

# Create main.tf at root
with open(os.path.join(project_name, "main.tf"), "w") as main_file:
    main_file.write('''provider "docker" {
  host = var.docker_host
}

module "docker" {
  source = "./modules/docker"
  image  = var.image
  name   = var.container_name
  ports  = var.ports
}
''')

# Create variables.tf at root
with open(os.path.join(project_name, "variables.tf"), "w") as variables_file:
    variables_file.write('''variable "docker_host" {
  description = "The Docker host Uri."
  type        = string
}

variable "image" {
  description = "The Docker image to use."
  type        = string
}

variable "container_name" {
  description = "The name of the Docker container."
  type        = string
}

variable "ports" {
  description = "List of ports to expose."
  type        = list(string)
}
''')

# Create terraform.tfvars at root
with open(os.path.join(project_name, "terraform.tfvars"), "w") as tfvars_file:
    tfvars_file.write('''docker_host = "tcp://localhost:2375"
image       = "nginx:latest"
container_name = "my_nginx"
ports      = ["80:80"]
''')

# Create versions.tf at root
with open(os.path.join(project_name, "versions.tf"), "w") as versions_file:
    versions_file.write('''terraform {
  required_version = ">= 1.0"

  required_providers {
    docker = {
      source  = "hashicorp/docker"
      version = ">= 2.0"
    }
  }
}
''')

# Create outputs.tf at root
with open(os.path.join(project_name, "outputs.tf"), "w") as outputs_file:
    outputs_file.write('''output "container_id" {
  description = "The ID of the Docker container."
  value       = module.docker.container_id
}

output "container_ip" {
  description = "The IP address of the Docker container."
  value       = module.docker.container_ip
}
''')

# Create main.tf in modules/docker
with open(os.path.join(docker_dir, "main.tf"), "w") as docker_main_file:
    docker_main_file.write('''resource "docker_container" "this" {
  name  = var.name
  image = var.image
  ports {
    internal = var.ports[0]
    external = var.ports[1]
  }
}
''')

# Create variables.tf in modules/docker
with open(os.path.join(docker_dir, "variables.tf"), "w") as docker_variables_file:
    docker_variables_file.write('''variable "image" {
  description = "The Docker image to use."
  type        = string
}

variable "name" {
  description = "The name of the Docker container."
  type        = string
}

variable "ports" {
  description = "List of ports for the container."
  type        = list(string)
}
''')

# Create terraform.tfvars in modules/docker
with open(os.path.join(docker_dir, "terraform.tfvars"), "w") as docker_tfvars_file:
    docker_tfvars_file.write('''image = "nginx:latest"
name  = "my_nginx"
ports = ["80", "80"]
''')

# Create versions.tf in modules/docker
with open(os.path.join(docker_dir, "versions.tf"), "w") as docker_versions_file:
    docker_versions_file.write('''terraform {
  required_version = ">= 1.0"

  required_providers {
    docker = {
      source  = "hashicorp/docker"
      version = ">= 2.0"
    }
  }
}
''')

# Create outputs.tf in modules/docker
with open(os.path.join(docker_dir, "outputs.tf"), "w") as docker_outputs_file:
    docker_outputs_file.write('''output "container_id" {
  description = "The ID of the Docker container."
  value       = docker_container.this.id
}

output "container_ip" {
  description = "The IP address of the Docker container."
  value       = docker_container.this.ip_address
}
''')