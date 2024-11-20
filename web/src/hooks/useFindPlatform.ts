import { platformData } from "../features/terraform/constants";

const useFindPlatform = (serviceName: string) => {
  const platform = platformData.find(
    (platform) => platform.serviceName === serviceName
  );
  return { platform };
};
export default useFindPlatform;
