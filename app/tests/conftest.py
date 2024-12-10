import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.models import (
    IaCTemplateGenerationDocker, IaCTemplateGenerationEC2, IaCTemplateGenerationS3, IaCTemplateGenerationIAM,
    IaCTemplateGenerationArgoCD, IaCTemplateGenerationELB, IaCTemplateGenerationEFS, SyncPolicy, ArgoApplication,
    HelmTemplateGeneration, Pod, Persistance, Ingress, Environment, IaCBasicInput, IaCBugfixInput, IaCInstallationInput,
    AnsibleInstallNginx, AnsibleInstallDocker, AnsibleInstallKuber, Build, Service, Network, PreCreatedNetwork,
    DockerCompose
)


@pytest.fixture
def client():
    # with TestClient(app) as client:
    #     yield client
    return TestClient(app)



@pytest.fixture
def iac_template_docker_sample_input():
    return IaCTemplateGenerationDocker().model_dump()


@pytest.fixture
def iac_template_ec2_sample_input():
    return IaCTemplateGenerationEC2().model_dump()


@pytest.fixture
def iac_template_s3_sample_input():
    return IaCTemplateGenerationS3().model_dump()


@pytest.fixture
def iac_template_iam_sample_input():
    return IaCTemplateGenerationIAM().model_dump()


@pytest.fixture
def iac_template_argocd_sample_input():
    sync_policy = SyncPolicy()
    argocd_application = ArgoApplication(sync_policy=sync_policy)
    return IaCTemplateGenerationArgoCD(argocd_application=argocd_application).model_dump()


@pytest.fixture
def iac_template_elb_sample_input():
    return IaCTemplateGenerationELB().model_dump()


@pytest.fixture
def iac_template_efs_sample_input():
    return IaCTemplateGenerationEFS().model_dump()


@pytest.fixture
def helm_template_sample_input():
    nginx_pod = Pod(
        name='nginx',
        image='nginx:latest',
        target_port=80,
        replicas=2,
        persistance=Persistance(),
        environment=[Environment(name='DEBUG', value='true')],
        stateless=True,
        ingress=Ingress(enabled=True)
    )

    redis_pod = Pod(
        name='redis',
        image='redis:latest',
        target_port=6379,
        replicas=1,
        persistance=Persistance(),
        environment=[],
        stateless=False,
        ingress=Ingress(enabled=False)
    )

    return HelmTemplateGeneration(api_version=3, pods=[nginx_pod, redis_pod]).model_dump()

@pytest.fixture
def helm_template_invalid_sample_input():
    return {
        'api_version': 0,
        'pods': [
            {
                'name': '',
                'image': 'nginx:latest',
                'target_port': 70000,
                'replicas': 0,
                'persistance': {'size': 'invalid_size', 'accessModes': 'InvalidMode'},
                'environment': [{'name': '', 'value': ''}],
                'stateless': True,
                'ingress': {'enabled': True, 'host': ''}
            }
        ]
    }


@pytest.fixture
def iac_basic_sample_input():
    return IaCBasicInput(
        input='How do I manage state effectively in Terraform?',
        service='terraform',
        min_tokens=100,
        max_tokens=500
    ).model_dump()


@pytest.fixture
def iac_basic_invalid_sample_input():
    return {
        'input': 'Create a basic configuration',
        'service': 'invalid_service',
        'min_tokens': 100,
        'max_tokens': 500
    }


@pytest.fixture
def ias_bugfix_sample_input():
    return IaCBugfixInput(
        bug_description='Application fails to start on version latest',
        version='latest',
        service='terraform',
        min_tokens=100,
        max_tokens=500
    ).model_dump()


@pytest.fixture
def iac_bugfix_invalid_sample_input():
    return {
        'bug_description': '',
        'version': 'latest',
        'service': 'terraform',
        'min_tokens': 100,
        'max_tokens': 500
    }


@pytest.fixture
def iac_install_sample_input():
    return IaCInstallationInput(
        os='ubuntu',
        service='terraform'
    ).model_dump()


@pytest.fixture
def iac_install_invalid_sample_input():
    return {
        'os': 'Kali',  # Unsupported OS
        'service': 'terraform',
    }


@pytest.fixture
def ansible_nginx_sample_input():
    return AnsibleInstallNginx().model_dump()


@pytest.fixture
def ansible_nginx_invalid_sample_input():
    sample_input = AnsibleInstallNginx().model_dump()
    sample_input['os'] = 'Kali'
    return sample_input


@pytest.fixture
def ansible_docker_sample_input():
    return AnsibleInstallDocker().model_dump()


@pytest.fixture
def ansible_docker_invalid_sample_input():
    sample_input = AnsibleInstallDocker().model_dump()
    sample_input['os'] = 'Kali'
    return sample_input


@pytest.fixture
def ansible_kuber_sample_input():
    return AnsibleInstallKuber(
        k8s_worker_nodes=['node-1', 'node-2'],
        k8s_master_nodes=['node-1', 'node-2']
    ).model_dump()


@pytest.fixture
def ansible_kuber_invalid_sample_input():
    sample_input = AnsibleInstallKuber(
        k8s_worker_nodes=['node-1', 'node-2'],
        k8s_master_nodes=['node-1', 'node-2']
    ).model_dump()
    sample_input['os'] = 'Kali'
    return sample_input


@pytest.fixture
def docker_compose_sample_input():
    return DockerCompose().model_dump()


@pytest.fixture
def docker_compose_invalid_sample_input():
    sample_input = DockerCompose().model_dump()
    sample_input['services']['web']['build'] = None
    sample_input['services']['web']['image'] = None
    return sample_input
