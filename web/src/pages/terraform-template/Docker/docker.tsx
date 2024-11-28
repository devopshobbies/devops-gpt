import { cn } from '@/lib/utils';
import { FC, useState } from 'react';

const Docker: FC = () => {
  const [services, setServices] = useState({
    docker_image: false,
    docker_container: false,
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
                'bg-orange-base hover:bg-orange-base/70': services.docker_image,
              })}
              onChange={() => handleServices('docker_image')}
            />
          </div>
          <div className="flex items-center justify-between w-full px-3 py-3">
            <p>Security Group</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70':
                  services.docker_container,
              })}
              onChange={() => handleServices('docker_container')}
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

export default Docker;
