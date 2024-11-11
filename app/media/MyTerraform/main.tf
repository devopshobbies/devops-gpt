provider "docker" {
  host = var.docker_host
}

module "docker" {
  source = "./modules/docker"
  image  = var.image
  name   = var.container_name
  ports  = var.ports
}
