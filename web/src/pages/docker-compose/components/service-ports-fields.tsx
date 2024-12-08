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
      <div className="grid grid-cols-4 gap-4">
        {fields.map((field, idx) => (
          <div className={'relative'} key={field.id}>
            <FormInput
              label=""
              name={`services.${serviceIndex}.ports.${idx}.value`}
              placeholder="8080:80"
              inputClass={cn({
                'pr-8': idx > 0,
                'divide-red-500 border-red-500 dark:divide-red-500 dark:border-red-500':
                  control.getFieldState(`services.${serviceIndex}.ports.${idx}`)
                    .invalid,
              })}
            />
            {idx > 0 && (
              <button
                type="button"
                onClick={() => remove(idx)}
                className="absolute right-3 top-0 z-10 h-full rounded-e-md rounded-s-none"
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

export default ServicePortsFields;
