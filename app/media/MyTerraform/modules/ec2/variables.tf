
variable "instance_type" {
  description = "The type of instance to create"
  type        = string
  default     = "t2.micro"
}

variable "ami" {
  description = "The AMI to use for the instance"
  type        = string
  default     = "ami-0c55b159cbfafe1f0" # Example AMI
}
