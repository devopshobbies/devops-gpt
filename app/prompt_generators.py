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
                minimum length of answer is {input.min_tokens} and maximum length is {input.max_tokens}

            """
    return prompt


def IaC_installation_generator(input : IaCInstallationInput) -> str:

    prompt = f"""
                generate a clear shell script about installation {input.service} in {input.os} based on {input.service} document.
                without any additional note. just script for installation. please consider new lines without any additional comment.

            """
    return prompt


def IaC_template_generator(input : IaCTemplateGeneration) -> str:

    prompt = f"""
              Generate a Python code to generate a Terraform project (project name is app/media/MyTerraform)
              that dynamically provisions resources for {input.base_config} ensuring a modular, flexible structure
              to enable users to configure all essential settings at the root level. Only provide Python code,
              no explanations or markdown formatting. The project should be organized as follows:
              1. Root Directory Structure:
                  - main.tf:
                      - Contains a provider block, configured with flexible variables where required to allow
                        users to specify provider settings without hardcoding.
                      - Defines a module block that references {input.base_config} from a subdirectory within
                        modules. This module block should expose all variables that {input.base_config} requires,
                        allowing configuration at the root level rather than directly within the module.
                      - Every variable defined in {input.base_config} should be passed through the module block,
                        ensuring that users can adjust all critical parameters of {input.base_config} by
                        modifying root main.tf.
                  - variables.tf:
                      - Declares all variables that users might need to configure for {input.base_config}.
                        These should include any inputs required by the provider or the {input.base_config}
                        resource, as well as optional parameters that users may want to customize.
                      - Variable descriptions should clearly indicate their purpose, and default values should
                        be avoided unless there are reasonable, common defaults, to maintain flexibility and
                        encourage explicit configuration.
                      - All types of variables can be used such as (number, string, bool, list(string),
                        map(string), list(map(string)), map(map(string)), object(), any)
                  - terraform.tfvars:
                      - Provides default values for variables declared in the root `variables.tf`, making it easy
                        for users to define common configurations.
                      - This file should be structured to include any typical default settings without hardcoding
                        sensitive values.
                  - versions.tf:
                      - Contains the `terraform` and `provider` blocks, specifying required versions.

                      - If {input.base_config} is a Docker resource, set kreuzwerker/docker as the provider with appropriate version constraints.
                      - If {input.base_config} is an AWS resource, set hashicorp/aws as the provider with suitable version constraints.

                      - Structure the `terraform` block as:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                <provider_name> = {{
                                  source  = "<source>"
                                  version = ">= <version>"
                               }}
                              }}
                            }}
              2. Module Directory Structure (modules/{input.base_config}):
                  - main.tf:
                      - Configures the resource for {input.base_config} with this logic:
                          - If {input.base_config} is an AWS resource, use all required parameters for it based on
                            the terraform aws provider.
                          - If {input.base_config} == 'docker_container':
                              - Use only the following parameters and avoid using any other parameters:
                                  - 1. image (type: string): Specifies the container image.
                                  - 2. name (type: string): Sets the container name.
                                  - 3. hostname (type: string): Configures the container hostname.
                                  - 4. restart (type: string): Defines the container's restart policy (e.g., always, on-failure, no).
                          - If {input.base_config} == 'docker_image':
                              - Use only the following parameters and avoid using any other parameters:
                                  - 1. name (type: string): Specifies the image name.
                                  - 2. force_remove (type: boolean): Determines whether to forcibly remove intermediate containers.
                                  - 3. build (block type, max: 1): Includes the following required field:
                                      - context (type: string, required): Specifies the build context for the image.
                      - The project must only create the resource defined by {input.base_config}, treating resource 
                        as completely unrelated entities
                      - Avoid any hardcoded values within the module to support full configurability from the root level.
                  - variables.tf:
                      - Lists all variables necessary for configuring {input.base_config}, with descriptions and
                        types specified to improve usability. No default values should be set here unless
                        necessary for required fields.
                      - Variable names should be clear and consistent with naming conventions in the root
                        variables file, ensuring consistency in usage.
                  - terraform.tfvars:
                      - Includes default values for module-level variables to ensure that common parameters have
                        defaults. This `terraform.tfvars` file within the module should be structured to provide
                        typical configuration values, making it easier to set up and reducing the need for hardcoded values.
                  - versions.tf:
                      - Contains the `terraform` and `provider` blocks, specifying required versions.
                      - If {input.base_config} is a Docker resource, set kreuzwerker/docker as the provider with appropriate version constraints.
                      - If {input.base_config} is an AWS resource, set hashicorp/aws as the provider with suitable version constraints.

                      - Structure the `terraform` block as:
                            terraform {{
                              required_version = ">= 1.0"

                              required_providers {{
                                <provider_name> = {{
                                  source  = "<source>"
                                  version = ">= <version>"
                                }}
                              }}
                            }}
              Ensure this project structure supports {input.base_config}’s configurability, extensibility, and
              reusability across diverse Terraform providers, empowering users to manage their resources through a
              single, customizable root configuration while keeping module internals robustly modular.

              finally just give me a python code without any note that can generate a project folder with the given
              schema without ```python entry. and we dont need any base directory in the python code. the final
              terraform template must work very well without any error!

              Python code you give me, must have structure like that:

                import os
                project_name = "app/media/MyTerraform"
                moduels_dir = os.path.join(project_name, "modules")

                # Create project directories

                os.makedirs(moduels_dir, exist_ok=True)

                # Create main.tf (for example)
                with open(os.path.join(project_name, "main.tf"), "w") as main_file:
                    # any thing you need



            """
    return prompt

def helm_template_generator(input : HelmTemplateGeneration) -> str:

    templates = [i.name for i in input.pods]
    docker_images = [{i.name:i.image} for i in input.pods]
    target_ports = [{i.name:i.target_port} for i in input.pods]
    replicas_ = [{i.name:i.replicas} for i in input.pods]
    persistance = [{i.name:i.persistance} for i in input.pods]
    envs = [{i.name:i.environment} for i in input.pods]
    status =  [{i.name:i.stateless} for i in input.pods]
    ingress_ = [{i.name:i.ingress} for i in input.pods]

    prompt = f"""

            generate a correct python code to generate a helm project structure (project name: app/media/MyHelm)
            based on the latest version of helm chart. Only provide Python code, no explanations or markdown formatting.
            just generate a code to generate a folder as project template. don't consider base_dir

            consider these directories : [charts/,templates/]
            consider these files : Chart.yaml & values.yaml
            in the templates/ directory create these directories: {templates}.
            set the api_version in the Chart.yaml : v{input.api_version}.
            initialize values.yaml based on these dict of templates and docker images,
            please provide other informations related to values.yaml : {docker_images},
            the target port of pods in the dict format are here : {target_ports}
            for each template, initialize this file => service.yaml.
            set replicas of pods following this dict format : {replicas_}.
            set persistance (pvc) of pods following this dict fomrat : {persistance}
            set environment variables of pods following this dict format : {envs} based on helm standard environment setting.(
                for example something like that:
                    env:
                     name=value
            )
            initialize ingress with a default host for pod if the pod ingress is true in here {ingress_}.
            set stateless in pod based on {status}.


            Based on values.yaml, create all necessary Kubernetes templates in the templates directory:
            if stateless.enabled is true, create deployment.yaml; if stateless.enabled is false, create statefulset.yaml.
            If a persistence block exists, include pvc.yaml. If the ingress block is defined and ingress.enabled
            is true, create ingress.yaml. if ingress.enabled is false, do not create ingress.yaml. Always create
            secrets.yaml for secure data storage.

            Ensure each template is fully parameterized to match values from values.yaml for flexible configuration.

            in the final stage, put helpers.tpl in all templates and set the content based on information given.
            """
    return prompt
