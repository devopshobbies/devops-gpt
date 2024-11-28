import PlatformBox from '../../../components/internal-ui/PlatformBox';
import useFindPlatform from '../../../hooks/useFindPlatform';
import { TerraformServices } from '../../constants';
import { ApiRequestTerraformS3, TerraformS3FormData } from '../../models';
import { useNavigate } from 'react-router-dom';
import { IoMdArrowRoundBack } from 'react-icons/io';
import { routes } from '../../../utils/routing';
import Download from './Download';

export const S3 = () => {
  const { platform } = useFindPlatform(TerraformServices.S3);

  const navigate = useNavigate();

  return (
    <>
      <IoMdArrowRoundBack
        onClick={() => navigate(routes.terraformTemplate)}
        className="text-mainOrange-500 size-6 my-4 cursor-pointer"
      />
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
      <Download />
    </>
  );
};

export default S3;
