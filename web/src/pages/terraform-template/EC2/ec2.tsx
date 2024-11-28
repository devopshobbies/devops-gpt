import { cn } from '@/lib/utils';
import { useState } from 'react';

const EC2 = () => {
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

  return (
    <div className="w-full max-w-96">
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
      <button className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70">
        Submit
      </button>
    </div>
  );
};

export default EC2;
