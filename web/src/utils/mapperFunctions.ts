import { CompleteHelmForm } from "../features/helm/models";
import {
  BasicGenFormData,
  ApiRequestBasicGen,
  BugFixFormData,
  ApiRequestBugFix,
  TerraformDockerFormData,
  ApiRequestTerraformDocker,
  TerraformEc2FormData,
  ApiRequestTerraformEc2,
  TerraformS3FormData,
  ApiRequestTerraformS3,
  TerraformIAMFormData,
  ApiRequestTerraformIam,
  ApiRequestTerraformArgocd,
  TerraformArgocdFormData,
  ApiRequestHelm,
} from "../features/models";

export const basicGenMapper = (data: BasicGenFormData): ApiRequestBasicGen => ({
  min_token: data.minToken,
  max_token: data.maxToken,
  service: data.service,
  input: data.input,
  requestId: "",
});

export const bugFixMapper = (data: BugFixFormData): ApiRequestBugFix => ({
  min_token: data.minToken,
  max_token: data.maxToken,
  bug_description: data.bugDescription,
  service: data.service,
  version: data.version,
  requestId: "",
});

export const terraformDockerMapper = (
  data: TerraformDockerFormData
): ApiRequestTerraformDocker => ({
  docker_image: data.dockerImage,
  docker_container: data.dockerContainer,
});

export const terraformEC2Mapper = (
  data: TerraformEc2FormData
): ApiRequestTerraformEc2 => ({
  key_pair: data.keyPair,
  security_group: data.securityGroup,
  aws_instance: data.awsInstance,
  ami_from_instance: data.amiFromInstance,
});

export const terraformS3Mapper = (
  data: TerraformS3FormData
): ApiRequestTerraformS3 => ({
  s3_bucket: data.s3Bucket,
  bucket_versioning: data.bucketVersioning,
});

export const terraformIAMMapper = (
  data: TerraformIAMFormData
): ApiRequestTerraformIam => ({
  iam_user: data.iamUser,
  iam_group: data.iamGroup,
});

export const terraformArgocdMapper = (
  data: TerraformArgocdFormData
): ApiRequestTerraformArgocd => ({
  argocd_application: {
    sync_policy: {
      auto_prune: data.autoPrune,
      self_heal: data.selfHeal,
    },
    sync_options: {
      apply_out_of_sync_only: data.applyOutOfSyncOnly,
      create_namespace: data.createNamespace,
      fail_or_share_resource: data.failOrShareResource,
    },
  },
  argocd_cluster: data.argocdCluster,
  argocd_repository: data.argocdRepository,
});

export const helmMapper = (data: CompleteHelmForm): ApiRequestHelm => ({
  api_version: Number(data.apiVersion),
  pods: data.pods.map((item) => ({
    environment: item.environment.map((env) => ({
      name: env.name,
      value: env.value,
    })),
    image: item.image,
    ingress: {
      enabled: item.enabled,
      host: item.host,
    },
    name: item.name,
    persistance: {
      accessModes: item.accessModes,
      size: item.size,
    },
    replicas: item.replicas,
    stateless: item.stateless,
    target_port: item.targetPort,
  })),
});
