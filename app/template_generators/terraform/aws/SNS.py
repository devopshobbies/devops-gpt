def IaC_template_generator_sns(input) -> str:

    aws_sns_create_topic = 'true' if input.sns_topic else 'false'
    aws_sns_create_topic_policy = 'true' if input.topic_policy else 'false'
    aws_sns_create_subscription = 'true' if input.subscription else 'false'
    
    tfvars_file = f"""create = {aws_sns_create_topic}
create_topic_policy = {aws_sns_create_topic_policy}
create_subscription = {aws_sns_create_subscription}
"""
    return tfvars_file
