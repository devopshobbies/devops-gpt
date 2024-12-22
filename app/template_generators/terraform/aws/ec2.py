def IaC_template_generator_ec2(input) -> str:
    
   

    aws_ec2_create_key_pair = 'true' if input.key_pair else 'false'
    aws_ec2_create_security_group = 'true' if input.security_group else 'false'
    aws_ec2_create_instance = 'true' if input.aws_instance else 'false'
    aws_ec2_create_ami_from_instance = 'true' if input.ami_from_instance else 'false'
    ingress_rules = """{
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
}"""
    egress_rules = """{
  from_port   = 0
  to_port     = 0
  protocol    = "-1"
  cidr_blocks = ["0.0.0.0/0"]
}"""

    tfvars_file = f"""key_pair_create = {aws_ec2_create_key_pair}
key_pair_name = "ec2"

security_group_create = {aws_ec2_create_security_group}
security_group_name = "my_rules"
security_group_ingress_rules = {ingress_rules}
security_group_egress_rule = {egress_rules}
instance_create = {aws_ec2_create_instance}
instance_type = "t2.micro"

ami_from_instance_create = {aws_ec2_create_ami_from_instance}
ami_name = "my-own-ami" """
    return tfvars_file