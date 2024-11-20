import PlatformBox from "../../../components/internal-ui/PlatformBox";
import useFindPlatform from "../../../hooks/useFindPlatform";
import { ApiRequestTerraformEc2, TerraformEc2FormData } from "../../model";

const EC2 = () => {
  const { platform } = useFindPlatform("EC2");
  return (
    <>
      {platform && (
        <PlatformBox
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
