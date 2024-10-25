provider "aws" {
  region = "us-west-2"
}

module "ec2_instance" {
  source = "./modules/ec2"

  instance_type = "t2.micro"
  ami           = "ami-0c55b159cbfafe01e"
  tags = {
    Name = "MyTerraform-instance"
  }
}
