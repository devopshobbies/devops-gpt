import PlatformBox from '../../../components/internal-ui/PlatformBox';
import useFindPlatform from '../../../hooks/useFindPlatform';
import { TerraformServices } from '../../constants';
import { ApiRequestTerraformIam, TerraformIAMFormData } from '../../models';
import { IoMdArrowRoundBack } from 'react-icons/io';
import { useNavigate } from 'react-router-dom';
import { routes } from '../../../utils/routing';
import Download from './Download';

const IAM = () => {
  const { platform } = useFindPlatform(TerraformServices.IAM);
  const navigate = useNavigate();

  return (
    <>
      <IoMdArrowRoundBack
        onClick={() => navigate(routes.terraformTemplate)}
        className="text-mainOrange-500 size-6 my-4 cursor-pointer"
      />
      {platform && (
        <PlatformBox
          defaultValues={platform.defaultValues as TerraformIAMFormData}
          endpoint={platform.endpoint}
          fieldProperties={platform.fieldProperties}
          mapperFunction={
            platform.mapperFunction as () => ApiRequestTerraformIam
          }
          serviceName={platform.serviceName}
        />
      )}
      <Download />
    </>
  );
};

export default IAM;
