resource "docker_image" "image" {
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
