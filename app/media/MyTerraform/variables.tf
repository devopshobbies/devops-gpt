
variable "docker_host" {
  description = "Docker host URL."
  type        = string
}

variable "image" {
  description = "Docker image to use."
  type        = string
}

variable "name" {
  description = "Name of the container."
  type        = string
}

variable "ports" {
  description = "List of ports to expose."
  type        = list(string)
}

variable "env" {
  description = "Environment variables for the container."
  type        = map(string)
}
