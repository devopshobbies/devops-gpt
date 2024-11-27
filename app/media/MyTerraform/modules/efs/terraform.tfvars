security_group_name = "efs_rule"
security_group_ingress_rules = {
  efs_rule = {
    description = "EFS Ingress"
    from_port   = 2049
    to_port     = 2049
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
security_group_egress_rule = {
  from_port   = 0
  to_port     = 0
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]
}

file_system_create = true
efs = {
  creation_token   = "terraform"
  encrypted        = true
  performance_mode = "generalPurpose"
  throughput_mode  = "elastic"
  backup_policy    = "ENABLED"
}

mount_target_create = true
backup_policy_create = false
