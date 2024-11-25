provider "aws" {
  region = "us-east-1"
}

module "efs" {
  source = "./modules/efs"

  security_group_name = var.security_group_name
  security_group_ingress_rules = var.security_group_ingress_rules
  security_group_egress_rule = var.security_group_egress_rule

  file_system_create = var.file_system_create
  efs = var.efs

  mount_target_create = var.mount_target_create
  backup_policy_create = var.backup_policy_create
}
