import { FC, useState } from 'react';
import { ChevronDown, Plus, Trash2 } from 'lucide-react';
import { cn } from '@/lib/utils';
import { usePost } from '@/core/react-query';
import { API } from '@/enums/api.enums';
import {
  HelmTemplateBody,
  HelmTemplateResponse,
  helmTemplateSchema,
  helmTemplateValidationError,
} from './helm-template.types';
import { toast } from 'sonner';
import { isAxiosError } from 'axios';
import { accessModesOptions, sizeOptions } from './data/select-options';
import { useDownload } from '@/hooks';
import { useFieldArray, useForm } from 'react-hook-form';

import { FormWrapper } from '@/components/form/form-wrapper';
import { zodResolver } from '@hookform/resolvers/zod';
import { FormInput } from '@/components/form/form-input';
import { FormCheckbox } from '@/components/form/form-checkbox';
import { FormSelect } from '@/components/form/form-select';
import PodEnvironmentFields from './components/pod-environment-fields';
import type { THelmTemplate } from './helm-template.types';

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

  const defaultValues = {
    api_version: '',
    pods: [
      {
        name: '',
        image: '',
        replicas: '',
        persistance: {},
        environment: [
          {
            name: '',
            value: '',
          },
        ],
        stateless: false,
        ingress: {},
      },
    ],
  };

  const methods = useForm({
    resolver: zodResolver(helmTemplateSchema),
    defaultValues,
  });

  const { control } = methods;

  const {
    fields: pods,
    append,
    remove,
  } = useFieldArray({
    control,
    name: 'pods',
  });

  const [openPod, setOpenPod] = useState<number | null>(0);

  const handleAddPod = () => {
    append(defaultValues.pods[0]);
  };

  const handleRemovePod = (index: number) => {
    remove(index);
  };

  const handleSubmit = async (data: THelmTemplate) => {
    try {
      const body_data = data.pods.map((data) => {
        const { mode, accessModes, size } = data.persistance;

        return {
          ...data,
          persistance: {
            size: `${size}${mode.value}`,
            accessModes: accessModes.value,
          },
        };
      });

      const body: HelmTemplateBody = {
        api_version: data.api_version,
        pods: body_data,
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
    <div className="flex h-[calc(100%-56px)] w-full justify-center overflow-y-auto p-4 text-black-1 scrollbar-thin dark:text-white">
      <div className="h-full w-full max-w-[768px]">
        <FormWrapper methods={methods} onSubmit={handleSubmit}>
          <div className="flex flex-col w-full mb-4">
            <FormInput
              label="Api Version"
              id="api_version"
              name="api_version"
              placeholder="2"
              inputType="number"
              isNumber={true}
            />
          </div>
          <div className="flex items-center mb-4">
            <h1 className="text-2xl font-bold">Pods</h1>
            <button
              type="button"
              disabled={pods.length >= 6}
              onClick={handleAddPod}
              className="ml-4 btn btn-xs"
            >
              Add <Plus className="size-3" />
            </button>
          </div>
          <div className="space-y-4">
            {pods.map((pod, index) => (
              <div
                key={pod.id}
                className="w-full p-5 border border-gray-500 rounded-md"
              >
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
                    'h-full max-h-0 overflow-auto px-1 transition-all duration-500 scrollbar-thin',
                    {
                      'max-h-[1000px]': openPod === index,
                    },
                  )}
                >
                  <div className="grid grid-cols-2 gap-4">
                    <FormInput
                      id="pods_name"
                      name={`pods.${index}.name`}
                      label="Name"
                      placeholder="web"
                    />
                    <FormInput
                      id="pods_image"
                      name={`pods.${index}.image`}
                      label="Image"
                      placeholder="nginx"
                    />
                    <FormInput
                      id="pods_target_port"
                      name={`pods.${index}.target_port`}
                      label="Target Port"
                      placeholder="80"
                      inputType="number"
                      isNumber={true}
                    />
                    <FormInput
                      id="pods_replicas"
                      name={`pods.${index}.replicas`}
                      label="Replicas"
                      placeholder="1"
                      inputType="number"
                      isNumber={true}
                    />
                  </div>
                  <p className="mt-6 mb-2 text-base font-bold">Persistence</p>
                  <div className="flex flex-col mb-2">
                    <p className="mb-1">Size</p>
                    <div className="flex gap-3 [&>div]:flex-1">
                      <FormInput
                        name={`pods.${index}.persistance.size`}
                        label=""
                        placeholder="Value"
                      />
                      <FormSelect
                        name={`pods.${index}.persistance.mode`}
                        label=""
                        placeholder="Select..."
                        options={sizeOptions}
                      />
                    </div>
                  </div>
                  <div className="flex flex-col mb-2">
                    <label className="mb-1">Access Modes</label>
                    <FormSelect
                      name={`pods.${index}.persistance.accessModes`}
                      options={accessModesOptions}
                      label=""
                      placeholder="Select..."
                    />
                  </div>

                  <PodEnvironmentFields podIndex={index} />
                  <div className="flex justify-between mb-2 mt-7">
                    <label htmlFor="pods_stateless" className="mb-1">
                      Stateless
                    </label>
                    <FormCheckbox
                      id="pods_stateless"
                      name={`pods.${index}.stateless`}
                      label=""
                    />
                  </div>
                  <p className="mt-6 mb-2 text-base font-bold">Ingress</p>
                  <div className="flex justify-between mt-3 mb-2">
                    <label htmlFor="pods_stateless" className="mb-1">
                      Enabled
                    </label>
                    <FormCheckbox
                      id="pods_ingress_enabled"
                      name={`pods.${index}.ingress.enabled`}
                      label=""
                    />
                  </div>
                  <div className="flex flex-col mt-3 mb-2">
                    <FormInput
                      id="pods_ingress_host"
                      name={`pods.${index}.ingress.host`}
                      label="Host"
                      placeholder="www.example.com"
                    />
                  </div>
                </div>
              </div>
            ))}
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
        </FormWrapper>
      </div>
    </div>
  );
};

export default HelmTemplate;
