import {
  BasicGenFormData,
  BugFixFormData,
  HelmFormData,
  InstallFormData,
  TerraformArgocdFormData,
  TerraformDockerFormData,
  TerraformEc2FormData,
  TerraformIAMFormData,
  TerraformS3FormData,
} from "./models";

export enum DownloadFolders {
  MY_TERRAFORM = "MyTerraform",
  MY_HELM = "MyHelm",
}

export enum TerraformServices {
  DOCKER = "DOCKER",
  S3 = "S3",
  EC2 = "EC2",
  IAM = "IAM",
  ARGOCD = "ARGOCD",
}

export enum Endpoints {
  POST_BASIC = "/IaC-basic",
  POST_FIX = "/IaC-bugfix",
  POST_INSTALL = "/IaC-install",
  POST_IAC_T_DOCKER = "/IaC-template/docker",
  POST_IAC_T_EC2 = "/IaC-template/aws/ec2",
  POST_IAC_T_S3 = "/IaC-template/aws/s3",
  POST_IAC_T_IAM = "/IaC-template/aws/iam",
  POST_IAC_ARGOCD = "/IaC-template/argocd",
  POST_IAC_HELM = "/Helm-template",
  GET_DOWNLOAD = "/download-folder",
  GET_DIRECTORY = "/list-directory",
}

export enum BasicGenFields {
  MIN_TOKEN = "minToken",
  MAX_TOKEN = "maxToken",
  SERVICE = "service",
  INPUT = "input",
}

export enum BugFixFields {
  MIN_TOKEN = "minToken",
  MAX_TOKEN = "maxToken",
  SERVICE = "service",
  VERSION = "version",
  BUG_DESCRIPTION = "bugDescription",
}

export enum TerraformDockerFields {
  DOCKER_IMAGE = "dockerImage",
  DOCKER_CONTAINER = "dockerContainer",
}

export enum TerraformEC2Fields {
  KEY_PAIR = "keyPair",
  SECURITY_GROUP = "securityGroup",
  AWS_INSTANCE = "awsInstance",
  AMI_FROM_INSTANCE = "amiFromInstance",
}

export enum TerraformS3Fields {
  S3_BUCKET = "s3Bucket",
  BUCKET_VERSIONING = "bucketVersioning",
}

export enum TerraformIAMFields {
  IAM_USER = "iamUser",
  IAM_GROUP = "iamGroup",
}

export enum TerraformArgocdFields {
  AUTO_PRUNE = "autoPrune",
  SELF_HEAL = "selfHeal",
  APPLY_OUT_OF_SYNC_ONLY = "applyOutOfSyncOnly",
  CREATE_NAMESPACE = "createNamespace",
  FAIL_OR_SHARE_RESOURCE = "failOrShareResource",
  ARGOCD_REPOSITORY = "argocdRepository",
  ARGOCD_CLUSTER = "argocdCluster",
}

export enum HelmFields {
  API_VERSION = "apiVersion",
  NAME = "name",
  IMAGE = "image",
  TARGET_PORT = "targetPort",
  ENVIRONMENT_NAME = "environmentName",
  VALUE = "value",
  REPLICAS = "replicas",
  SIZE = "size",
  ACCESS_MODES = "accessModes",
  STATELESS = "stateless",
  ENABLED = "enabled",
  HOST = "host",
}

export enum InstallFields {
  OS = "os",
  SERVICE = "service",
}

export enum UserType {
  USER = "user",
  BOT = "bot",
}

export const basicGenDefaultValues: BasicGenFormData = {
  minToken: 100,
  maxToken: 500,
  service: "terraform",
  input: "",
};

export const bugFixDefaultValues: BugFixFormData = {
  minToken: 100,
  maxToken: 500,
  service: "terraform",
  version: "latest",
  bugDescription: "",
};

export const terraformDockerDefaultValues: TerraformDockerFormData = {
  dockerImage: false,
  dockerContainer: false,
};

export const terraformArgocdDefaultValues: TerraformArgocdFormData = {
  applyOutOfSyncOnly: false,
  argocdCluster: false,
  argocdRepository: false,
  autoPrune: false,
  createNamespace: false,
  failOrShareResource: false,
  selfHeal: false,
};

export const terraformEc2DefaultValues: TerraformEc2FormData = {
  keyPair: false,
  amiFromInstance: false,
  awsInstance: false,
  securityGroup: false,
};

export const terraformS3DefaultValues: TerraformS3FormData = {
  s3Bucket: false,
  bucketVersioning: false,
};

export const terraformIamDefaultValues: TerraformIAMFormData = {
  iamUser: false,
  iamGroup: false,
};

export const helmDefaultValues: HelmFormData = {
  apiVersion: 2,
  pods: [
    {
      accessModes: "ReadWriteOnce",
      enabled: false,
      host: "www.example.com",
      environmentName: "ENV1",
      value: "Hi",
      image: "nginx",
      name: "web",
      replicas: 1,
      size: "1Gi",
      stateless: false,
      targetPort: 80,
    },
  ],
};

export const installDefaultValues: InstallFormData = {
  os: "",
  service: "",
};
