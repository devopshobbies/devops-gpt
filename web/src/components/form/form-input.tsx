import * as Form from '@radix-ui/react-form';
import { useFormContext } from 'react-hook-form';
import { FormFieldProps } from '../../types/form.types';
import { getNestedValue } from '@/lib/helper';

export const FormInput = ({ name, label, error, ...props }: FormFieldProps) => {
  const {
    register,
    formState: { errors },
  } = useFormContext();

  const fieldError = getNestedValue(errors, name);
  const errorMessage = fieldError?.message as string;

  return (
    <Form.Field className="form-field" name={name}>
      {label && (
        <div className="mb-2 flex items-baseline justify-between">
          <Form.Label className="form-label">{label} :</Form.Label>
          {errorMessage && (
            <Form.Message className="form-message text-sm text-red-500">
              {errorMessage}
            </Form.Message>
          )}
        </div>
      )}
      <Form.Control asChild>
        <input
          className="w-full rounded-md border border-gray-200 px-3 py-2 outline-none dark:border-none"
          {...register(name)}
          {...props}
        />
      </Form.Control>
    </Form.Field>
  );
};
