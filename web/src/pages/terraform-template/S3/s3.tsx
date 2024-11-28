import { cn } from '@/lib/utils';
import { FC, useState } from 'react';

const S3: FC = () => {
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

  return (
    <div className="w-full max-w-96">
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
      <button className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70">
        Submit
      </button>
    </div>
  );
};

export default S3;
