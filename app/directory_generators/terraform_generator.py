import os
project_name = "app/media/MyTerraform"
modules_dir = os.path.join(project_name, "modules")
docker_dir = os.path.join(modules_dir, "docker")

# Create project directories
os.makedirs(docker_dir, exist_ok=True)

# Create main.tf
with open(os.path.join(project_name, "main.tf"), "w") as main_file:
    main_file.write('''provider "docker" {
  host = "unix:///var/run/docker.sock"
}

module "docker" {
  source = "./modules/docker"

  create_image       = var.create_image
  image_name         = var.image_name
  image_force_remove  = var.image_force_remove
  image_build        = var.image_build

  create_container    = var.create_container
  container_image     = var.container_image
  container_name      = var.container_name
  container_hostname  = var.container_hostname
  container_restart    = var.container_restart
}
''')

# Create variables.tf
with open(os.path.join(project_name, "variables.tf"), "w") as variables_file:
    variables_file.write('''variable "create_image" {
  type = bool
}

variable "image_name" {
  type = string
}

variable "image_force_remove" {
  type = bool
}

variable "image_build" {
  type = object({
    context = string
    tag = list(string)
  })
}

variable "create_container" {
  type = bool
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
''')

# Create terraform.tfvars
with open(os.path.join(project_name, "terraform.tfvars"), "w") as tfvars_file:
    tfvars_file.write('''create_image = true
image_name = "my-image"
image_force_remove = true
image_build = {
  context = "./"
  tag    = ["my-image:latest"]
}

create_container = false
container_image = "my-image"
container_name = "my-container"
container_hostname = "my-host"
container_restart = "always"
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
with open(os.path.join(docker_dir, "main.tf"), "w") as module_main_file:
    module_main_file.write('''resource "docker_image" "image" {
  count        = var.create_image ? 1 : 0
  name         = var.image_name
  force_remove = var.image_force_remove

  build {
    context = var.image_build.context
    tag    = var.image_build.tag
  }
}

resource "docker_container" "container" {
  count     = var.create_container ? 1 : 0
  image     = var.container_image
  name      = var.container_name
  hostname  = var.container_hostname
  restart   = var.container_restart
}
''')

# Create module variables.tf
with open(os.path.join(docker_dir, "variables.tf"), "w") as module_variables_file:
    module_variables_file.write('''variable "create_image" {
  type = bool
}

variable "image_name" {
  type = string
}

variable "image_force_remove" {
  type = bool
}

variable "image_build" {
  type = object({
    context = string
    tag = list(string)
  })
}

variable "create_container" {
  type = bool
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
''')

# Create module terraform.tfvars
with open(os.path.join(docker_dir, "terraform.tfvars"), "w") as module_tfvars_file:
    module_tfvars_file.write('''create_image = true
image_name = "my-image"
image_force_remove = true
image_build = {
  context = "./"
  tag    = ["my-image:latest"]
}

create_container = false
container_image = "my-image"
container_name = "my-container"
container_hostname = "my-host"
container_restart = "always"
''')

# Create module versions.tf
with open(os.path.join(docker_dir, "versions.tf"), "w") as module_versions_file:
    module_versions_file.write('''terraform {
  required_version = ">= 1.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = ">= 2.8.0"
    }
  }
}
''')