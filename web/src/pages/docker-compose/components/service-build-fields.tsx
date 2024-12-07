import { FC } from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { useFieldArray, useFormContext } from 'react-hook-form';
import { FormInput } from '@/components/form/form-input';
import { FormCheckbox } from '@/components/form/form-checkbox';
import { cn } from '@/lib/utils';

type ServiceBuildFieldsProps = {
  serviceIndex: number;
};

export const ServiceBuildFields: FC<ServiceBuildFieldsProps> = ({
  serviceIndex,
}) => {
  const { control, watch } = useFormContext();
  const buildEnabled = watch(`services.${serviceIndex}.build.enabled`);

  const { fields, append, remove } = useFieldArray({
    control,
    name: `services.${serviceIndex}.build.args`,
  });

  return (
    <div className="mt-6 mb-2">
      <div className="flex items-center justify-between mb-4">
        <p className="text-base font-bold">Build Configuration</p>
        <FormCheckbox
          name={`services.${serviceIndex}.build.enabled`}
          label="Enable Build"
        />
      </div>

      {buildEnabled && (
        <div className="p-4 space-y-4 border border-gray-200 rounded-md dark:border-gray-500">
          <div className="flex gap-2 [&>div]:flex-1">
            <FormInput
              name={`services.${serviceIndex}.build.context`}
              label="Context"
              placeholder="."
            />
            <FormInput
              name={`services.${serviceIndex}.build.dockerfile`}
              label="Dockerfile"
              placeholder="Dockerfile"
            />
          </div>

          <div className="space-y-2">
            <div className="flex items-center">
              <p className="text-sm font-semibold">Build Arguments</p>
              <button
                type="button"
                onClick={() => append({ key: '', value: '' })}
                className="ml-4 btn btn-xs"
              >
                Add <Plus className="size-3" />
              </button>
            </div>

            <div className="grid grid-cols-2 gap-4">
              {fields.map((field, idx) => (
                <div
                  className={cn(
                    'relative mb-4 flex items-center divide-x-2 divide-gray-200 rounded-md border border-gray-200 dark:divide-gray-500 dark:border-gray-500 [&>div]:mb-0',
                    {
                      'divide-red-500 border-red-500 dark:divide-red-500 dark:border-red-500':
                        control.getFieldState(
                          `services.${serviceIndex}.build.args.${idx}.key`,
                        ).invalid ||
                        control.getFieldState(
                          `services.${serviceIndex}.build.args.${idx}.value`,
                        ).invalid,
                    },
                  )}
                  key={field.id}
                >
                  <FormInput
                    id={`env_name_${idx}`}
                    name={`services.${serviceIndex}.build.args.${idx}.key`}
                    label=""
                    placeholder="Key"
                    inputClass={'border-none'}
                  />
                  <FormInput
                    id={`env_value_${idx}`}
                    name={`services.${serviceIndex}.build.args.${idx}.value`}
                    label=""
                    placeholder="Value"
                    inputClass={cn('border-none rounded-s-none', {
                      'rounded-e-md': idx === 0,
                    })}
                  />

                  {idx > 0 && (
                    <button
                      type="button"
                      onClick={() => remove(idx)}
                      className="z-10 h-full px-4"
                    >
                      <Trash2 className="size-4" />
                    </button>
                  )}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
