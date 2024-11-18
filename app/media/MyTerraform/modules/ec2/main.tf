
data "aws_ami" "linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023*kernel-6.1-x86_64"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_key_pair" "key_pair" {
  count       = var.key_pair_create ? 1 : 0
  key_name    = var.key_pair_name
  public_key  = file("${path.module}/terraform.pub")
}

resource "aws_security_group" "security_group" {
  count = var.security_group_create ? 1 : 0
  name  = var.security_group_name

  dynamic "ingress" {
    for_each = var.security_group_ingress_rules
    content {
      description = ingress.value["description"]
      from_port   = ingress.value["from_port"]
      to_port     = ingress.value["to_port"]
      protocol    = ingress.value["protocol"]
      cidr_blocks = ingress.value["cidr_blocks"]
    }
  }

  egress {
    from_port   = var.security_group_egress_rule["from_port"]
    to_port     = var.security_group_egress_rule["to_port"]
    protocol    = var.security_group_egress_rule["protocol"]
    cidr_blocks = var.security_group_egress_rule["cidr_blocks"]
  }
}

resource "aws_instance" "instance" {
  count                  = var.instance_create ? 1 : 0
  ami                    = data.aws_ami.linux.id
  instance_type          = var.instance_type
  key_name               = var.key_pair_create ? aws_key_pair.key_pair[0].key_name : null
  vpc_security_group_ids = var.security_group_create ? [aws_security_group.security_group[0].id] : null
}
