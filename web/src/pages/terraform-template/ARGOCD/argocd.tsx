import { cn } from '@/lib/utils';
import { FC, FormEvent, useState } from 'react';
import { ChevronDown } from 'lucide-react';
import { TerraformTemplateAPI } from '@/enums/api.enums';
import { usePost } from '@/core/react-query';
import { ArgocdBody, ArgocdResponse } from './argocd.types';
import { toast } from 'sonner';
import { useDownload } from '@/hooks';

const Argocd: FC = () => {
  const { mutateAsync: argocdMutate, isPending: argocdPending } = usePost<
    ArgocdResponse,
    ArgocdBody
  >(TerraformTemplateAPI.Argocd, 'argocd');
  const { download, isPending: downloadPending } = useDownload({
    folderName: 'MyTerraform',
    source: 'argocd',
    downloadFileName: 'Argocd',
  });

  const [dropdown, setDropdown] = useState({
    argo_application: false,
    sync_policy: false,
  });
  const [services, setServices] = useState({
    auto_prune: false,
    self_heal: false,
    argocd_repository: false,
    application_depends_repository: false,
  });

  const handleDropdown = (dropdownItem: keyof typeof dropdown) => {
    setDropdown((prev) => ({
      ...prev,
      [dropdownItem]: !prev[dropdownItem],
    }));
  };

  const handleServices = (serviceItem: keyof typeof services) => {
    setServices((prev) => ({
      ...prev,
      [serviceItem]: !prev[serviceItem],
    }));
  };

  const handleForm = async (e: FormEvent) => {
    e.preventDefault();

    try {
      const argocdBody: ArgocdBody = {
        argocd_application: dropdown.argo_application
          ? {
              sync_policy: {
                auto_prune: services.auto_prune,
                self_heal: services.self_heal,
              },
            }
          : null,
        argocd_repository: services.argocd_repository,
        application_depends_repository: services.application_depends_repository,
      };

      await argocdMutate(argocdBody);
      await download();
    } catch (error) {
      console.log(error);
      toast.error('Something went wrong');
    }
  };

  return (
    <form onSubmit={handleForm} className="w-full max-w-96">
      <div className="rounded-md border border-gray-500">
        <div className="divide-y divide-gray-500">
          <div className="flex w-full items-center justify-between px-3 py-3">
            <p>Argo Application</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70':
                  dropdown.argo_application,
              })}
              onChange={() => handleDropdown('argo_application')}
            />
          </div>
          <div
            className={cn(
              'max-h-0 w-full divide-y divide-gray-500 overflow-hidden transition-all',
              {
                'max-h-96': dropdown.argo_application,
              },
            )}
          >
            <div
              className="flex cursor-pointer items-center justify-between py-3 pl-10 pr-3"
              onClick={() => handleDropdown('sync_policy')}
            >
              <p>Sync Policy</p>
              <ChevronDown
                className={cn('transition-all', {
                  'rotate-180': dropdown.sync_policy,
                })}
              />
            </div>
            <div
              className={cn(
                'max-h-0 w-full divide-y divide-gray-500 overflow-hidden transition-all',
                {
                  'max-h-96': dropdown.sync_policy,
                },
              )}
            >
              <div className="flex items-center justify-between py-3 pl-16 pr-3">
                <p>Auto Prune</p>
                <input
                  type="checkbox"
                  className={cn('toggle border-gray-500 bg-gray-500', {
                    'bg-orange-base hover:bg-orange-base/70':
                      services.auto_prune,
                  })}
                  onChange={() => handleServices('auto_prune')}
                />
              </div>
              <div className="flex items-center justify-between py-3 pl-16 pr-3">
                <p>Self Heal</p>
                <input
                  type="checkbox"
                  className={cn('toggle border-gray-500 bg-gray-500', {
                    'bg-orange-base hover:bg-orange-base/70':
                      services.self_heal,
                  })}
                  onChange={() => handleServices('self_heal')}
                />
              </div>
            </div>
          </div>
          <div className="flex w-full items-center justify-between px-3 py-3">
            <p>Argocd Repository</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70':
                  services.argocd_repository,
              })}
              onChange={() => handleServices('argocd_repository')}
            />
          </div>
          <div className="flex w-full items-center justify-between px-3 py-3">
            <p>Application Depends Repository</p>
            <input
              type="checkbox"
              className={cn('toggle border-gray-500 bg-gray-500', {
                'bg-orange-base hover:bg-orange-base/70':
                  services.application_depends_repository,
              })}
              onChange={() => handleServices('application_depends_repository')}
            />
          </div>
        </div>
      </div>
      <button
        type="submit"
        disabled={argocdPending || downloadPending}
        className="btn mt-3 w-full bg-orange-base text-white hover:bg-orange-base/70 disabled:bg-orange-base/50 disabled:text-white/70"
      >
        {argocdPending
          ? 'Generate Terraform...'
          : downloadPending
            ? 'Downloading Template...'
            : 'Generate Terraform'}
      </button>
    </form>
  );
};

export default Argocd;
