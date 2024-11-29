import { usePost } from '@/core/react-query';
import { API } from '@/enums/api.enums';
import { FC, FormEvent, useState } from 'react';
import {
  InstallationBody,
  InstallationResponse,
  InstallationValidationError,
} from './installation.types';
import { toast } from 'sonner';
import { isAxiosError } from 'axios';

const Installation: FC = () => {
  const { mutateAsync, isPending } = usePost<
    InstallationResponse,
    InstallationBody
  >(API.Installation, 'installation');

  const [os, setOs] = useState('');
  const [tool, setTool] = useState('');

  const handleInstall = async (e: FormEvent) => {
    e.preventDefault();

    try {
      const installationBody: InstallationBody = {
        os,
        service: tool,
      };

      const {
        data: { output },
      } = await mutateAsync(installationBody);

      const blob = new Blob([output], { type: 'text/plain' });

      const url = URL.createObjectURL(blob);

      const link = document.createElement('a');
      link.href = url;
      link.download = 'installation.sh';
      document.body.appendChild(link);
      link.click();

      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    } catch (error) {
      if (isAxiosError<InstallationValidationError>(error)) {
        toast.error(error.response?.data.detail[0].msg);
      } else {
        toast.error('Something went wrong');
      }
    }
  };

  return (
    <form
      onSubmit={handleInstall}
      className="flex h-full w-full items-center justify-center"
    >
      <div className="w-full max-w-96">
        <div className="divide-y divide-gray-500 rounded-md border border-gray-500">
          <input
            value={os}
            onChange={(e) => setOs(e.target.value)}
            placeholder="os (example: ubuntu)"
            className="block w-full rounded-t-md p-2 outline-none"
          />
          <input
            value={tool}
            onChange={(e) => setTool(e.target.value)}
            placeholder="tool (example: nginx)"
            className="block w-full rounded-b-md p-2 outline-none"
          />
        </div>
        <button
          type="submit"
          disabled={isPending}
          className="btn mt-3 w-full bg-orange-base text-white hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
        >
          {isPending ? 'Wait...' : 'Install'}
        </button>
      </div>
    </form>
  );
};

export default Installation;
