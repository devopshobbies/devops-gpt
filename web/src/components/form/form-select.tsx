// components/form/FormSelect.tsx
import * as Form from '@radix-ui/react-form';
import { Controller, useFormContext } from 'react-hook-form';
import { FormFieldProps } from '../../types/form.types';
import Select from 'react-select';

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

  const fieldError = errors[name];
  const errorMessage = fieldError?.message as string;

  return (
    <Form.Field className="form-field" name={name}>
      {label && (
        <div className="mb-2 flex items-baseline justify-between">
          <Form.Label className="form-label">{label} :</Form.Label>
          {errorMessage && (
            <Form.Message className="form-message text-red-500">
              {errorMessage}
            </Form.Message>
          )}
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
            />
          )}
        />
      </Form.Control>
    </Form.Field>
  );
};
