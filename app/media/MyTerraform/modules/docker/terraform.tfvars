
create_image = true
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
