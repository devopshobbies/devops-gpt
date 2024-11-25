import { UserType } from "./constants";

export interface Message {
  user: UserType;
  content: string;
  id: string;
}

export interface BasicGenFormData {
  minToken: number;
  maxToken: number;
  service: string;
  input: string;
}

export interface ApiRequestBasicGen {
  min_token: number;
  max_token: number;
  service: string;
  input: string;
  requestId: string;
}

export interface BugFixFormData {
  minToken: number;
  maxToken: number;
  service: string;
  bugDescription: string;
  version: string;
}

export interface ApiRequestBugFix {
  min_token: number;
  max_token: number;
  service: string;
  bug_description: string;
  version: string;
  requestId: string;
}

export interface TerraformDockerFormData {
  dockerImage: boolean;
  dockerContainer: boolean;
}

export interface ApiRequestTerraformDocker {
  docker_image: boolean;
  docker_container: boolean;
}

export interface TerraformEc2FormData {
  keyPair: boolean;
  securityGroup: boolean;
  awsInstance: boolean;
  amiFromInstance: boolean;
}

export interface ApiRequestTerraformEc2 {
  key_pair: boolean;
  security_group: boolean;
  aws_instance: boolean;
  ami_from_instance: boolean;
}

export interface TerraformS3FormData {
  s3Bucket: boolean;
  bucketVersioning: boolean;
}

export interface ApiRequestTerraformS3 {
  s3_bucket: boolean;
  bucket_versioning: boolean;
}

export interface TerraformIAMFormData {
  iamUser: boolean;
  iamGroup: boolean;
}

export interface ApiRequestTerraformIam {
  iam_user: boolean;
  iam_group: boolean;
}

export interface TerraformArgocdFormData {
  autoPrune: boolean;
  selfHeal: boolean;
  applyOutOfSyncOnly: boolean;
  createNamespace: boolean;
  failOrShareResource: boolean;
  argocdRepository: boolean;
  argocdCluster: boolean;
}

export interface ApiRequestTerraformArgocd {
  argocd_application: {
    sync_policy: {
      auto_prune: boolean;
      self_heal: boolean;
    };
    sync_options: {
      apply_out_of_sync_only: boolean;
      create_namespace: boolean;
      fail_or_share_resource: boolean;
    };
  };
  argocd_repository: boolean;
  argocd_cluster: boolean;
}
export interface HelmFormData {
  apiVersion: number;
  pods: Array<{
    name: string;
    image: string;
    targetPort: number;
    replicas: number;
    size: string;
    accessModes: string;
    environmentName: string;
    value: string;
    stateless: boolean;
    enabled: boolean;
    host: string;
  }>;
}

export interface Pod {
  name: string;
  image: string;
  target_port: number;
  replicas: number;
  persistance: {
    size: string;
    accessModes: string;
  };
  environment: [
    {
      name: string;
      value: string;
    }
  ];
  stateless: boolean;
  ingress: {
    enabled: boolean;
    host: string;
  };
}

export interface ApiRequestHelm {
  api_version: number;
  pods: Pod[];
}

export interface InstallFormData {
  os: string;
  service: string;
}

export interface ApiRequestInstall {
  os: string;
  service: string;
}

export interface ApiResponseDownload {
  data: {
    output: string;
  };
}
