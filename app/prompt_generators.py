from .models import (IaCBasicInput, 
    IaCBugfixInput,
    IaCInstallationInput, IaCTemplateGeneration,HelmTemplateGeneration)

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
                generate a clear shell acript about installation {input.service} in {input.os} based on {input.service} document.
                without any additional note. just script for installation.

            """
    return prompt


def IaC_template_generator(input : IaCTemplateGeneration) -> str:

    prompt = f"""
                generate a complex template for {input.service} base on standard template with project structure focus on 
                these important points:

                    1 - CI pipeline integration = {input.CI_integration}
                    2 - base config is {input.base_config}
                    3 - project name is app/media/MyTerraform
                    4 - number of modules = 1
                   
                if CI integration is true, generate a pipeline based on github actions.

                finally just give me a python code without any note that can generate a project folder with the given schema
                without ```python entry. and we dont need any base directory in the python code.
                the final terraform template must work very well without any error!

                
            """
    return prompt

def helm_template_generator(input : HelmTemplateGeneration) -> str:

    prompt = f"""
            generate a correct python code to generate a helm project structure (project name: app/media/MyHelm) 
            based on the latest version of helm chart. 
            just generate a code to generate a folder as project template. don't consider base_dir
                
            CI integrated (using github actions) = {input.CI_integration}.
            consider these directories : [charts/, crds/, templates/]
            consider these files : Chart.yaml & values.yaml
            in the templates/ directory create these directories: {input.templates}.
            set the api_version in the Chart.yaml : v{input.api_version}.
            initialize values.yaml based on these docker images : {input.images}

            please set a something default in chart.yaml and values.yaml

            just Generate a python code without any additional notes or ```python3 entry
            """
    return prompt