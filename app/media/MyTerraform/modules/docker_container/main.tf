
resource "docker_container" "app" {
  image = var.image
  name  = var.name
  ports {
    internal = 80
    external = var.ports[0]
  }
  env = var.env
}
