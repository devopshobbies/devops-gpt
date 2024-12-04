import { FC } from 'react';
import {
  dockerAnsibleSchema,
  type DockerAnsible,
  type DockerAnsibleBody,
  type DockerAnsibleResponse,
  type dockerTemplateValidationError,
} from './docker.types';
import { AnsibleTemplateAPI } from '@/enums/api.enums';
import { useDownload } from '@/hooks';
import { usePost } from '@/core/react-query';
import { isAxiosError } from 'axios';
import { toast } from 'sonner';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { FormWrapper } from '@/components/form/form-wrapper';
import { FormInput } from '@/components/form/form-input';
import HostsField from './components/hosts-fields';
import { FormSelect } from '@/components/form/form-select';
import { OSOptions, versionOptions } from './data/select-options';

const DockerAnsible: FC = () => {
  const defaultValues = {
    ansible_user: '',
    os: { label: 'Ubuntu', value: 'ubuntu' },
    hosts: [{ value: '' }],
    version: {
      label: 'Latest',
      value: 'latest',
    },
  };

  const methods = useForm<DockerAnsible>({
    resolver: zodResolver(dockerAnsibleSchema),
    defaultValues,
  });

  const { mutateAsync: dockerAnsibleMutate, isPending: dockerAnsiblePending } =
    usePost<DockerAnsibleResponse, DockerAnsibleBody>(
      AnsibleTemplateAPI.Docker,
      'ansible-docker',
    );

  const { download, isPending: downloadPending } = useDownload({
    downloadFileName: 'DockerAnsible',
    source: 'docker',
    folderName: 'MyAnsible',
  });

  const handleSubmit = async (data: DockerAnsible) => {
    try {
      const body = {
        ...data,
        hosts: data.hosts.map((host) => host.value),
        os: data.os.value,
        version: data.version.value,
      };

      await dockerAnsibleMutate(body);
      await download();
    } catch (error) {
      console.log(error);
      if (isAxiosError<dockerTemplateValidationError>(error)) {
        toast.error(
          `${error.response?.data.detail[0].loc[error.response?.data.detail[0].loc.length - 1]} ${error.response?.data.detail[0].msg}`,
        );
      } else {
        toast.error('Something went wrong');
      }
    }
  };

  return (
    <div className="w-full max-w-96 text-black dark:text-white">
      <FormWrapper methods={methods} onSubmit={handleSubmit}>
        <div className="mb-4">
          <FormInput
            id="ansible_user"
            name={`ansible_user`}
            label="User"
            placeholder="root"
          />
        </div>
        <div className="mb-4">
          <FormInput
            id="ansible_port"
            name={`ansible_port`}
            label="Port"
            placeholder="22"
            inputType={'number'}
            isNumber={true}
          />
        </div>
        <div className="mb-4">
          <FormSelect
            name={`os`}
            label="OS"
            placeholder="Select..."
            options={OSOptions}
          />
        </div>
        <div className="mb-4">
          <HostsField />
        </div>
        <div className="mb-4">
          <FormSelect
            name={`version`}
            label="Version"
            placeholder="Select..."
            options={versionOptions}
          />
        </div>
        <button
          type="submit"
          disabled={dockerAnsiblePending}
          className="btn mt-3 w-full bg-orange-base text-white hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
        >
          {dockerAnsiblePending
            ? 'Generating...'
            : downloadPending
              ? 'Downloading...'
              : 'Generate'}
        </button>
      </FormWrapper>
    </div>
  );
};

export default DockerAnsible;
