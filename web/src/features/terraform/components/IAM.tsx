import PlatformBox from "../../../components/internal-ui/PlatformBox";
import useFindPlatform from "../../../hooks/useFindPlatform";
import { TerraformServices } from "../../constants";
import { ApiRequestTerraformIam, TerraformIAMFormData } from "../../model";

const IAM = () => {
  const { platform } = useFindPlatform(TerraformServices.IAM);
  return (
    <>
      {platform && (
        <PlatformBox
          defaultValues={platform.defaultValues as TerraformIAMFormData}
          endpoint={platform.endpoint}
          fieldProperties={platform.fieldProperties}
          mapperFunction={
            platform.mapperFunction as () => ApiRequestTerraformIam
          }
          serviceName={platform.serviceName}
        />
      )}
    </>
  );
};

export default IAM;
