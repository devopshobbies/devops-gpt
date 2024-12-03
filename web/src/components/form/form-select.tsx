// components/form/FormSelect.tsx
import * as Form from '@radix-ui/react-form';
import { Controller, useFormContext } from 'react-hook-form';
import { FormFieldProps } from '../../types/form.types';
import Select from 'react-select';
import { getNestedValue } from '@/lib/helper';
import { selectStyle } from '@/pages/helm-template/styles/helm-template.style';
import { useStyle } from '@/hooks';

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
    <Form.Field className="form-field" name={name}>
      {label && (
        <div className="mb-2 flex items-baseline justify-between">
          <Form.Label className="form-label">{label} :</Form.Label>
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
              styles={selectStyle(darkMode)}
            />
          )}
        />
      </Form.Control>
      {errorMessage && (
        <Form.Message className="form-message mt-1 text-red-500">
          {errorMessage}
        </Form.Message>
      )}
    </Form.Field>
  );
};
