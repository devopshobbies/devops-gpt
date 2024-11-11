variable "docker_host" {
  description = "The Docker host Uri."
  type        = string
}

variable "image" {
  description = "The Docker image to use."
  type        = string
}

variable "container_name" {
  description = "The name of the Docker container."
  type        = string
}

variable "ports" {
  description = "List of ports to expose."
  type        = list(string)
}
