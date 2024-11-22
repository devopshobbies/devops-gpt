
variable "key_pair_create" {
  type = bool
}

variable "key_pair_name" {
  type = string
}

variable "security_group_create" {
  type = bool
}

variable "security_group_name" {
  type = string
}

variable "security_group_ingress_rules" {
  type = map(object({
    description = string
    from_port = number
    to_port = number
    protocol = string
    cidr_blocks = list(string)
  }))
}

variable "security_group_egress_rule" {
  type = object({
    from_port = number
    to_port = number
    protocol = string
    cidr_blocks = list(string)
  })
}

variable "instance_create" {
  type = bool
}

variable "instance_type" {
  type = string
}

variable "ami_from_instance_create" {
  type = bool
}

variable "ami_name" {
  type = string
}
