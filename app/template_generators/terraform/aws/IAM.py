def IaC_template_generator_iam(input) -> str:

    

    aws_iam_create_user = 'true' if input.iam_user else 'false'
    aws_iam_create_group = 'true' if input.iam_group else 'false'
    iam_user = """ {
    name = "devopshobbies"
    path = "/"
  }"""
    iam_groups = """{
    name = "developers"
    path = "/"
  }
    """
    
    tfvars_file = f"""iam_create_user = {aws_iam_create_user}
iam_users = [
  {iam_user}
]

iam_create_group = {aws_iam_create_group}
iam_groups = [
  {iam_groups}
]"""
    return tfvars_file