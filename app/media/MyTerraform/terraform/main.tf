provider "aws" {
  region = "us-west-2"
}

module "ec2_instance" {
  source = "./modules/ec2"

  instance_type = "t2.micro"
  ami           = "ami-0c55b159cbfafe1f0"  # Update with a valid AMI ID
}
