def IaC_template_generator_efs(input) -> str:
    
    efs = ['aws_security_group', 'aws_efs_file_system', 'aws_efs_mount_target', 'aws_efs_backup_policy']

    aws_efs_create_file_system = 'true' if input.efs_file_system else 'false'
    aws_efs_create_mount_target = 'true' if input.efs_mount_target else 'false'
    aws_efs_create_backup_policy = 'true' if input.efs_backup_policy else 'false'
    ingress_rules = """{
  efs_rule = {
    description = "EFS Ingress"
    from_port   = 2049
    to_port     = 2049
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}"""
    egress_ruels = """ {
  from_port   = 0
  to_port     = 0
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]
}
    """
    efs = """{
  creation_token   = "terraform"
  encrypted        = true
  performance_mode = "generalPurpose"
  throughput_mode  = "elastic"
  backup_policy    = "ENABLED"
}
"""

    
    tfvars_file = f"""security_group_name = "efs_rule"
security_group_ingress_rules = {ingress_rules}
security_group_egress_rule = {egress_ruels}

file_system_create = {aws_efs_create_file_system}
efs = {efs}

mount_target_create = {aws_efs_create_mount_target}
backup_policy_create = {aws_efs_create_backup_policy}"""
    return tfvars_file