def IaC_template_generator_cloudfront(input) -> str:

    aws_cloudfront_create_distribution = 'true' if input.distribution else 'false'
    aws_cloudfront_create_origin_access_identity = 'true' if input.origin_access_identity else 'false'
    aws_cloudfront_create_origin_access_control = 'true' if input.origin_access_control else 'false'
    aws_cloudfront_create_monitoring_subscription = 'true' if input.monitoring_subscription else 'false'
    aws_cloudfront_create_vpc_origin = 'true' if input.vpc_origin else 'false'
    
    tfvars_file = f"""create_distribution = {aws_cloudfront_create_distribution}
create_origin_access_identity = {aws_cloudfront_create_origin_access_identity}
create_origin_access_control = {aws_cloudfront_create_origin_access_control}
create_monitoring_subscription = {aws_cloudfront_create_monitoring_subscription}
create_vpc_origin = {aws_cloudfront_create_vpc_origin}
"""
    return tfvars_file
