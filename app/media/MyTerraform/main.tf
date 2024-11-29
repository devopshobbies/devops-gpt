provider "docker" {
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
