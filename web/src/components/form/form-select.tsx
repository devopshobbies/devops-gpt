// components/form/FormSelect.tsx
import * as Form from '@radix-ui/react-form';
import { Controller, useFormContext } from 'react-hook-form';
import { FormFieldProps } from '../../types/form.types';
import Select from 'react-select';
import { getNestedValue } from '@/lib/helper';
import { useStyle } from '@/hooks';
import { cn } from '@/lib/utils';
import { selectStyle } from '@/styles/select.styles';

interface OptionType {
  value: string;
  label: string;
}

interface FormSelectProps extends FormFieldProps {
  options: OptionType[];
  placeholder?: string;
  isSearchable?: boolean;
}

export const FormSelect = ({
  name,
  label,
  error,
  options,
  placeholder = 'Select...',
  isSearchable = true,
  ...props
}: FormSelectProps) => {
  const {
    control,
    formState: { errors },
  } = useFormContext();

  const { darkMode } = useStyle();

  const fieldError = getNestedValue(errors, name);
  const errorMessage = fieldError?.message as string;

  return (
    <Form.Field
      className={cn('form-field relative', {
        'mb-6': errorMessage,
      })}
      name={name}
    >
      {label && (
        <div className="mb-1 flex items-baseline justify-between">
          <Form.Label className="form-label">{label}</Form.Label>
        </div>
      )}
      <Form.Control asChild>
        <Controller
          name={name}
          control={control}
          render={({ field }) => (
            <Select
              {...field}
              options={options}
              placeholder={placeholder}
              className="w-full"
              {...props}
              styles={selectStyle(darkMode, !!errorMessage)}
            />
          )}
        />
      </Form.Control>
      {errorMessage && (
        <div className="absolute left-0 top-full">
          <Form.Message className="form-message ml-auto text-sm text-red-500">
            {errorMessage}
          </Form.Message>
        </div>
      )}
    </Form.Field>
  );
};
