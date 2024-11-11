resource "docker_container" "this" {
  name  = var.name
  image = var.image
  ports {
    internal = var.ports[0]
    external = var.ports[1]
  }
}
