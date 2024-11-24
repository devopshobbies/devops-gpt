import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.models import (
    IaCTemplateGenerationDocker, IaCTemplateGenerationEC2, IaCTemplateGenerationS3, IaCTemplateGenerationIAM,
    IaCTemplateGenerationArgoCD, IaCTemplateGenerationELB, IaCTemplateGenerationEFS, SyncPolicy, ArgoApplication
)


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


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
