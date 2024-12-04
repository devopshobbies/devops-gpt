import { zodResolver } from '@hookform/resolvers/zod';
import { FC } from 'react';
import { useForm } from 'react-hook-form';
import {
  KuberAnsible,
  KuberAnsibleBody,
  KuberAnsibleResponse,
  kuberAnsibleSchema,
  kuberTemplateValidationError,
} from './kuber.types';
import { FormWrapper } from '@/components/form/form-wrapper';
import { FormInput } from '@/components/form/form-input';
import { FormSelect } from '@/components/form/form-select';
import { usePost } from '@/core/react-query';
import { AnsibleTemplateAPI } from '@/enums/api.enums';
import { OSOptions, versionOptions } from './data/select-options';
import { useDownload } from '@/hooks';
import { isAxiosError } from 'axios';
import { toast } from 'sonner';
import K8SMasterNodes from './components/k8s-master-nodes';
import K8SWorkerNodes from './components/k8s-worker-nodes';

const KubernetesAnsible: FC = () => {
  const { mutateAsync: kuberAnsibleMutate, isPending: kuberAnsiblePending } =
    usePost<KuberAnsibleResponse, KuberAnsibleBody>(
      AnsibleTemplateAPI.Kubernetes,
      'ansible-docker',
    );

  const { download, isPending: downloadPending } = useDownload({
    downloadFileName: 'KubernetesAnsible',
    source: 'kubernetes',
    folderName: 'MyAnsible',
  });

  const defaultValues = {
    ansible_user: '',
    os: { label: 'Ubuntu', value: 'ubuntu' },
    k8s_worker_nodes: [{ value: '' }],
    k8s_master_nodes: [{ value: '' }],
  };

  const methods = useForm<KuberAnsible>({
    resolver: zodResolver(kuberAnsibleSchema),
    defaultValues,
  });

  const handleSubmit = async (data: KuberAnsible) => {
    try {
      const body = {
        ...data,
        k8s_worker_nodes: data.k8s_worker_nodes.map((worker) => worker.value),
        k8s_master_nodes: data.k8s_master_nodes.map((master) => master.value),
        os: data.os.value,
        version: data.version.value,
      };

      await kuberAnsibleMutate(body);
      await download();
    } catch (error) {
      console.log(error);
      if (isAxiosError<kuberTemplateValidationError>(error)) {
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
          <K8SMasterNodes />
        </div>
        <div className="mb-4">
          <K8SWorkerNodes />
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
          disabled={kuberAnsiblePending}
          className="btn mt-3 w-full bg-orange-base text-white hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
        >
          {kuberAnsiblePending
            ? 'Generating...'
            : downloadPending
              ? 'Downloading...'
              : 'Generate'}
        </button>
      </FormWrapper>
    </div>
  );
};

export default KubernetesAnsible;
