import { usePost } from '@/core/react-query';
import { cn } from '@/lib/utils';
import { FC, FormEvent, useState } from 'react';
import { IAMBody, IAMResponse } from './iam.types';
import { TerraformTemplateAPI } from '@/enums/api.enums';
import { useDownload } from '@/hooks';
import { toast } from 'sonner';

const IAM: FC = () => {
  const { mutateAsync: iamMutate, isPending: iamPending } = usePost<
    IAMResponse,
    IAMBody
  >(TerraformTemplateAPI.Iam, 'iam');
  const { download, isPending: downloadPending } = useDownload({
    folderName: 'MyTerraform',
    source: 'iam',
    downloadFileName: 'Iam',
  });

  const [services, setServices] = useState({
    iam_user: false,
    iam_group: false,
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
      const iamBody: IAMBody = {
        ...services,
      };

      await iamMutate(iamBody);
      await download();
    } catch (error) {
      console.log(error);
      toast.error('Something went wrong');
    }
  };

  return (
    <form
      onSubmit={handleForm}
      className="w-full max-w-96 text-black dark:text-white"
    >
      <div className="rounded-md border border-gray-500">
        <div className="divide-y divide-gray-500">
          <div className="flex w-full items-center justify-between px-3 py-3">
            <p>IAM User</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70': services.iam_user,
              })}
              onChange={() => handleServices('iam_user')}
            />
          </div>
          <div className="flex w-full items-center justify-between px-3 py-3">
            <p>IAM Group</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70': services.iam_group,
              })}
              onChange={() => handleServices('iam_group')}
            />
          </div>
        </div>
      </div>
      <button
        type="submit"
        disabled={iamPending || downloadPending}
        className="btn mt-3 w-full bg-orange-base text-white hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
      >
        {iamPending
          ? 'Wait...'
          : downloadPending
            ? 'Wait...'
            : 'Generate Terraform'}
      </button>
    </form>
  );
};

export default IAM;
