import { Endpoints } from "../features/constants";

export const nameGenerator = (endpoint: Endpoints | "") => {
  let name = "Terraform";
  switch (endpoint) {
    case Endpoints.POST_IAC_T_DOCKER:
      name = `${name}_Docker`;
      break;
    case Endpoints.POST_IAC_T_EC2:
      name = `${name}_EC2`;
      break;
    case Endpoints.POST_IAC_T_S3:
      name = `${name}_S3`;
      break;
    case Endpoints.POST_IAC_T_IAM:
      name = `${name}_IAM`;
      break;
  }
  return name;
};
