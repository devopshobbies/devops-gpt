
import * as Form from '@radix-ui/react-form';
import { useFormContext } from 'react-hook-form';
import { FormFieldProps } from '../../types/form.types';
import { cn } from '@/lib/utils';

interface FormCheckboxProps extends FormFieldProps {
  labelPosition?: 'left' | 'right';
  checkboxClassName?: string;
}

export const FormCheckbox = ({
  name,
  label,
  error,
  labelPosition = 'right',
  checkboxClassName,
  ...props
}: FormCheckboxProps) => {
  const {
    register,
    formState: { errors },
  } = useFormContext();

  const fieldError = errors[name];
  const errorMessage = fieldError?.message as string;

  return (
    <Form.Field className="form-field" name={name}>
      <div className={cn(
        'flex items-center gap-2',
        labelPosition === 'right' ? 'flex-row' : 'flex-row-reverse justify-end'
      )}>
        <Form.Control asChild>
          <input
            type="checkbox"
            className={cn(
              'toggle border-gray-500 bg-gray-500',
              'checked:bg-orange-base checked:hover:bg-orange-base/70',
              checkboxClassName
            )}
            {...register(name)}
            {...props}
          />
        </Form.Control>
        <Form.Label className="form-label cursor-pointer">{label}</Form.Label>
      </div>
      {errorMessage && (
        <Form.Message className="form-message mt-1 text-red-500">
          {errorMessage}
        </Form.Message>
      )}
    </Form.Field>
  );
};