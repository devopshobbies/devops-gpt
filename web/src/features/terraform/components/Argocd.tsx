import PlatformBox from "../../../components/internal-ui/PlatformBox";
import useFindPlatform from "../../../hooks/useFindPlatform";
import { TerraformServices } from "../../constants";
import {
  ApiRequestTerraformArgocd,
  TerraformArgocdFormData,
} from "../../models";

const Argocd = () => {
  const { platform } = useFindPlatform(TerraformServices.ARGOCD);

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
