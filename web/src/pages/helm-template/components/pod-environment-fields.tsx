import { useFieldArray, useFormContext } from 'react-hook-form';
import { Plus, Trash2 } from 'lucide-react';
import { FormInput } from '@/components/form/form-input';
import { cn } from '@/lib/utils';
import { FC } from 'react';

type PodEnvironmentFieldsProps = {
  podIndex: number;
};

const PodEnvironmentFields: FC<PodEnvironmentFieldsProps> = ({ podIndex }) => {
  const { control } = useFormContext();
  const { fields, append, remove } = useFieldArray({
    control,
    name: `pods.${podIndex}.environment`,
  });

  return (
    <div className="mb-2 mt-6">
      <div className="mb-2 flex items-center">
        <p className="text-base font-bold">Environments</p>

        <button
          type="button"
          onClick={() => append({ name: '', value: '' })}
          className="btn btn-xs ml-4"
        >
          Add <Plus className="size-3" />
        </button>
      </div>
      <div className="grid grid-cols-2 gap-4">
        {fields.map((field, envIdx) => (
          <div
            className={cn(
              'mb-4 flex items-center divide-x divide-gray-200 rounded-md border border-gray-200 dark:divide-gray-500 dark:border-gray-500 [&>div]:mb-0',
              {
                'divide-red-500 border-red-500 dark:divide-red-500 dark:border-red-500':
                  control.getFieldState(
                    `pods.${podIndex}.environment.${envIdx}.name`,
                  ).invalid,
              },
            )}
            key={field.id}
          >
            <FormInput
              id={`env_name_${envIdx}`}
              name={`pods.${podIndex}.environment.${envIdx}.name`}
              label=""
              placeholder="Env"
              className="h-12 w-full rounded-s-md px-2 outline-none"
            />
            <FormInput
              id={`env_value_${envIdx}`}
              name={`pods.${podIndex}.environment.${envIdx}.value`}
              label=""
              placeholder="Hi"
              className={cn('h-12 w-full rounded-s-md px-2 outline-none', {
                'rounded-e-md': envIdx === 0,
              })}
            />
            {envIdx > 0 && (
              <button
                onClick={() => remove(envIdx)}
                className="btn btn-error rounded-e-md rounded-s-none"
              >
                <Trash2 />
              </button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default PodEnvironmentFields;
