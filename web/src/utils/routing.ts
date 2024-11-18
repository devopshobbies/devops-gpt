import { Endpoints } from "../features/constants";

export const routes = {
  basicGen: "/",
  bugFix: "/IaC-bugfix",
  terraformTemplate: "/terraformT",
  listDirectory: "/download",
};

export const btnMappings = [
  { label: "Basic", route: routes.basicGen },
  { label: "Bug fix", route: routes.bugFix },
  { label: "Terraform template", route: routes.terraformTemplate },
  { label: "Download", route: routes.listDirectory },
  { label: "Installation", route: Endpoints.POST_INSTALL },
  { label: "Helm Template", route: Endpoints.POST_IAC_HELM },
];
