def IaC_template_generator_rds(input) -> str:

    aws_rds_create_db_instance = 'true' if input.db_instance else 'false'
    aws_rds_create_db_option_group = 'true' if input.db_option_group else 'false'
    aws_rds_create_db_parameter_group = 'true' if input.db_parameter_group else 'false'
    aws_rds_create_db_subnet_group = 'true' if input.db_subnet_group else 'false'
    aws_rds_create_monitoring_role = 'true' if input.monitoring_role else 'false'
    aws_rds_create_cloudwatch_log_group = 'true' if input.cloudwatch_log_group else 'false'
    aws_rds_create_master_user_password_rotation = 'true' if input.master_user_password_rotation else 'false'
    
    tfvars_file = f"""create_db_instance = {aws_rds_create_db_instance}
create_db_option_group = {aws_rds_create_db_option_group}
create_db_parameter_group = {aws_rds_create_db_parameter_group}
create_db_subnet_group = {aws_rds_create_db_subnet_group}
create_monitoring_role = {aws_rds_create_monitoring_role}
create_cloudwatch_log_group = {aws_rds_create_cloudwatch_log_group}
manage_master_user_password_rotation = {aws_rds_create_master_user_password_rotation}
"""
    return tfvars_file
