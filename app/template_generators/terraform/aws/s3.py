def IaC_template_generator_s3(input) -> str:

    s3 = ['aws_s3_bucket', 'aws_s3_bucket_versioning']

    aws_s3_create_bucket = 'true' if input.s3_bucket else 'false'
    aws_s3_create_bucket_versioning = 'true' if input.bucket_versioning else 'false'
    bucket_tags = """{
  Name        = "My bucket"
  Environment = "Dev"
}"""

    tfvars_file = f"""
s3_create_bucket = {aws_s3_create_bucket}
s3_bucket_name = "UniqueName"
s3_bucket_force_destroy = false
s3_bucket_tags = {bucket_tags}
s3_create_bucket_versioning = {aws_s3_create_bucket_versioning}
s3_bucket_versioning_status = "Enabled" """
    return tfvars_file