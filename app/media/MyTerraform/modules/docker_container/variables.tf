
variable "image" {
  description = "Docker image."
  type        = string
}

variable "name" {
  description = "Container name."
  type        = string
}

variable "ports" {
  description = "List of exposed ports."
  type        = list(string)
}

variable "env" {
  description = "Map of environment variables."
  type        = map(string)
}
