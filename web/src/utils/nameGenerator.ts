import { Endpoints } from "../features/constants";

export const nameGenerator = (endpoint: Endpoints | "") => {
  let name = "";
  switch (endpoint) {
    case Endpoints.POST_IAC_T_DOCKER:
      name = "DOCKER";
      break;
    case Endpoints.POST_IAC_T_EC2:
      name = "EC2";
      break;
    case Endpoints.POST_IAC_T_S3:
      name = "S3";
      break;
    case Endpoints.POST_IAC_T_IAM:
      name = "IAM";
      break;
  }
  return name;
};
