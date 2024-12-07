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
  INetworkConfig,
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
import ServiceEnvironmentFields from './components/service-environment-fields';
import { convertKVtoObject, convertServicesToObject } from '@/lib/helper';
import NetworkFields from './components/network-fields';
import { useDownload } from '@/hooks';

const DockerCompose: FC = () => {
  const [openService, setOpenService] = useState<number | null>(0);

  const { mutateAsync: dockerComposeMutate, isPending: dockerComposePending } =
    usePost<DockerComposeResponse, DockerComposeBody>(
      API.DockerCompose,
      'docker-compose',
    );

  const { download, isPending: downloadPending } = useDownload({
    downloadFileName: 'DockerCompose',
    source: 'docker',
    folderName: 'MyCompose',
  });

  const defaultValues = {
    version: '',
    services: [
      {
        name: '',
        build: {
          context: '',
          dockerfile: '',
          args: [
            {
              key: '',
              value: '',
            },
          ],
        },
        command: '',
        container_name: '',
        environment: [
          {
            key: '',
            value: '',
          },
        ],
        image: '',
        ports: [
          {
            value: '',
          },
        ],
        volumes: [
          {
            value: '',
          },
        ],
        networks: [
          {
            value: '',
          },
        ],
        depends_on: [{ value: '' }],
      },
    ],
    networks: {
      custom: false,
      app_network: [
        {
          network_name: '',
          driver: { value: 'bridge', label: 'Bridge' },
        },
      ],
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
      build: {
        args: [
          {
            key: '',
            value: '',
          },
        ],
        context: '',
        dockerfile: '',
      },
      name: '',
      command: '',
      container_name: '',
      image: '',
      environment: [
        {
          key: '',
          value: '',
        },
      ],
      depends_on: [
        {
          value: '',
        },
      ],
      networks: [
        {
          value: '',
        },
      ],
      ports: [
        {
          value: '',
        },
      ],
      volumes: [
        {
          value: '',
        },
      ],
    });
  };

  const handleRemoveService = (index: number) => {
    remove(index);
  };

  const handleSubmit = async (data: TDockerCompose) => {
    try {
      const refactoredService = data.services.map(
        ({ build: { enabled, ...buildRest }, ...service }) => ({
          ...service,
          ...(service.environment && {
            environment: convertKVtoObject(service.environment),
          }),
          ...(enabled
            ? {
                build: {
                  ...buildRest,
                  args: convertKVtoObject(buildRest.args),
                },
              }
            : { build: null }),
        }),
      );

      const refactoredNetwork = data.networks.app_network.reduce(
        (acc: INetworkConfig, network) => {
          if (!data.networks.custom) {
            if ('driver' in network) {
              acc[network.network_name] = {
                driver: network.driver?.value,
              };
            }
          }
          if ('name' in network && 'external' in network) {
            acc[network.network_name] = {
              name: network.name,
              external: !!network.external,
            };
          }
          return acc;
        },
        {},
      );

      const services = refactoredService.map((item) => {
        if (item.ports?.some((port) => !port.value)) {
          item.ports = null;
        }
        if (item.volumes?.some((volume) => !volume.value)) {
          item.volumes = null;
        }
        if (item.networks?.some((network) => !network.value)) {
          item.networks = null;
        }
        if (item.depends_on?.some((depend_on) => !depend_on.value)) {
          item.depends_on = null;
        }
        if (
          item.environment &&
          !Object.entries(item.environment).some(
            ([k, v]) => k !== '' || v !== '',
          )
        ) {
          item.environment = null;
        }
        if (
          item.build?.args &&
          !Object.entries(item.build?.args).some(
            ([k, v]) => k !== '' || v !== '',
          )
        ) {
          item.build.args = null;
        }
        return item;
      });

      const requestBody: DockerComposeBody = {
        version: data.version,
        services: convertServicesToObject(services),
        networks: refactoredNetwork,
      };

      await dockerComposeMutate(requestBody);
      await download();
    } catch (error) {
      console.log(error);
      if (isAxiosError<DockerComposeValidationError>(error)) {
        toast.error(
          `${error.response?.data.detail[0].loc[error.response?.data.detail[0].loc.length - 1]} ${error.response?.data.detail[0].msg}`,
        );
      } else {
        console.log(error);
        toast.error('Something went wrong');
      }
    }
  };

  return (
    <div className="flex h-[calc(100%-56px)] w-full justify-center overflow-y-auto p-4 text-black-1 scrollbar-thin dark:text-white">
      <div className="h-full w-full max-w-[768px]">
        <FormWrapper methods={methods} onSubmit={handleSubmit}>
          <div className="flex flex-col w-full mb-4">
            <FormInput label="Version" name="version" placeholder="3" />
          </div>
          <div className="flex flex-col w-full mb-4">
            <NetworkFields />
          </div>

          <div className="flex items-center mb-4">
            <h1 className="text-2xl font-bold">Services</h1>
            <button
              type="button"
              onClick={handleAddService}
              className="ml-4 btn btn-xs"
            >
              Add <Plus className="size-3" />
            </button>
          </div>

          <div className="space-y-4">
            {services.map((service, index) => (
              <div
                key={service.id}
                className="w-full p-5 border border-gray-500 rounded-md"
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
                    'h-full max-h-0 overflow-y-auto px-1 transition-all duration-500',
                    {
                      'max-h-[1000px]': openService === index,
                    },
                  )}
                >
                  <div className="flex flex-col mb-4">
                    <FormInput
                      id="service_name"
                      name={`services.${index}.name`}
                      label="Name"
                      placeholder="service name"
                    />
                  </div>
                  <div className="flex flex-col mb-4">
                    <FormInput
                      id="image"
                      name={`services.${index}.image`}
                      label="Image"
                      placeholder="image"
                    />
                  </div>
                  <div className="flex flex-col mb-4">
                    <FormInput
                      id="container_name"
                      name={`services.${index}.container_name`}
                      label="Container Name"
                      placeholder="container_name"
                    />
                  </div>
                  <div className="flex flex-col mb-4">
                    <FormInput
                      id="command"
                      name={`services.${index}.command`}
                      label="Command"
                      placeholder="command..."
                    />
                  </div>
                  <ServiceBuildFields serviceIndex={index} />
                  <ServicePortsFields serviceIndex={index} />
                  <ServiceVolumesFields serviceIndex={index} />
                  <ServiceNetworkFields serviceIndex={index} />
                  <ServiceDependsOnFields serviceIndex={index} />
                  <ServiceEnvironmentFields serviceIndex={index} />
                </div>
              </div>
            ))}
          </div>
          <button
            type="submit"
            disabled={dockerComposePending}
            className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
          >
            {dockerComposePending
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

export default DockerCompose;
