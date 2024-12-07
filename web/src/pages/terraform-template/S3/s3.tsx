import { TerraformTemplateAPI } from '@/enums/api.enums';
import { useDownload } from '@/hooks';
import { cn } from '@/lib/utils';
import { FC, FormEvent, useState } from 'react';
import { S3Body, S3Response } from './s3.types';
import { toast } from 'sonner';
import { usePost } from '@/core/react-query';
import { isAxiosError } from 'axios';

const S3: FC = () => {
  const { mutateAsync: s3Mutate, isPending: s3Pending } = usePost<
    S3Response,
    S3Body
  >(TerraformTemplateAPI.S3, 's3');
  const { download, isPending: downloadPending } = useDownload({
    folderName: 'MyTerraform',
    source: 's3',
    downloadFileName: 'S3',
  });

  const [services, setServices] = useState({
    s3_bucket: false,
    bucket_versioning: false,
  });

  const handleServices = (serviceItem: keyof typeof services) => {
    setServices((prev) => ({
      ...prev,
      [serviceItem]: !prev[serviceItem],
    }));
  };

  const handleForm = async (e: FormEvent) => {
    e.preventDefault();

    try {
      const s3Body: S3Body = {
        ...services,
      };

      await s3Mutate(s3Body);
      await download();
    } catch (error) {
      if (isAxiosError(error)) {
        if (error.response?.data.detail) {
          toast.error(error.response.data.detail);
        } else {
          toast.error('Something went wrong');
        }
      }
    }
  };

  return (
    <form
      onSubmit={handleForm}
      className="w-full text-black max-w-96 dark:text-white"
    >
      <div className="border border-gray-500 rounded-md">
        <div className="divide-y divide-gray-500">
          <div className="flex items-center justify-between w-full px-3 py-3">
            <p>S3 Bucket</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70': services.s3_bucket,
              })}
              onChange={() => handleServices('s3_bucket')}
            />
          </div>
          <div className="flex items-center justify-between w-full px-3 py-3">
            <p>Bucket Versioning</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70':
                  services.bucket_versioning,
              })}
              onChange={() => handleServices('bucket_versioning')}
            />
          </div>
        </div>
      </div>
      <button
        type="submit"
        disabled={s3Pending || downloadPending}
        className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
      >
        {s3Pending
          ? 'Wait...'
          : downloadPending
            ? 'Wait...'
            : 'Generate Terraform'}
      </button>
    </form>
  );
};

export default S3;
