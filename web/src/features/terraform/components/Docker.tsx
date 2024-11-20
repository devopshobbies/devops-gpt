import PlatformBox from "../../../components/internal-ui/PlatformBox";
import useFindPlatform from "../../../hooks/useFindPlatform";
import { TerraformServices } from "../../constants";
import {
  ApiRequestTerraformDocker,
  TerraformDockerFormData,
} from "../../models";

const Docker = () => {
  const { platform } = useFindPlatform(TerraformServices.DOCKER);
  return (
    <>
      {platform && (
        <PlatformBox
          defaultValues={platform.defaultValues as TerraformDockerFormData}
          endpoint={platform.endpoint}
          fieldProperties={platform.fieldProperties}
          mapperFunction={
            platform.mapperFunction as () => ApiRequestTerraformDocker
          }
          serviceName={platform.serviceName}
        />
      )}
    </>
  );
};
export default Docker;
