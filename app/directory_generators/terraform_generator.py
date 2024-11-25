import os
project_name = "app/media/MyTerraform"
modules_dir = os.path.join(project_name, "modules")
efs_dir = os.path.join(modules_dir, "efs")

# Create project directories
os.makedirs(efs_dir, exist_ok=True)

# Create main.tf
with open(os.path.join(project_name, "main.tf"), "w") as main_file:
    main_file.write('''provider "aws" {
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
''')

# Create variables.tf
with open(os.path.join(project_name, "variables.tf"), "w") as variables_file:
    variables_file.write('''variable "security_group_name" {
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
''')

# Create terraform.tfvars
with open(os.path.join(project_name, "terraform.tfvars"), "w") as tfvars_file:
    tfvars_file.write('''security_group_name = "efs_rule"
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
''')

# Create versions.tf
with open(os.path.join(project_name, "versions.tf"), "w") as versions_file:
    versions_file.write('''terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.20"
    }
  }
}
''')

# Create module main.tf
with open(os.path.join(efs_dir, "main.tf"), "w") as efs_main_file:
    efs_main_file.write('''locals {
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
''')

# Create module variables.tf
with open(os.path.join(efs_dir, "variables.tf"), "w") as efs_variables_file:
    efs_variables_file.write('''variable "security_group_name" {
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
''')

# Create module terraform.tfvars
with open(os.path.join(efs_dir, "terraform.tfvars"), "w") as efs_tfvars_file:
    efs_tfvars_file.write('''security_group_name = "efs_rule"
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
''')

# Create module versions.tf
with open(os.path.join(efs_dir, "versions.tf"), "w") as efs_versions_file:
    efs_versions_file.write('''terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.20"
    }
  }
}
''')