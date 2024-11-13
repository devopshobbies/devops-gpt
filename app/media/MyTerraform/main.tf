
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

