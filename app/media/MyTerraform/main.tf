terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
  required_version = ">= 0.12"
}

provider "aws" {
  region = var.aws_region
}

module "ec2_module" {
  source = "./modules/ec2-module"
  instance_type = var.instance_type
  ami = var.ami
  key_name = var.key_name
}
