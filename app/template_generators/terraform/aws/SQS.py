def IaC_template_generator_sqs(input) -> str:

    aws_sqs_create_queue = 'true' if input.sqs_queue else 'false'
    aws_sqs_create_queue_policy = 'true' if input.queue_policy else 'false'
    aws_sqs_create_dlq = 'true' if input.dlq else 'false'
    aws_sqs_create_dlq_redrive_allow_policy = 'true' if input.dlq_redrive_allow_policy else 'false'
    aws_sqs_create_dlq_queue_policy = 'true' if input.dlq_queue_policy else 'false'
    
    tfvars_file = f"""create = {aws_sqs_create_queue}
create_queue_policy = {aws_sqs_create_queue_policy}
create_dlq = {aws_sqs_create_dlq}
create_dlq_redrive_allow_policy = {aws_sqs_create_dlq_redrive_allow_policy}
create_dlq_queue_policy = {aws_sqs_create_dlq_queue_policy}
"""
    return tfvars_file
