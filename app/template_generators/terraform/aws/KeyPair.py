def IaC_template_generator_key_pair(input) -> str:

    aws_key_pair_create = 'true' if input.key_pair else 'false'
    aws_key_pair_create_private_key = 'true' if input.private_key else 'false'
    
    tfvars_file = f"""create = {aws_key_pair_create}
create_private_key = {aws_key_pair_create_private_key}
"""
    return tfvars_file
