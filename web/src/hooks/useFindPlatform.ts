import { TerraformServices } from "../features/constants";
import { platformData } from "../features/terraform/constants";

const useFindPlatform = (serviceName: TerraformServices) => {
  const platform = platformData.find(
    (platform) => platform.serviceName === serviceName
  );
  return { platform };
};
export default useFindPlatform;
