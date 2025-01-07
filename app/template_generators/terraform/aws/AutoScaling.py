def IaC_template_generator_autoscaling(input) -> str:

    aws_autoscaling_create_group = 'true' if input.autoscaling_group else 'false'
    aws_autoscaling_create_launch_template = 'true' if input.launch_template else 'false'
    aws_autoscaling_create_schedule = 'true' if input.schedule else 'false'
    aws_autoscaling_create_scaling_policy = 'true' if input.scaling_policy else 'false'
    aws_autoscaling_create_iam_instance_profile = 'true' if input.iam_instance_profile else 'false'
    
    tfvars_file = f"""create = {aws_autoscaling_create_group}
create_launch_template = {aws_autoscaling_create_launch_template}
create_schedule = {aws_autoscaling_create_schedule}
create_scaling_policy = {aws_autoscaling_create_scaling_policy}
create_iam_instance_profile = {aws_autoscaling_create_iam_instance_profile}
"""
    return tfvars_file
