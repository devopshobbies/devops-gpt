export enum TerraformTemplateAPI {
  Argocd = '/IaC-template/argocd',
  Iam = '/IaC-template/aws/iam',
  S3 = '/IaC-template/aws/s3',
  EC2 = '/IaC-template/aws/ec2',
  Docker = '/IaC-template/docker',
}

export enum API {
  Basic = '/IaC-basic',
  BugFix = '/IaC-bugfix',
  Installation = '/IaC-install',
  HelmTemplate = '/Helm-template',
  DockerCompose = "/docker-compose"
}

export enum AnsibleTemplateAPI {
  Docker = '/ansible-install/docker',
  Nginx = '/ansible-install/nginx',
  Kubernetes = '/ansible-install/kuber',
}
