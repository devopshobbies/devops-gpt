import { FC } from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { useFieldArray, useFormContext } from 'react-hook-form';
import { FormInput } from '@/components/form/form-input';
import { cn } from '@/lib/utils';

type ServicePortsFieldsProps = {
  serviceIndex: number;
};

const ServicePortsFields: FC<ServicePortsFieldsProps> = ({ serviceIndex }) => {
  const { control } = useFormContext();

  const { fields, append, remove } = useFieldArray({
    control,
    name: `services.${serviceIndex}.ports`,
  });

  return (
    <div className="mb-2 mt-6">
      <div className="mb-2 flex items-center">
        <p className="text-base font-bold">Ports</p>

        <button
          type="button"
          onClick={() => append('')}
          className="btn btn-xs ml-4"
        >
          Add <Plus className="size-3" />
        </button>
      </div>
      <div className="flex space-x-4">
        {fields.map((field, idx) => (
          <div
            className={cn(
              'flex items-center divide-x divide-gray-200 rounded-md border border-gray-200 dark:divide-gray-500 dark:border-gray-500',
              {
                'divide-red-500 border-red-500 dark:divide-red-500 dark:border-red-500':
                  control.getFieldState(`services.${serviceIndex}.ports.${idx}`)
                    .invalid,
              },
            )}
            key={field.id}
          >
            <FormInput
              name={`services.${serviceIndex}.ports.${idx}`}
              label=""
              placeholder="8080:80"
              className="h-12 w-full rounded-s-md px-2 outline-none"
            />

            <button
              type="button"
              onClick={() => remove(idx)}
              className="btn btn-error rounded-e-md rounded-s-none"
            >
              <Trash2 />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ServicePortsFields;
