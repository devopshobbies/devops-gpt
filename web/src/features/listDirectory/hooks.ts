import { useMutation, UseMutationOptions } from "@tanstack/react-query";
import apiClient from "../../utils/apiClient";
import { FieldValues, useForm, UseFormProps } from "react-hook-form";
import { useState } from "react";

export const useDirectoryDownloader = <
  TFormData extends FieldValues,
  TResponse
>(
  defaultValues: UseFormProps<TFormData>["defaultValues"],
  endpointResolver: (formData: TFormData) => string,
  apiEndpoint: (resolvedEndpoint: string) => string
) => {
  const formMethods = useForm<TFormData>({ defaultValues });
  const [endpoint, setEndpoint] = useState("");
  const [data, setData] = useState<TResponse>();

  const { handleSubmit } = formMethods;

  const useGenericMutation = (options?: UseMutationOptions) =>
    useMutation({
      mutationFn: () =>
        apiClient
          .get<TResponse>(apiEndpoint(endpoint))
          .then((res) => setData(res.data)),
      ...options,
    });

  const { mutate, isSuccess, error } = useGenericMutation();

  const onSubmit = (formData: TFormData) => {
    const resolvedEndpoint = endpointResolver(formData);
    setEndpoint(resolvedEndpoint);
    mutate();
  };

  return {
    formMethods,
    handleSubmit,
    onSubmit,
    error,
    isSuccess,
    data,
  };
};
