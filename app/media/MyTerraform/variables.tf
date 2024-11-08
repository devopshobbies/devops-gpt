variable "aws_region" {
  description = "The AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami" {
  description = "AMI to use for the EC2 instance"
  type        = string
}

variable "key_name" {
  description = "Key pair name to access the instance"
  type        = string
}
