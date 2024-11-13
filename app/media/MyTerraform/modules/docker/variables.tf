variable "image_name" {
  type = string
}

variable "image_force_remove" {
  type = bool
}

variable "image_build" {
  type = object({
    context = string
    tag    = list(string)
  })
}

variable "image_count" {
  type = number
}

variable "container_image" {
  type = string
}

variable "container_name" {
  type = string
}

variable "container_hostname" {
  type = string
}

variable "container_restart" {
  type = string
}

variable "container_count" {
  type = number
}
