import { FC, useState } from 'react';
import { Plus, Trash2, ChevronDown } from 'lucide-react';
import { useFieldArray, useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { FormWrapper } from '@/components/form/form-wrapper';
import { FormInput } from '@/components/form/form-input';
import {
  DockerComposeBody,
  DockerComposeResponse,
  DockerComposeSchema,
  DockerComposeValidationError,
  TDockerCompose,
} from './docker-compose.type';
import { cn } from '@/lib/utils';
import ServiceNetworkFields from './components/service-network-fields';
import ServiceDependsOnFields from './components/service-depends-on-fields';
import { ServiceVolumesFields } from './components/service-volumes-fields';
import ServicePortsFields from './components/service-ports-fields';
import { ServiceBuildFields } from './components/service-build-fields';
import { toast } from 'sonner';
import { isAxiosError } from 'axios';
import { usePost } from '@/core/react-query';
import { API } from '@/enums/api.enums';
import ServiceEnvironmentFields from '../helm-template/components/pod-environment-fields';

const DockerCompose: FC = () => {
  const [openService, setOpenService] = useState<number | null>(0);

  const { mutateAsync: dockerComposeMutate, isPending: dockerComposePending } =
    usePost<DockerComposeResponse, DockerComposeBody>(
      API.DockerCompose,
      'docker-compose',
    );

  const defaultValues = {
    version: '3',
    services: [
      {
        name: 'web',
        build: {
          enabled: false,
          context: '.',
          dockerfile: 'Dockerfile',
          args: [],
        },
        command: 'command...',
        container_name: 'web_server',
        depends_on: [],
        environment: { foo: 'bar' },
        image: 'nginx:latest',
        networks: ['app_network'],
        ports: [],
        volumes: [],
      },
    ],
    networks: {
      app_network: {
        driver: 'bridge',
      },
    },
  };

  const methods = useForm({
    resolver: zodResolver(DockerComposeSchema),
    defaultValues,
  });

  const { control } = methods;

  const {
    fields: services,
    append,
    remove,
  } = useFieldArray({
    control,
    name: 'services',
  });

  const handleAddService = () => {
    append({
      name: '',
      build: {
        args: {},
        context: '',
        dockerfile: '',
      },
      command: '',
      container_name: '',
      depends_on: [''],
      environment: {},
      image: '',
      networks: [''],
      ports: [''],
      volumes: [''],
    });
  };

  const handleRemoveService = (index: number) => {
    remove(index);
  };

  const handleSubmit = async (data: TDockerCompose) => {
    try {
      console.log(data);

      // dockerComposeMutate(data)
    } catch (error) {
      console.log(error);
      if (isAxiosError<DockerComposeValidationError>(error)) {
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
            <FormInput label="Version" name="version" placeholder="3" />
          </div>

          <div className="mb-4 flex items-center">
            <h1 className="text-2xl font-bold">Services</h1>
            <button
              type="button"
              onClick={handleAddService}
              className="btn btn-xs ml-4"
            >
              Add <Plus className="size-3" />
            </button>
          </div>

          <div className="space-y-4">
            {services.map((service, index) => (
              <div
                key={service.id}
                className="w-full rounded-md border border-gray-500 p-5"
              >
                <div
                  className={cn(
                    'flex items-center justify-between transition-all delay-200',
                    {
                      'mb-7': openService === index,
                    },
                  )}
                >
                  <p className="font-semibold">Service #{index + 1}</p>
                  <div className="flex items-center gap-2">
                    {index > 0 && (
                      <button
                        type="button"
                        onClick={() => handleRemoveService(index)}
                      >
                        <Trash2 className="size-4" />
                      </button>
                    )}
                    <ChevronDown
                      className={cn('cursor-pointer transition-all', {
                        'rotate-180': openService === index,
                      })}
                      onClick={() =>
                        setOpenService(openService === index ? -1 : index)
                      }
                    />
                  </div>
                </div>
                <div
                  className={cn(
                    'h-full max-h-0 overflow-hidden px-1 transition-all duration-500',
                    {
                      'max-h-[1000px]': openService === index,
                    },
                  )}
                >
                  <div className="mb-4 flex flex-col">
                    <FormInput
                      id="service_name"
                      name={`services.${index}.name`}
                      label="Name"
                      placeholder="service name"
                    />
                  </div>
                  <div className="mb-4 flex flex-col">
                    <FormInput
                      id="image"
                      name={`services.${index}.image`}
                      label="Image"
                      placeholder="image"
                    />
                  </div>
                  <div className="mb-4 flex flex-col">
                    <FormInput
                      id="container_name"
                      name={`services.${index}.container_name`}
                      label="ContainerName"
                      placeholder="container_name"
                    />
                  </div>
                  <ServiceBuildFields serviceIndex={index} />
                  <ServiceNetworkFields serviceIndex={index} />
                  <ServiceDependsOnFields serviceIndex={index} />
                  <ServiceVolumesFields serviceIndex={index} />
                  <ServicePortsFields serviceIndex={index} />
                  <ServiceEnvironmentFields serviceIndex={index} />
                </div>
              </div>
            ))}
          </div>
          <button
            type="submit"
            disabled={dockerComposePending}
            className="btn mt-3 w-full bg-orange-base text-white hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
          >
            {dockerComposePending ? 'Generating...' : 'Generate'}
          </button>
        </FormWrapper>
      </div>
    </div>
  );
};

export default DockerCompose;
