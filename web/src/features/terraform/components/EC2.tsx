import Platform from "../../../components/internal-ui/Platform";
import useFindPlatform from "../../../hooks/useFindPlatform";
import { TerraformServices } from "../../constants";
import { ApiRequestTerraformEc2, TerraformEc2FormData } from "../../models";

const EC2 = () => {
  const { platform } = useFindPlatform(TerraformServices.EC2);
  return (
    <>
      {platform && (
        <Platform
          defaultValues={platform.defaultValues as TerraformEc2FormData}
          endpoint={platform.endpoint}
          fieldProperties={platform.fieldProperties}
          mapperFunction={
            platform.mapperFunction as () => ApiRequestTerraformEc2
          }
          serviceName={platform.serviceName}
        />
      )}
    </>
  );
};

export default EC2;
