import { ENDPOINTS } from "../features/constants";

export const btnMappings = [
  { label: "Basic", route: "/" },
  { label: "Bug fix", route: ENDPOINTS.postFix },
  { label: "Installation", route: ENDPOINTS.postInstall },
  { label: "Template - IaC", route: ENDPOINTS.PostIacTemp },
  { label: "Template - Helm", route: ENDPOINTS.PostIacHelm },
  { label: "Download", route: ENDPOINTS.getDonwload },
  { label: "List directory", route: ENDPOINTS.getDirectory },
];
