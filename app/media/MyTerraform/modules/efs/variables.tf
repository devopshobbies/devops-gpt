
variable "security_group_name" {
  type = string
}

variable "security_group_ingress_rules" {
  type = map(object({
    description = string
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
  }))
}

variable "security_group_egress_rule" {
  type = object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
  })
}

variable "file_system_create" {
  type = bool
}

variable "efs" {
  type = object({
    creation_token   = string
    encrypted        = bool
    performance_mode = string
    throughput_mode  = string
    backup_policy    = string
  })
}

variable "mount_target_create" {
  type = bool
}

variable "backup_policy_create" {
  type = bool
}
