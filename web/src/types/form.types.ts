// types/form.types.ts
import { z } from 'zod';
import { ComponentPropsWithoutRef } from 'react';
import * as Form from '@radix-ui/react-form';

export type FormFieldProps = {
  name: string;
  label: string;
  error?: string;
  placeholder?: string;
  isNumber?: boolean;
  inputType?: typeof HTMLInputElement.prototype.type;
  inputClass?: string;
  showError?: boolean;
} & ComponentPropsWithoutRef<typeof Form.Field>;

export type FormConfig<T extends z.ZodType> = {
  defaultValues?: z.infer<T>;
  schema?: T;
  mode?: 'onSubmit' | 'onChange' | 'onBlur';
};
