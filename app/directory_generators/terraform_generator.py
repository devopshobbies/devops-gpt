import os
project_name = "app/media/MyTerraform"
modules_dir = os.path.join(project_name, "modules")
docker_module_dir = os.path.join(modules_dir, "docker")

# Create project directories
os.makedirs(docker_module_dir, exist_ok=True)

# Create main.tf
with open(os.path.join(project_name, "main.tf"), "w") as main_file:
    main_file.write('''provider "docker" {
  host = "unix:///var/run/docker.sock"
}

module "docker" {
  source = "./modules/docker"

  image_name         = var.image_name
  image_force_remove = var.image_force_remove
  image_build        = var.image_build
  image_count        = var.image_count

  container_image     = var.container_image
  container_name      = var.container_name
  container_hostname  = var.container_hostname
  container_restart    = var.container_restart
  container_count      = var.container_count
}
''')

# Create variables.tf
with open(os.path.join(project_name, "variables.tf"), "w") as vars_file:
    vars_file.write('''variable "image_name" {
  type = string
}

variable "image_force_remove" {
  type = bool
}

variable "image_build" {
  type = object({
    context = string
    tag    = list(string)
  })
}

variable "image_count" {
  type = number
}

variable "container_image" {
  type = string
}

variable "container_name" {
  type = string
}

variable "container_hostname" {
  type = string
}

variable "container_restart" {
  type = string
}

variable "container_count" {
  type = number
}
''')

# Create terraform.tfvars
with open(os.path.join(project_name, "terraform.tfvars"), "w") as tfvars_file:
    tfvars_file.write('''image_name = "my-image"
image_force_remove = true
image_build = {
  context = "./"
  tag    = ["my-image:latest"]
}
image_count = 0

container_image = "my-image"
container_name = "my-container"
container_hostname = "my-host"
container_restart = "always"
container_count = 1
''')

# Create versions.tf
with open(os.path.join(project_name, "versions.tf"), "w") as versions_file:
    versions_file.write('''terraform {
  required_version = ">= 1.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = ">= 2.8.0"
    }
  }
}
''')

# Create module main.tf
with open(os.path.join(docker_module_dir, "main.tf"), "w") as docker_main_file:
    docker_main_file.write('''resource "docker_image" "image" {
  count          = var.image_count
  name           = var.image_name
  force_remove   = var.image_force_remove

  build {
    context = var.image_build.context
    tag    = var.image_build.tag
  }
}

resource "docker_container" "container" {
  count       = var.container_count
  image       = var.container_image
  name        = var.container_name
  hostname    = var.container_hostname
  restart     = var.container_restart
}
''')

# Create module variables.tf
with open(os.path.join(docker_module_dir, "variables.tf"), "w") as docker_vars_file:
    docker_vars_file.write('''variable "image_name" {
  type = string
}

variable "image_force_remove" {
  type = bool
}

variable "image_build" {
  type = object({
    context = string
    tag    = list(string)
  })
}

variable "image_count" {
  type = number
}

variable "container_image" {
  type = string
}

variable "container_name" {
  type = string
}

variable "container_hostname" {
  type = string
}

variable "container_restart" {
  type = string
}

variable "container_count" {
  type = number
}
''')

# Create module terraform.tfvars
with open(os.path.join(docker_module_dir, "terraform.tfvars"), "w") as docker_tfvars_file:
    docker_tfvars_file.write('''image_name = "my-image"
image_force_remove = true
image_build = {
  context = "./"
  tag    = ["my-image:latest"]
}
image_count = 0

container_image = "my-image"
container_name = "my-container"
container_hostname = "my-host"
container_restart = "always"
container_count = 1
''')

# Create module versions.tf
with open(os.path.join(docker_module_dir, "versions.tf"), "w") as docker_versions_file:
    docker_versions_file.write('''terraform {
  required_version = ">= 1.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = ">= 2.8.0"
    }
  }
}
''')