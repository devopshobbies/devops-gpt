import { useState } from "react";
import { FieldValues, useForm, UseFormProps } from "react-hook-form";
import { Endpoints } from "../constants";
import { useMutation, UseMutationOptions } from "@tanstack/react-query";
import apiClient from "../../utils/apiClient";

const useTerraFormHandler = <T extends FieldValues, K>(
  initialValues: UseFormProps<T>["defaultValues"],
  endpoint: Endpoints
) => {
  const [request, setRequest] = useState<K>();
  const formMethods = useForm<T>({ defaultValues: initialValues });
  const { handleSubmit } = formMethods;

  const useTerraMutation = (options?: UseMutationOptions) =>
    useMutation({
      mutationFn: () => apiClient.post(endpoint, request),
      ...options,
    });

  const { mutate, isSuccess, isError } = useTerraMutation();

  const onSubmit = (data: K) => {
    setRequest({ ...data });
    mutate();
    formMethods.reset();
  };

  return { formMethods, handleSubmit, onSubmit, isSuccess, isError };
};

export default useTerraFormHandler;
