import PlatformBox from '../../../components/internal-ui/PlatformBox';
import useFindPlatform from '../../../hooks/useFindPlatform';
import { TerraformServices } from '../../constants';
import { useNavigate } from 'react-router-dom';
import { routes } from '../../../utils/routing';

import {
  ApiRequestTerraformArgocd,
  TerraformArgocdFormData,
} from '../../models';
import { IoMdArrowRoundBack } from 'react-icons/io';
import Download from './Download';

const Argocd = () => {

  const { platform } = useFindPlatform(TerraformServices.ARGOCD);

  const navigate = useNavigate();

  return (
    <>
      <IoMdArrowRoundBack
        onClick={() => navigate(routes.terraformTemplate)}
        className="text-mainOrange-500 size-6 my-4 cursor-pointer"
      />
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
      <Download />
    </>
  );
};

export default Argocd;
