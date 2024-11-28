export const routes = {
  basicGen: '/',
  bugFix: '/IaC-bugfix',
  terraformTemplate: '/terraform-template',
  installation: '/IaC-install',
  helmTemplate: '/Helm-template',
};

export const terraformRoutes = {
  dockerService: `${routes.terraformTemplate}/docker-service`,
  ec2Service: `${routes.terraformTemplate}/ec2-service`,
  s3Service: `${routes.terraformTemplate}/s3-service`,
  iamService: `${routes.terraformTemplate}/iam-service`,
  argocdService: `${routes.terraformTemplate}/argocd-service`,
};
