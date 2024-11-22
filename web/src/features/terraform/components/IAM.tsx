import Platform from "../../../components/internal-ui/Platform";
import useFindPlatform from "../../../hooks/useFindPlatform";
import { TerraformServices } from "../../constants";
import { ApiRequestTerraformIam, TerraformIAMFormData } from "../../models";

const IAM = () => {
  const { platform } = useFindPlatform(TerraformServices.IAM);
  return (
    <>
      {platform && (
        <Platform
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
