
resource "docker_image" "app_image" {
  count         = var.image_count
  name          = var.image_name
  force_remove  = var.image_force_remove

  build {
    context = var.image_build.context
    tag    = var.image_build.tag
  }
}

resource "docker_container" "app_container" {
  count     = var.container_count
  image     = var.container_image
  name      = var.container_name
  hostname  = var.container_hostname
  restart   = var.container_restart
}
