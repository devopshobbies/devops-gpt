
provider "aws" {
  region = "us-east-1"
}

module "module1" {
  source = "./modules/module1"
}
