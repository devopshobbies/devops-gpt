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
} from '../features/models';

export const basicGenMapper = (data: BasicGenFormData): ApiRequestBasicGen => ({
  min_token: data.minToken,
  max_token: data.maxToken,
  service: data.service,
  input: data.input,
  requestId: '',
});

export const bugFixMapper = (data: BugFixFormData): ApiRequestBugFix => ({
  min_token: data.minToken,
  max_token: data.maxToken,
  bug_description: data.bugDescription,
  service: data.service,
  version: data.version,
  requestId: '',
});

export const terraformDockerMapper = (
  data: TerraformDockerFormData,
): ApiRequestTerraformDocker => ({
  docker_image: data.dockerImage,
  docker_container: data.dockerContainer,
});

export const terraformEC2Mapper = (
  data: TerraformEc2FormData,
): ApiRequestTerraformEc2 => ({
  key_pair: data.keyPair,
  security_group: data.securityGroup,
  aws_instance: data.awsInstance,
  ami_from_instance: data.amiFromInstance,
});

export const terraformS3Mapper = (
  data: TerraformS3FormData,
): ApiRequestTerraformS3 => ({
  s3_bucket: data.s3Bucket,
  bucket_versioning: data.bucketVersioning,
});

export const terraformIAMMapper = (
  data: TerraformIAMFormData,
): ApiRequestTerraformIam => ({
  iam_user: data.iamUser,
  iam_group: data.iamGroup,
});

export const terraformArgocdMapper = (
  data: TerraformArgocdFormData,
): ApiRequestTerraformArgocd => ({
  argocd_application: {
    sync_policy: {
      auto_prune: data.autoPrune,
      self_heal: data.selfHeal,
    },
  },
  argocd_repository: data.argocdRepository,
  application_depends_repository: data.applicationDependsRepository,
});
