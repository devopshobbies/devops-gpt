import { FC } from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { useFieldArray, useFormContext } from 'react-hook-form';
import { FormInput } from '@/components/form/form-input';
import { cn } from '@/lib/utils';

type ServiceDependsOnFieldsProps = {
  serviceIndex: number;
};

const ServiceDependsOnFields: FC<ServiceDependsOnFieldsProps> = ({
  serviceIndex,
}) => {
  const { control } = useFormContext();

  const { fields, append, remove } = useFieldArray({
    control,
    name: `services.${serviceIndex}.depends_on`,
  });

  return (
    <div className="mb-2 mt-6">
      <div className="mb-2 flex items-center">
        <p className="text-base font-bold">Depends On</p>

        <button
          type="button"
          onClick={() => append('')}
          className="btn btn-xs ml-4"
        >
          Add <Plus className="size-3" />
        </button>
      </div>
      <div className="flex gap-4">
        {fields.map((field, depIdx) => (
          <div
            className={cn(
              'mb-4 flex items-center divide-x divide-gray-200 rounded-md border border-gray-200 dark:divide-gray-500 dark:border-gray-500 [&>div]:mb-0',
            )}
            key={field.id}
          >
            <FormInput
              id={`depends_on_${depIdx}`}
              name={`services.${serviceIndex}.depends_on.${depIdx}`}
              label=""
              placeholder="Service name"
              className="h-12 w-full rounded-s-md px-2 outline-none"
            />

            <button
              onClick={() => remove(depIdx)}
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

export default ServiceDependsOnFields;
