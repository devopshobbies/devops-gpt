import PlatformBox from "../../../components/internal-ui/PlatformBox";
import useFindPlatform from "../../../hooks/useFindPlatform";
import {
  ApiRequestTerraformDocker,
  TerraformDockerFormData,
} from "../../model";

const Docker = () => {
  const { platform } = useFindPlatform("Docker");
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
