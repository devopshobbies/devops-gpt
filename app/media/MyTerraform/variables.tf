variable "region" {{
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}}

variable "instance_type" {{
  description = "EC2 Instance type"
  type        = string
  default     = "t2.micro"
}}

variable "ami" {{
  description = "AMI ID"
  type        = string
  default     = "ami-0c55b159cbfafe1f0"
}}
