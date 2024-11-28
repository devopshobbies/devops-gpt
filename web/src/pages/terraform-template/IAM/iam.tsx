import { cn } from '@/lib/utils';
import { FC, useState } from 'react';

const IAM: FC = () => {
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

  return (
    <div className="w-full max-w-96">
      <div className="border border-gray-500 rounded-md">
        <div className="divide-y divide-gray-500">
          <div className="flex items-center justify-between w-full px-3 py-3">
            <p>IAM User</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70': services.iam_user,
              })}
              onChange={() => handleServices('iam_user')}
            />
          </div>
          <div className="flex items-center justify-between w-full px-3 py-3">
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
      <button className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70">
        Submit
      </button>
    </div>
  );
};

export default IAM;
