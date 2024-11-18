
variable "key_pair_create" {
  description = "Create Key Pair"
  type        = bool
}

variable "key_pair_name" {
  description = "Key Pair Name"
  type        = string
}

variable "security_group_create" {
  description = "Create Security Group"
  type        = bool
}

variable "security_group_name" {
  description = "Security Group Name"
  type        = string
}

variable "security_group_ingress_rules" {
  description = "Security Group Ingress Rules"
  type        = map(object({
    description = string
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
  }))
}

variable "security_group_egress_rule" {
  description = "Security Group Egress Rule"
  type        = object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
  })
}

variable "instance_create" {
  description = "Create EC2 Instance"
  type        = bool
}

variable "instance_type" {
  description = "EC2 Instance Type"
  type        = string
}
