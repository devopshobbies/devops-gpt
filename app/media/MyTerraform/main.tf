
provider "aws" {
  region = "us-east-1"
}

module "ec2" {
  source = "./modules/ec2"

  key_pair_create = var.key_pair_create
  key_pair_name = var.key_pair_name

  security_group_create = var.security_group_create
  security_group_name = var.security_group_name
  security_group_ingress_rules = var.security_group_ingress_rules
  security_group_egress_rule = var.security_group_egress_rule

  instance_create = var.instance_create
  instance_type = var.instance_type

  ami_from_instance_create = var.ami_from_instance_create
  ami_name = var.ami_name
}
