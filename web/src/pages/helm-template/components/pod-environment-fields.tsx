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
                    `pods.${podIndex}.environment.${envIdx}.name`,
                  ).invalid ||
                  control.getFieldState(
                    `pods.${podIndex}.environment.${envIdx}.value`,
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
              inputClass={'border-none'}
            />
            <FormInput
              id={`env_value_${envIdx}`}
              name={`pods.${podIndex}.environment.${envIdx}.value`}
              label=""
              placeholder="Hi"
              inputClass={'border-none'}
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

export default PodEnvironmentFields;
