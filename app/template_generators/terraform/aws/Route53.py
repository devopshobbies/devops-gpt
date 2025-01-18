def IaC_template_generator_route53(input) -> str:

    aws_route53_create_zone = 'true' if input.zone else 'false'
    aws_route53_create_record = 'true' if input.record else 'false'
    aws_route53_create_delegation_set = 'true' if input.delegation_set else 'false'
    aws_route53_create_resolver_rule_association = 'true' if input.resolver_rule_association else 'false'
    
    tfvars_file = f"""create_zone = {aws_route53_create_zone}
create_record = {aws_route53_create_record}
create_delegation_set = {aws_route53_create_delegation_set}
create_resolver_rule_association = {aws_route53_create_resolver_rule_association}
"""
    return tfvars_file
