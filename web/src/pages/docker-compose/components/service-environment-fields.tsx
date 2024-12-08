import { useFieldArray, useFormContext } from 'react-hook-form';
import { Plus, Trash2 } from 'lucide-react';
import { FormInput } from '@/components/form/form-input';
import { cn } from '@/lib/utils';
import { FC } from 'react';

type ServiceEnvironmentFieldsProps = {
  serviceIndex: number;
};

const ServiceEnvironmentFields: FC<ServiceEnvironmentFieldsProps> = ({
  serviceIndex,
}) => {
  const { control } = useFormContext();
  const { fields, append, remove } = useFieldArray({
    control,
    name: `services.${serviceIndex}.environment`,
  });

  return (
    <div className="mt-6 mb-2">
      <div className="flex items-center mb-2">
        <p className="text-base font-bold">Environments</p>

        <button
          type="button"
          onClick={() => append({ name: '', value: '' })}
          className="ml-4 btn btn-xs"
        >
          Add <Plus className="size-3" />
        </button>
      </div>
      <div className="grid grid-cols-2 gap-4">
        {fields.map((field, envIdx) => (
          <div
            className={cn(
              'relative mb-4 flex items-center divide-x-2 divide-gray-200 rounded-md border border-gray-200 dark:divide-gray-500 dark:border-gray-500 [&>div]:mb-0',
              {
                'divide-red-500 border-red-500 dark:divide-red-500 dark:border-red-500':
                  control.getFieldState(
                    `services.${serviceIndex}.environment.${envIdx}.name`,
                  ).invalid,
              },
            )}
            key={field.id}
          >
            <FormInput
              id={`env_name_${envIdx}`}
              name={`services.${serviceIndex}.environment.${envIdx}.key`}
              label=""
              placeholder="Env"
              inputClass={'border-none'}
            />
            <FormInput
              id={`env_value_${envIdx}`}
              name={`services.${serviceIndex}.environment.${envIdx}.value`}
              label=""
              placeholder="Hi"
              inputClass={cn('border-none rounded-s-none', {
                'rounded-e-md': envIdx === 0,
              })}
            />

            {envIdx > 0 && (
              <button
                type="button"
                onClick={() => remove(envIdx)}
                className="z-10 h-full px-4"
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

export default ServiceEnvironmentFields;
