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
    <div className="mt-6 mb-2">
      <div className="flex items-center mb-2">
        <p className="text-base font-bold">Depends On</p>

        <button
          type="button"
          onClick={() => append('')}
          className="ml-4 btn btn-xs"
        >
          Add <Plus className="size-3" />
        </button>
      </div>
      <div className="grid grid-cols-3 gap-4">
        {fields.map((field, idx) => (
          <div className={'relative'} key={field.id}>
            <FormInput
              label=""
              name={`services.${serviceIndex}.depends_on.${idx}.value`}
              placeholder="Service name"
              inputClass={cn({
                'pr-8': idx > 0,
                'divide-red-500 border-red-500 dark:divide-red-500 dark:border-red-500':
                  control.getFieldState(
                    `services.${serviceIndex}.depends_on.${idx}`,
                  ).invalid,
              })}
            />
            {idx > 0 && (
              <button
                type="button"
                onClick={() => remove(idx)}
                className="absolute top-0 z-10 h-full right-3 rounded-e-md rounded-s-none"
              >
                <Trash2 className="size-4" />
              </button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default ServiceDependsOnFields;
