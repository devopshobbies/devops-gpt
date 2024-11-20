import PlatformBox from "../../../components/internal-ui/PlatformBox";
import useFindPlatform from "../../../hooks/useFindPlatform";
import {
  ApiRequestTerraformArgocd,
  TerraformArgocdFormData,
} from "../../model";

const Argocd = () => {
  const { platform } = useFindPlatform("ARGOCD");

  return (
    <>
      {platform && (
        <PlatformBox
          defaultValues={platform.defaultValues as TerraformArgocdFormData}
          endpoint={platform.endpoint}
          fieldProperties={platform.fieldProperties}
          mapperFunction={
            platform.mapperFunction as () => ApiRequestTerraformArgocd
          }
          serviceName={platform.serviceName}
        />
      )}
    </>
  );
};

export default Argocd;
