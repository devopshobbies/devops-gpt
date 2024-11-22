import Platform from "../../../components/internal-ui/Platform";
import useFindPlatform from "../../../hooks/useFindPlatform";
import { TerraformServices } from "../../constants";
import { ApiRequestTerraformS3, TerraformS3FormData } from "../../models";

export const S3 = () => {
  const { platform } = useFindPlatform(TerraformServices.S3);
  return (
    <>
      {platform && (
        <Platform
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
