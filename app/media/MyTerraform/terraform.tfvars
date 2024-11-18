
key_pair_create = true
key_pair_name = "ec2"

security_group_create = true
security_group_name = "my_rules"
security_group_ingress_rules = {
  ssh_rule = {
    description = "SSH Ingress"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  },
  http_rule = {
    description = "HTTP Ingress"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
security_group_egress_rule = {
  from_port   = 0
  to_port     = 0
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]
}

instance_create = true
instance_type = "t2.micro"
