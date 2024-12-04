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
import type { HelmTemplate } from './helm-template.types';

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

  const handleSubmit = async (data: HelmTemplate) => {
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
          <div className="mb-4 flex w-full flex-col">
            <FormInput
              label="Api Version"
              id="api_version"
              name="api_version"
              placeholder="2"
              inputType="number"
              isNumber={true}
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
              <div
                key={pod.id}
                className="w-full rounded-md border border-gray-500 p-5"
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
                    'h-full max-h-0 overflow-hidden px-1 transition-all duration-500',
                    {
                      'max-h-[1500px]': openPod === index,
                    },
                  )}
                >
                  <div className="mb-4 flex flex-col">
                    <FormInput
                      id="pods_name"
                      name={`pods.${index}.name`}
                      label="Name"
                      placeholder="web"
                    />
                  </div>
                  <div className="mb-4 flex flex-col">
                    <FormInput
                      id="pods_image"
                      name={`pods.${index}.image`}
                      label="Image"
                      placeholder="nginx"
                    />
                  </div>
                  <div className="mb-4 flex flex-col">
                    <FormInput
                      id="pods_target_port"
                      name={`pods.${index}.target_port`}
                      label="Target Port"
                      placeholder="80"
                      inputType="number"
                      isNumber={true}
                    />
                  </div>
                  <div className="mb-2 flex flex-col">
                    <FormInput
                      id="pods_replicas"
                      name={`pods.${index}.replicas`}
                      label="Replicas"
                      placeholder="1"
                      inputType="number"
                      isNumber={true}
                    />
                  </div>
                  <p className="mb-2 mt-6 text-base font-bold">Persistence</p>
                  <div className="mb-2 flex flex-col">
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
                  <div className="mb-2 flex flex-col">
                    <label className="mb-1">Access Modes</label>
                    <FormSelect
                      name={`pods.${index}.persistance.accessModes`}
                      options={accessModesOptions}
                      label=""
                      placeholder="Select..."
                    />
                  </div>

                  <PodEnvironmentFields podIndex={index} />
                  <div className="mb-2 mt-7 flex justify-between">
                    <label htmlFor="pods_stateless" className="mb-1">
                      Stateless
                    </label>
                    <FormCheckbox
                      id="pods_stateless"
                      name={`pods.${index}.stateless`}
                      label=""
                    />
                  </div>
                  <p className="mb-2 mt-6 text-base font-bold">Ingress</p>
                  <div className="mb-2 mt-3 flex justify-between">
                    <label htmlFor="pods_stateless" className="mb-1">
                      Enabled
                    </label>
                    <FormCheckbox
                      id="pods_ingress_enabled"
                      name={`pods.${index}.ingress.enabled`}
                      label=""
                    />
                  </div>
                  <div className="mb-2 mt-3 flex flex-col">
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
            className="btn mt-3 w-full bg-orange-base text-white hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
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
