from .models import (IaCBasicInput, 
    IaCBugfixInput,
    IaCInstallationInput, IaCTemplateGeneration)

def IaC_basics_generator(input : IaCBasicInput) -> str:

    prompt = f"""
                Write a robust answer about {input.service},
                focusing on the latest update of {input.service} and based on this question:{input.input},
                minimun length of answer is {input.min_tokens} and maximum length is {input.max_tokens}

            """
    return prompt


def IaC_bugfix_generator(input : IaCBugfixInput) -> str:

    prompt = f"""
                Write a clear answer to debug {input.service}
                focusing on the version {input.version} of {input.service} and based on this bug:{input.bug_description},
                generate a correct code that help us to solve this bug.
                minimun length of answer is {input.min_tokens} and maximum length is {input.max_tokens}

            """
    return prompt


def IaC_installation_generator(input : IaCInstallationInput) -> str:

    prompt = f"""
                Write a clear answer about installation {input.service} in {input.os} based on {input.service} document.
                
                minimun length of answer is {input.min_tokens} and maximum length is {input.max_tokens}

            """
    return prompt


def IaC_template_generator(input : IaCTemplateGeneration) -> str:

    prompt = f"""
                generate a complex template for {input.service} base on standard template with project structure focus on 
                these parameters:
                    1- CI pipeline integration = {input.CI_integration}
                    2 - base config is {input.base_config}
                    3 - project name is app/media/{input.project_name}
                   
                if CI integration is true, generate a pipeline based on github actions.

                finally just give me a python code without any note that can generate a project folder with the given schema
                without ```python entry. and we dont need any base directory in the python code

                
            """
    return prompt