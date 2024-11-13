image_name = "my-image"
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
