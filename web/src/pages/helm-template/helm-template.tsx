import { FC, FormEvent, useState } from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { cn } from '@/lib/utils';
import { usePost } from '@/core/react-query';
import { API } from '@/enums/api.enums';
import {
  HelmTemplateBody,
  HelmTemplateResponse,
  helmTemplateValidationError,
} from './helm-template.types';
import { toast } from 'sonner';
import { isAxiosError } from 'axios';
import Select, { SingleValue } from 'react-select';
import { accessModesOptions, sizeOptions } from './data/select-options';
import { selectStyle } from './styles/helm-template.style';
import { OptionType } from '@/types/select.types';
import { useDownload } from '@/hooks';

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

  const [version, setVersion] = useState('');
  const [name, setName] = useState('');
  const [image, setImage] = useState('');
  const [targetPort, setTargetPort] = useState('');
  const [replicas, setReplicas] = useState('');
  const [sizeValue, setSizeValue] = useState('');
  const [sizeType, setSizeType] = useState<SingleValue<OptionType>>();
  const [accessModes, setAccessModes] = useState<SingleValue<OptionType>>();
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
  const [ingressHost, setIngressHost] = useState('');

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

  const handleEnvironmentChange = (
    index: number,
    field: string,
    value: string,
  ) => {
    setEnvironments((prev) =>
      prev.map((env, i) => (i === index ? { ...env, [field]: value } : env)),
    );
  };

  const handleForm = async (e: FormEvent) => {
    e.preventDefault();

    try {
      const body: HelmTemplateBody = {
        api_version: parseInt(version),
        pods: [
          {
            name,
            image,
            target_port: parseInt(targetPort),
            replicas: parseInt(replicas),
            persistance: {
              size: `${sizeValue}${sizeType?.value as string}`,
              accessModes: accessModes?.value as string,
            },
            environment: environments.map((env) => ({
              name: env.name,
              value: env.value,
            })),
            stateless,
            ingress: {
              enabled: ingress,
              host: ingressHost,
            },
          },
        ],
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
    <div className="flex h-[calc(100%-56px)] w-full justify-center overflow-y-auto scrollbar-thin">
      <form onSubmit={handleForm} className="h-full w-full max-w-[768px]">
        <div className="flex flex-col w-full mb-4">
          <label htmlFor="api_version" className="mb-1">
            Api Version
          </label>
          <input
            id="api_version"
            placeholder="2"
            value={version}
            onChange={(e) => setVersion(e.target.value)}
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
            placeholder="web"
            value={name}
            onChange={(e) => setName(e.target.value)}
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
            value={image}
            onChange={(e) => setImage(e.target.value)}
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <div className="flex flex-col mb-4">
          <label htmlFor="pods_target_port" className="mb-1">
            Target Port
          </label>
          <input
            id="pods_target_port"
            placeholder="80"
            value={targetPort}
            onChange={(e) => setTargetPort(e.target.value)}
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
            value={replicas}
            onChange={(e) => setReplicas(e.target.value)}
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <h2 className="mb-2 text-lg font-bold">Persistence</h2>
        <div className="flex flex-col mb-7">
          <p className="mb-1">Size</p>
          <div className="flex items-center gap-3">
            <input
              placeholder="Value"
              type="number"
              value={sizeValue}
              onChange={(e) => setSizeValue(e.target.value)}
              className="w-full gap-2 px-3 py-2 rounded-md outline-none"
            />
            <Select
              placeholder="Select..."
              options={sizeOptions}
              value={sizeType}
              onChange={(e) => setSizeType(e)}
              className="w-full h-10"
              styles={selectStyle}
            />
          </div>
        </div>
        <div className="flex flex-col mb-2">
          <label className="mb-1">Access Modes</label>
          <Select
            placeholder="Select..."
            options={accessModesOptions}
            value={accessModes}
            onChange={(e) => setAccessModes(e)}
            styles={selectStyle}
          />
        </div>
        <div className="flex items-center mt-5 mb-2">
          <h3 className="text-lg font-bold">Environments</h3>
          <button
            type="button"
            className="ml-4 btn btn-xs"
            onClick={handleAddEnvironment}
          >
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
                placeholder={env.namePlaceholder}
                value={env.name}
                onChange={(e) =>
                  handleEnvironmentChange(index, 'name', e.target.value)
                }
                className="w-full h-12 px-2 outline-none rounded-s-md"
              />
              <input
                placeholder={env.valuePlaceholder}
                value={env.value}
                onChange={(e) =>
                  handleEnvironmentChange(index, 'value', e.target.value)
                }
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
            value={ingressHost}
            onChange={(e) => setIngressHost(e.target.value)}
            className="w-full px-3 py-2 rounded-md outline-none"
          />
        </div>
        <button
          type="submit"
          disabled={helmTemplatePending}
          className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
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
