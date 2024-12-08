import { usePost } from '@/core/react-query';
import { useDownload } from '@/hooks';
import { cn } from '@/lib/utils';
import { FormEvent, useState } from 'react';
import { EC2Body, EC2Response } from './ec2.types';
import { TerraformTemplateAPI } from '@/enums/api.enums';
import { toast } from 'sonner';
import { isAxiosError } from 'axios';

const EC2 = () => {
  const { mutateAsync: ec2Mutate, isPending: ec2Pending } = usePost<
    EC2Response,
    EC2Body
  >(TerraformTemplateAPI.EC2, 'ec2');
  const { download, isPending: downloadPending } = useDownload({
    folderName: 'MyTerraform',
    source: 'ec2',
    downloadFileName: 'EC2',
  });

  const [services, setServices] = useState({
    key_pair: false,
    security_group: false,
    aws_instance: false,
    ami_from_instance: false,
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
      const ec2Body: EC2Body = {
        ...services,
      };

      await ec2Mutate(ec2Body);
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
            <p>Key Pair</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70': services.key_pair,
              })}
              onChange={() => handleServices('key_pair')}
            />
          </div>
          <div className="flex items-center justify-between w-full px-3 py-3">
            <p>Security Group</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70':
                  services.security_group,
              })}
              onChange={() => handleServices('security_group')}
            />
          </div>
          <div className="flex items-center justify-between w-full px-3 py-3">
            <p>AWS Instance</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70': services.aws_instance,
              })}
              onChange={() => handleServices('aws_instance')}
            />
          </div>
          <div className="flex items-center justify-between w-full px-3 py-3">
            <p>AMI From Instance</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70':
                  services.ami_from_instance,
              })}
              onChange={() => handleServices('ami_from_instance')}
            />
          </div>
        </div>
      </div>
      <button
        type="submit"
        disabled={ec2Pending || downloadPending}
        className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
      >
        {ec2Pending
          ? 'Wait...'
          : downloadPending
            ? 'Wait...'
            : 'Generate Terraform'}
      </button>
    </form>
  );
};

export default EC2;
