import * as Form from '@radix-ui/react-form';
import { FormProvider, UseFormReturn } from 'react-hook-form';
import { z } from 'zod';
import { FormConfig } from '../../types/form.types';

interface FormWrapperProps<T extends z.ZodType>
  extends Omit<FormConfig<T>, 'mode'> {
  children: React.ReactNode;
  onSubmit: (data: z.infer<T>) => void;
  methods: UseFormReturn<z.infer<T>>;
}

export const FormWrapper = <T extends z.ZodType>({
  children,
  onSubmit,
  methods,
}: FormWrapperProps<T>) => {
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
