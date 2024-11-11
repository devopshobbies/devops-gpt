variable "image" {
  description = "The Docker image to use."
  type        = string
}

variable "name" {
  description = "The name of the Docker container."
  type        = string
}

variable "ports" {
  description = "List of ports for the container."
  type        = list(string)
}
