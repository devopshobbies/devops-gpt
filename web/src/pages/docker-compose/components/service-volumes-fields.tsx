import { FC } from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { useFieldArray, useFormContext } from 'react-hook-form';
import { FormInput } from '@/components/form/form-input';
import { cn } from '@/lib/utils';

type ServiceVolumesFieldsProps = {
  serviceIndex: number;
};

export const ServiceVolumesFields: FC<ServiceVolumesFieldsProps> = ({
  serviceIndex,
}) => {
  const { control } = useFormContext();

  const { fields, append, remove } = useFieldArray({
    control,
    name: `services.${serviceIndex}.volumes`,
  });

  return (
    <div className="mb-2 mt-6">
      <div className="mb-2 flex items-center">
        <p className="text-base font-bold">Volumes</p>

        <button
          type="button"
          onClick={() => append('')}
          className="btn btn-xs ml-4"
        >
          Add <Plus className="size-3" />
        </button>
      </div>
      <div className="flex space-y-4">
        {fields.map((field, idx) => (
          <div
            className={cn(
              'flex items-center divide-x divide-gray-200 rounded-md border border-gray-200 dark:divide-gray-500 dark:border-gray-500',
              {
                'divide-red-500 border-red-500 dark:divide-red-500 dark:border-red-500':
                  control.getFieldState(
                    `services.${serviceIndex}.volumes.${idx}`,
                  ).invalid,
              },
            )}
            key={field.id}
          >
            <FormInput
              name={`services.${serviceIndex}.volumes.${idx}`}
              label=""
              placeholder="./host/path:/container/path"
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
