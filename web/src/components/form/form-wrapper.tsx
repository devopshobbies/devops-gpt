// components/form/FormWrapper.tsx
import * as Form from '@radix-ui/react-form';
import { FormProvider, useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { FormConfig } from '../../types/form.types';

interface FormWrapperProps<T extends z.ZodType> extends FormConfig<T> {
  children: React.ReactNode;
  onSubmit: (data: z.infer<T>) => void;
}

export const FormWrapper = <T extends z.ZodType>({
  children,
  onSubmit,
  schema,
  defaultValues,
  mode = 'onChange',
}: FormWrapperProps<T>) => {
  const methods = useForm({
    defaultValues,
    resolver: schema ? zodResolver(schema) : undefined,
    mode,
  });

  return (
    <FormProvider {...methods}>
      <Form.Root
        onSubmit={methods.handleSubmit(onSubmit)}
        className="text-black dark:text-white"
      >
        {children}
      </Form.Root>
    </FormProvider>
  );
};
