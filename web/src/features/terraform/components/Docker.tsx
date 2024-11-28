import { useNavigate } from 'react-router-dom';
import PlatformBox from '../../../components/internal-ui/PlatformBox';
import useFindPlatform from '../../../hooks/useFindPlatform';
import { TerraformServices } from '../../constants';
import { routes } from '../../../utils/routing';

import {
  ApiRequestTerraformDocker,
  TerraformDockerFormData,
} from '../../models';
import { IoMdArrowRoundBack } from 'react-icons/io';
import Download from './Download';

const Docker = () => {
  const { platform } = useFindPlatform(TerraformServices.DOCKER);

  const navigate = useNavigate();

  return (
    <>
      <IoMdArrowRoundBack
        onClick={() => navigate(routes.terraformTemplate)}
        className="text-mainOrange-500 size-6 my-4 cursor-pointer"
      />
      {platform && (
        <PlatformBox
          defaultValues={platform.defaultValues as TerraformDockerFormData}
          endpoint={platform.endpoint}
          fieldProperties={platform.fieldProperties}
          mapperFunction={
            platform.mapperFunction as () => ApiRequestTerraformDocker
          }
          serviceName={platform.serviceName}
        />
      )}
      <Download />
    </>
  );
};
export default Docker;
