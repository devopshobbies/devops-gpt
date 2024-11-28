import { FC, useState } from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { cn } from '@/lib/utils';

const HelmTemplate: FC = () => {
  const [environments, setEnvironments] = useState([
    {
      name: '',
      value: '',
      namePlaceholder: 'ENV1',
      valuePlaceholder: 'Hi',
    },
  ]);
  const [stateless, setStateless] = useState(false);
  const [ingress, setIngress] = useState(false);

  const handleAddEnvironment = () => {
    setEnvironments((prev) => [
      ...prev,
      {
        name: '',
        value: '',
        namePlaceholder: `ENV${prev.length + 1}`,
        valuePlaceholder: 'Hi',
      },
    ]);
  };

  const handleRemoveEnvironment = (index: number) => {
    setEnvironments((prev) => prev.filter((_, i) => i !== index));
  };

  return (
    <div className="scrollbar-thin flex h-[calc(100%-56px)] w-full items-center justify-center overflow-y-auto">
      <form className="flex h-full w-full max-w-[768px] flex-col justify-center">
        <div className="flex flex-col w-full mb-4">
          <label htmlFor="api_version" className="mb-1">
            Api Version
          </label>
          <input
            id="api_version"
            placeholder="2"
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <h1 className="mb-4 text-2xl font-bold">Pods</h1>
        <div className="flex flex-col mb-4">
          <label htmlFor="pods_name" className="mb-1">
            Name
          </label>
          <input
            id="pods_name"
            placeholder="2"
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <div className="flex flex-col mb-4">
          <label htmlFor="pods_image" className="mb-1">
            Image
          </label>
          <input
            id="pods_image"
            placeholder="nginx"
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <div className="flex flex-col mb-4">
          <label htmlFor="pods_target_port" className="mb-1">
            Target Port
          </label>
          <input
            id="pods_target_port"
            placeholder="nginx"
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <div className="flex flex-col mb-2">
          <label htmlFor="pods_replicas" className="mb-1">
            Replicas
          </label>
          <input
            id="pods_replicas"
            placeholder="1"
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <h2 className="mb-2 text-lg font-bold">Persistence</h2>
        <div className="flex flex-col mb-7">
          <label htmlFor="pods_persistence_size" className="mb-1">
            Size
          </label>
          <input
            id="pods_persistence_size"
            placeholder="iG1"
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <div className="flex flex-col mb-2">
          <label htmlFor="pods_accessModes" className="mb-1">
            Access Modes
          </label>
          <input
            id="pods_accessModes"
            placeholder="ReadWriteOnce"
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <div className="flex items-center mt-5 mb-2">
          <h3 className="text-lg font-bold">Environments</h3>
          <button className="ml-4 btn btn-xs" onClick={handleAddEnvironment}>
            Add <Plus className="size-3" />
          </button>
        </div>
        <div className="grid grid-cols-2 gap-4">
          {environments.map((env, index) => (
            <div
              className="flex items-center border border-gray-500 divide-x divide-gray-500 rounded-md"
              key={index}
            >
              <input
                value={env.name}
                placeholder={env.namePlaceholder}
                className="w-full h-12 px-2 outline-none rounded-s-md"
              />
              <input
                value={env.value}
                placeholder={env.valuePlaceholder}
                className={cn('h-12 w-full px-2 outline-none', {
                  'rounded-e-md': index === 0,
                })}
              />
              {index > 0 && (
                <button
                  onClick={() => handleRemoveEnvironment(index)}
                  className="btn btn-error rounded-e-md rounded-s-none"
                >
                  <Trash2 />
                </button>
              )}
            </div>
          ))}
        </div>
        <div className="flex justify-between mb-2 mt-7">
          <label htmlFor="pods_stateless" className="mb-1">
            Stateless
          </label>
          <input
            id="pods_stateless"
            type="checkbox"
            className={cn('toggle border-gray-500 bg-gray-500', {
              'bg-orange-base hover:bg-orange-base/70': stateless,
            })}
            onChange={() => setStateless(!stateless)}
          />
        </div>
        <h4 className="mt-5 text-lg font-bold">Ingress</h4>
        <div className="flex justify-between mt-3 mb-2">
          <label htmlFor="pods_ingress_enabled" className="mb-1">
            Enabled
          </label>
          <input
            id="pods_ingress_enabled"
            type="checkbox"
            className={cn('toggle border-gray-500 bg-gray-500', {
              'bg-orange-base hover:bg-orange-base/70': ingress,
            })}
            onChange={() => setIngress(!ingress)}
          />
        </div>
        <div className="flex flex-col mt-3 mb-2">
          <label htmlFor="pods_ingress_host" className="mb-1">
            Host
          </label>
          <input
            id="pods_ingress_host"
            placeholder="www.example.com"
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <button className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70">
          Submit
        </button>
      </form>
    </div>
  );
};

export default HelmTemplate;
