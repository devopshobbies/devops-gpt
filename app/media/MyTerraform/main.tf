
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
  region = "us-east-1"
}

module "ec2" {
  source = "./modules/ec2"
  instance_type = "t2.micro"
  ami = "ami-0c55b159cbfafe1f0" # Example AMI
}
