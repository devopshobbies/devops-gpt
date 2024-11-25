locals {
  default_efs_lifecycle_policies = {
    transition_to_ia                    = "AFTER_14_DAYS",
    transition_to_primary_storage_class = "AFTER_1_ACCESS",
  }
}

data "aws_availability_zones" "available_zones" {
  state = "available"
}

data "aws_vpc" "default_vpc" {
  default = true
}

data "aws_subnets" "subnets_ids" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default_vpc.id]
  }
}

resource "aws_security_group" "security_group" {
  count = var.file_system_create && var.mount_target_create ? 1 : 0
  name = var.security_group_name
  description = "Security group for EFS mount targets"
  vpc_id = data.aws_vpc.default_vpc.id

  dynamic "ingress" {
    for_each = var.security_group_ingress_rules
    content {
      description = ingress.value["description"]
      from_port   = ingress.value["from_port"]
      to_port     = ingress.value["to_port"]
      protocol    = ingress.value["protocol"]
      cidr_blocks = ingress.value["cidr_blocks"]
    }
  }

  egress {
    from_port   = var.security_group_egress_rule["from_port"]
    to_port     = var.security_group_egress_rule["to_port"]
    protocol    = var.security_group_egress_rule["protocol"]
    cidr_blocks = var.security_group_egress_rule["cidr_blocks"]
  }
}

resource "aws_efs_file_system" "filesystem" {
  count = var.file_system_create ? 1 : 0
  creation_token = var.efs["creation_token"]
  encrypted = var.efs["encrypted"]
  performance_mode = var.efs["performance_mode"]
  throughput_mode  = var.efs["throughput_mode"]

  lifecycle_policy {
    transition_to_ia = lookup(local.default_efs_lifecycle_policies, "transition_to_ia", null)
  }

  lifecycle_policy {
    transition_to_primary_storage_class = lookup(local.default_efs_lifecycle_policies, "transition_to_primary_storage_class", null)
  }

  tags = {
    Name = "terraform-efs"
  }
}

resource "aws_efs_mount_target" "mount_target" {
  count = var.file_system_create && var.mount_target_create ? length(data.aws_availability_zones.available_zones.names) : 0
  file_system_id = aws_efs_file_system.filesystem[0].id
  subnet_id = data.aws_subnets.subnets_ids.ids[count.index]
  security_groups = [aws_security_group.security_group[0].id]
}

resource "aws_efs_backup_policy" "backup_policy" {
  count = var.file_system_create && var.backup_policy_create ? 1 : 0
  file_system_id = aws_efs_file_system.filesystem[0].id

  backup_policy {
    status = var.efs["backup_policy"]
  }
}
