from .models import (IaCBasicInput,
    IaCBugfixInput,
    IaCInstallationInput,HelmTemplateGeneration)

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
