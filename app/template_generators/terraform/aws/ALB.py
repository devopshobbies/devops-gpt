def IaC_template_generator_alb(input) -> str:

    aws_alb_create_resources = 'true' if input.alb_resources else 'false'
    aws_alb_create_security_group = 'true' if input.security_group else 'false'
    
    tfvars_file = f"""alb_create = {aws_alb_create_resources}
create_security_group = {aws_alb_create_security_group}
"""
    return tfvars_file
