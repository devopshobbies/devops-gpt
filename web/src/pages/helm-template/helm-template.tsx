import { FC, FormEvent, useState } from 'react';
import { ChevronDown, Plus, Trash2 } from 'lucide-react';
import { cn } from '@/lib/utils';
import { usePost } from '@/core/react-query';
import { API } from '@/enums/api.enums';
import {
  HelmTemplateBody,
  HelmTemplateResponse,
  helmTemplateValidationError,
  Pod,
} from './helm-template.types';
import { toast } from 'sonner';
import { isAxiosError } from 'axios';
import Select from 'react-select';
import { accessModesOptions, sizeOptions } from './data/select-options';
import { selectStyle } from './styles/helm-template.style';
import { useDownload, useStyle } from '@/hooks';

const HelmTemplate: FC = () => {
  const { mutateAsync: helmTemplateMutate, isPending: helmTemplatePending } =
    usePost<HelmTemplateResponse, HelmTemplateBody>(
      API.HelmTemplate,
      'helm-template',
    );
  const { download, isPending: downloadPending } = useDownload({
    downloadFileName: 'helm-template',
    source: 'helm',
    folderName: 'MyHelm',
  });

  const [openPod, setOpenPod] = useState<number | null>(0);
  const [apiVersion, setApiVersion] = useState('');
  const [pods, setPods] = useState<Pod[]>([
    {
      name: '',
      image: '',
      target_port: null,
      replicas: null,
      persistance: {
        accessModes: '',
        size: '',
      },
      environment: [
        {
          name: '',
          value: '',
        },
      ],
      stateless: false,
      ingress: {
        enabled: false,
        host: '',
      },
    },
  ]);
  const { darkMode } = useStyle();

  const handleAddEnvironment = (podIndex: number) => {
    const newPods = [...pods];
    newPods[podIndex].environment.push({
      name: '',
      value: '',
    });
    setPods(newPods);
  };

  const handleRemoveEnvironment = (podIndex: number, envIndex: number) => {
    setPods((prev) => {
      const newPods = [...prev];
      newPods[podIndex].environment.splice(envIndex, 1);
      return newPods;
    });
  };

  const handleEnvironmentChange = (
    podIndex: number,
    envIndex: number,
    field: 'name' | 'value',
    value: string,
  ) => {
    setPods((prev) => {
      const newPods = [...prev];
      newPods[podIndex].environment[envIndex][field] = value;
      return newPods;
    });
  };

  const updatePod = (index: number, path: string[], value: any) => {
    setPods((prevPods) => {
      const updatedPods = [...prevPods];
      let current: any = updatedPods[index];

      for (let i = 0; i < path.length - 1; i++) {
        current = current[path[i]];
      }

      current[path[path.length - 1]] = value;

      return updatedPods;
    });
  };

  const handleUpdatePersistence = (
    currentValue: string,
    newPart: string | number,
    type: 'number' | 'unit' | 'accessModes',
    item: 'size' | 'accessModes',
    podIndex: number,
  ) => {
    let newValue;
    if (type === 'number') {
      const currentUnit = currentValue.match(/\D+$/)?.[0] || '';
      newValue = `${newPart}${currentUnit}`;
    } else if (type === 'unit') {
      const currentNumber = currentValue.replace(/\D+$/, '');
      newValue = `${currentNumber}${newPart}`;
    } else if (type === 'accessModes') {
      newValue = newPart;
    }

    updatePod(podIndex, ['persistance', item], newValue);
  };

  const handleAddPod = () => {
    setPods((prev) => {
      return [
        ...prev,
        {
          name: '',
          image: '',
          target_port: null,
          replicas: null,
          persistance: {
            accessModes: '',
            size: '',
          },
          environment: [
            {
              name: '',
              value: '',
            },
          ],
          stateless: false,
          ingress: {
            enabled: false,
            host: '',
          },
        },
      ];
    });
  };

  const handleRemovePod = (index: number) => {
    setPods((prev) => {
      return prev.filter((_, i) => i !== index);
    });
  };

  const handleForm = async (e: FormEvent) => {
    e.preventDefault();

    try {
      const body: HelmTemplateBody = {
        api_version: parseInt(apiVersion),
        pods,
      };

      await helmTemplateMutate(body);
      await download();
    } catch (error) {
      console.log(error);
      if (isAxiosError<helmTemplateValidationError>(error)) {
        toast.error(
          `${error.response?.data.detail[0].loc[error.response?.data.detail[0].loc.length - 1]} ${error.response?.data.detail[0].msg}`,
        );
      } else {
        toast.error('Something went wrong');
      }
    }
  };

  return (
    <div className="text-black-1 flex h-[calc(100%-56px)] w-full justify-center overflow-y-auto p-4 scrollbar-thin dark:text-white">
      <form onSubmit={handleForm} className="h-full w-full max-w-[768px]">
        <div className="mb-4 flex w-full flex-col">
          <label htmlFor="api_version" className="mb-1">
            Api Version
          </label>
          <input
            id="api_version"
            placeholder="2"
            value={apiVersion}
            onChange={(e) => setApiVersion(e.target.value)}
            className="dark:bg-black-1 order w-full rounded-md border border-gray-200 px-3 py-2 outline-none dark:border-none"
          />
        </div>
        <div className="mb-4 flex items-center">
          <h1 className="text-2xl font-bold">Pods</h1>
          <button
            type="button"
            disabled={pods.length >= 6}
            onClick={handleAddPod}
            className="btn btn-xs ml-4"
          >
            Add <Plus className="size-3" />
          </button>
        </div>
        <div className="space-y-4">
          {pods.map((pod, index) => (
            <div className="w-full rounded-md border border-gray-500 p-5">
              <div
                className={cn(
                  'flex items-center justify-between transition-all delay-200',
                  {
                    'mb-7': openPod === index,
                  },
                )}
              >
                <p className="font-semibold">Pod #{index + 1}</p>
                <div className="flex items-center gap-2">
                  {index > 0 && (
                    <button
                      type="button"
                      onClick={() => handleRemovePod(index)}
                    >
                      <Trash2 className="size-4" />
                    </button>
                  )}
                  <ChevronDown
                    className={cn('cursor-pointer transition-all', {
                      'rotate-180': openPod === index,
                    })}
                    onClick={() => setOpenPod(openPod === index ? -1 : index)}
                  />
                </div>
              </div>
              <div
                className={cn(
                  'h-full max-h-0 overflow-hidden px-1 transition-all duration-500',
                  {
                    'max-h-[1000px]': openPod === index,
                  },
                )}
              >
                <div className="mb-4 flex flex-col">
                  <label htmlFor="pods_name" className="mb-1">
                    Name
                  </label>
                  <input
                    id="pods_name"
                    placeholder="web"
                    value={pod.name}
                    onChange={(e) => updatePod(index, ['name'], e.target.value)}
                    className="dark:bg-black-1 w-full rounded-md border border-gray-200 px-3 py-2 outline-none dark:border-none"
                  />
                </div>
                <div className="mb-4 flex flex-col">
                  <label htmlFor="pods_image" className="mb-1">
                    Image
                  </label>
                  <input
                    id="pods_image"
                    placeholder="nginx"
                    value={pod.image}
                    onChange={(e) =>
                      updatePod(index, ['image'], e.target.value)
                    }
                    className="dark:bg-black-1 w-full rounded-md border border-gray-200 px-3 py-2 outline-none dark:border-none"
                  />
                </div>
                <div className="mb-4 flex flex-col">
                  <label htmlFor="pods_target_port" className="mb-1">
                    Target Port
                  </label>
                  <input
                    id="pods_target_port"
                    placeholder="80"
                    value={pod.target_port || ''}
                    onChange={(e) =>
                      updatePod(index, ['target_port'], e.target.value)
                    }
                    className="dark:bg-black-1 w-full rounded-md border border-gray-200 px-3 py-2 outline-none dark:border-none"
                  />
                </div>
                <div className="mb-2 flex flex-col">
                  <label htmlFor="pods_replicas" className="mb-1">
                    Replicas
                  </label>
                  <input
                    id="pods_replicas"
                    placeholder="1"
                    value={pod.replicas || ''}
                    onChange={(e) =>
                      updatePod(index, ['replicas'], e.target.value)
                    }
                    className="dark:bg-black-1 w-full rounded-md border border-gray-200 px-3 py-2 outline-none dark:border-none"
                  />
                </div>
                <p className="mb-2 mt-6 text-base font-bold">Persistence</p>
                <div className="mb-2 flex flex-col">
                  <p className="mb-1">Size</p>
                  <div className="flex items-center gap-3">
                    <input
                      placeholder="Value"
                      type="number"
                      onChange={(e) =>
                        handleUpdatePersistence(
                          pod.persistance.size,
                          e.target.value,
                          'number',
                          'size',
                          index,
                        )
                      }
                      className="dark:bg-black-1 w-full gap-2 rounded-md border border-gray-200 px-3 py-2 outline-none dark:border-none"
                    />
                    <Select
                      placeholder="Select..."
                      options={sizeOptions}
                      onChange={(e) =>
                        handleUpdatePersistence(
                          pod.persistance.size,
                          e?.value as string,
                          'unit',
                          'size',
                          index,
                        )
                      }
                      className="h-10 w-full"
                      styles={selectStyle(darkMode)}
                    />
                  </div>
                </div>
                <div className="mb-2 flex flex-col">
                  <label className="mb-1">Access Modes</label>
                  <Select
                    placeholder="Select..."
                    options={accessModesOptions}
                    onChange={(e) =>
                      handleUpdatePersistence(
                        pod.persistance.accessModes,
                        e?.value as string,
                        'accessModes',
                        'accessModes',
                        index,
                      )
                    }
                    styles={selectStyle(darkMode)}
                  />
                </div>
                <div className="mb-2 mt-6 flex items-center">
                  <p className="text-base font-bold">Environments</p>
                  <button
                    type="button"
                    onClick={() => handleAddEnvironment(index)}
                    className="btn btn-xs ml-4"
                  >
                    Add <Plus className="size-3" />
                  </button>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  {pod.environment.map((env, envIdx) => (
                    <div
                      className="flex items-center divide-x divide-gray-200 rounded-md border border-gray-200 dark:divide-gray-500 dark:border-gray-500"
                      key={index}
                    >
                      <input
                        placeholder={'Env'}
                        value={env.name}
                        onChange={(e) =>
                          handleEnvironmentChange(
                            index,
                            envIdx,
                            'name',
                            e.target.value,
                          )
                        }
                        className="h-12 w-full rounded-s-md px-2 outline-none"
                      />
                      <input
                        placeholder={'Hi'}
                        value={env.value}
                        onChange={(e) =>
                          handleEnvironmentChange(
                            index,
                            envIdx,
                            'value',
                            e.target.value,
                          )
                        }
                        className={cn(
                          'dark:bg-black-1 h-12 w-full px-2 outline-none',
                          {
                            'rounded-e-md': index === 0,
                          },
                        )}
                      />
                      {envIdx > 0 && (
                        <button
                          onClick={() => handleRemoveEnvironment(index, envIdx)}
                          className="btn btn-error rounded-e-md rounded-s-none"
                        >
                          <Trash2 />
                        </button>
                      )}
                    </div>
                  ))}
                </div>
                <div className="mb-2 mt-7 flex justify-between">
                  <label htmlFor="pods_stateless" className="mb-1">
                    Stateless
                  </label>
                  <input
                    id="pods_stateless"
                    type="checkbox"
                    className={cn('toggle border-gray-500 bg-gray-500', {
                      'bg-orange-base hover:bg-orange-base/70': pod.stateless,
                    })}
                    onChange={() =>
                      updatePod(index, ['stateless'], !pod.stateless)
                    }
                  />
                </div>
                <p className="mb-2 mt-6 text-base font-bold">Ingress</p>
                <div className="mb-2 mt-3 flex justify-between">
                  <label htmlFor="pods_ingress_enabled" className="mb-1">
                    Enabled
                  </label>
                  <input
                    id="pods_ingress_enabled"
                    type="checkbox"
                    checked={pod.ingress.enabled}
                    className={cn('toggle border-gray-500 bg-gray-500', {
                      'bg-orange-base hover:bg-orange-base/70':
                        pod.ingress.enabled,
                    })}
                    onChange={() =>
                      updatePod(
                        index,
                        ['ingress', 'enabled'],
                        !pod.ingress.enabled,
                      )
                    }
                  />
                </div>
                <div className="mb-2 mt-3 flex flex-col">
                  <label htmlFor="pods_ingress_host" className="mb-1">
                    Host
                  </label>
                  <input
                    id="pods_ingress_host"
                    placeholder="www.example.com"
                    value={pod.ingress.host}
                    onChange={(e) =>
                      updatePod(index, ['ingress', 'host'], e.target.value)
                    }
                    className="w-full rounded-md border border-gray-200 px-3 py-2 outline-none dark:border-none"
                  />
                </div>
              </div>
            </div>
          ))}
        </div>
        <button
          type="submit"
          disabled={helmTemplatePending}
          className="btn mt-3 w-full bg-orange-base text-white hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
        >
          {helmTemplatePending
            ? 'Generating...'
            : downloadPending
              ? 'Downloading...'
              : 'Generate'}
        </button>
      </form>
    </div>
  );
};

export default HelmTemplate;
