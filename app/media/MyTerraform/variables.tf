
variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "ami" {
  description = "AMI to use for the instance"
  default     = "ami-0c55b159cbfafe01f" # Update this to the desired AMI
}
