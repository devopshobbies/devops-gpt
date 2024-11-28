import PlatformBox from '../../../components/internal-ui/PlatformBox';
import useFindPlatform from '../../../hooks/useFindPlatform';
import { TerraformServices } from '../../constants';
import { ApiRequestTerraformEc2, TerraformEc2FormData } from '../../models';
import { useNavigate } from 'react-router-dom';
import { IoMdArrowRoundBack } from 'react-icons/io';
import { routes } from '../../../utils/routing';
import Download from './Download';

const EC2 = () => {
  const { platform } = useFindPlatform(TerraformServices.EC2);

  const navigate = useNavigate();

  return (
    <>
      <IoMdArrowRoundBack
        onClick={() => navigate(routes.terraformTemplate)}
        className="text-mainOrange-500 size-6 my-4 cursor-pointer"
      />
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
          <Download />
    </>
  );
};

export default EC2;
