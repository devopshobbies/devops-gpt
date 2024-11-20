import PlatformBox from "../../../components/internal-ui/PlatformBox";
import useFindPlatform from "../../../hooks/useFindPlatform";
import { ApiRequestTerraformS3, TerraformS3FormData } from "../../model";

export const S3 = () => {
  const { platform } = useFindPlatform("S3");
  return (
    <>
      {platform && (
        <PlatformBox
          defaultValues={platform.defaultValues as TerraformS3FormData}
          endpoint={platform.endpoint}
          fieldProperties={platform.fieldProperties}
          mapperFunction={
            platform.mapperFunction as () => ApiRequestTerraformS3
          }
          serviceName={platform.serviceName}
        />
      )}
    </>
  );
};

export default S3;
