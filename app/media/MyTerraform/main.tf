provider "docker" {
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
