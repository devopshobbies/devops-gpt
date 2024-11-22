import Platform from "../../../components/internal-ui/Platform";
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
        <Platform
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
