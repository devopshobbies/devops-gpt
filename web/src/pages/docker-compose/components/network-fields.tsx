import { FC } from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { useFieldArray, useFormContext } from 'react-hook-form';
import { FormInput } from '@/components/form/form-input';
import { FormCheckbox } from '@/components/form/form-checkbox';
import { FormSelect } from '@/components/form/form-select';

const defaultNetworkDrivers = ['Bridge', 'Host', 'None', 'Overlay'] as const;

const NetworkFields: FC = () => {
  const { control, watch } = useFormContext();

  const { fields, append, remove } = useFieldArray({
    control,
    name: 'networks.app_network',
  });

  const customNetwork = watch('networks.external_network');

  const handleRemoveNetwork = (index: number) => {
    remove(index);
  };

  const handleAppendNetwork = () => {
    const networkData = customNetwork
      ? {
          network_name: '',
          name: '',
        }
      : {
          network_name: '',
          driver: {
            label: 'Bridge',
            value: 'bridge',
          },
        };

    append(networkData);
  };

  return (
    <div>
      <div className="mb-4 flex items-center justify-between">
        <div className="flex items-center">
          <p className="text-2xl font-bold">Networks</p>
          <button
            type="button"
            onClick={handleAppendNetwork}
            className="btn btn-xs ml-4"
          >
            Add <Plus className="size-3" />
          </button>
        </div>
        <FormCheckbox
          label="External Network"
          name="networks.external_network"
        />
      </div>

      <div className="space-y-4">
        <div className="flex w-full flex-col gap-4 rounded-md border border-gray-500 p-5">
          {fields.map((field, index) => (
            <div key={field.id} className="mb-4">
              <div className="mb-4 flex items-center justify-between">
                <p className="font-semibold">Network #{index + 1}</p>
                {index > 0 && (
                  <button
                    type="button"
                    onClick={() => handleRemoveNetwork(index)}
                  >
                    <Trash2 className="size-4" color="red" />
                  </button>
                )}
              </div>

              <div>
                <div className="flex items-center gap-3 [&>div]:flex-1">
                  <FormInput
                    name={`networks.app_network.${index}.network_name`}
                    label="App Network"
                    placeholder="network_name"
                    showError={false}
                  />
                  {!customNetwork && (
                    <FormSelect
                      name={`networks.app_network.${index}.driver`}
                      label="Network Driver"
                      options={defaultNetworkDrivers.map((driver) => ({
                        label: driver,
                        value: driver,
                      }))}
                    />
                  )}
                  {customNetwork && (
                    <FormInput
                      name={`networks.app_network.${index}.name`}
                      label="Name"
                      placeholder="Name"
                      showError={false}
                    />
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default NetworkFields;
