import { useState } from "react";
import { FieldValues, useForm, UseFormProps } from "react-hook-form";
import { v4 as uuid } from "uuid";
import { UserType } from "../features/constants";
import useGptStore from "../utils/store";

const useFormHandler = <T extends FieldValues, K>(
  initialValues: UseFormProps<T>["defaultValues"]
) => {
  const [request, setRequest] = useState<K & { requestId: string }>();
  const formMethods = useForm<T>({ defaultValues: initialValues });
  const addMessage = useGptStore((s) => s.addMessage);
  const { handleSubmit } = formMethods;

  const onSubmit = (data: K, content: string) => {
    addMessage(UserType.USER, content, uuid());
    formMethods.reset();
    setRequest({ ...data, requestId: uuid() });
  };

  return { formMethods, request, handleSubmit, onSubmit };
};

export default useFormHandler;
