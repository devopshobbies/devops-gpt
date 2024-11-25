import { Endpoints } from "../features/constants";

export const routes = {
  basicGen: "/",
  bugFix: "/IaC-bugfix",
  terraformTemplate: "/terraform-template",
};

export const btnMappings = [
  { label: "Basic", route: routes.basicGen },
  { label: "Bug fix", route: routes.bugFix },
  { label: "Terraform template", route: routes.terraformTemplate },
  { label: "Installation", route: Endpoints.POST_INSTALL },
  { label: "Helm Template", route: Endpoints.POST_IAC_HELM },
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
