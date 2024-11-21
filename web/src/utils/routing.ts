export const routes = {
  basicGen: "/",
  bugFix: "/IaC-bugfix",
  terraformTemplate: "/terraform-template",
  helm: "/helm",
  install: "/install",
};

export const btnMappings = [
  { label: "Basic", route: routes.basicGen },
  { label: "Bug fix", route: routes.bugFix },
  { label: "Terraform template", route: routes.terraformTemplate },
  { label: "Helm Template", route: routes.helm },
  { label: "Installation", route: routes.install },
];

export const terraformRoutes = {
  dockerService: "/docker-service",
  ec2Service: "/ec2-service",
  s3Service: "/s3-service",
  iamService: "/iam-service",
  argocdService: "/argocd-service",
};

export const terraformBtnMapping = [
  { label: "Docker service", route: terraformRoutes.dockerService },
  { label: "EC2 service", route: terraformRoutes.ec2Service },
  { label: "S3 service", route: terraformRoutes.s3Service },
  { label: "IAM service", route: terraformRoutes.iamService },
  { label: "ARGOCD service", route: terraformRoutes.argocdService },
];
