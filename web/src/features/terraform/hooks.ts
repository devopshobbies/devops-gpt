import { useState } from "react";
import { FieldValues, useForm, UseFormProps } from "react-hook-form";
import { Endpoints } from "../constants";
import { useMutation, UseMutationOptions } from "@tanstack/react-query";
import apiClient from "../../utils/apiClient";
import useGptStore from "../../utils/store";

const useTerraFormHandler = <T extends FieldValues, K>(
  initialValues: UseFormProps<T>["defaultValues"],
  endpoint: Endpoints
) => {
  const [request, setRequest] = useState<K>();
  const setGeneratorQuery = useGptStore((s) => s.setGeneratorQuery);
  const formMethods = useForm<T>({ defaultValues: initialValues });
  const { handleSubmit } = formMethods;

  const useTerraMutation = (options?: UseMutationOptions) =>
    useMutation({
      mutationFn: () => apiClient.post(endpoint, request),
      onSuccess: () => setGeneratorQuery(true, endpoint),
      onError: () => setGeneratorQuery(false, endpoint),
      ...options,
    });

  const { mutate, isSuccess, isError, status, data } = useTerraMutation();

  const onSubmit = (data: K) => {
    setRequest(data);
    mutate();
    formMethods.reset();
  };

  return {
    formMethods,
    handleSubmit,
    onSubmit,
    isSuccess,
    isError,
    status,
    data,
  };
};

export default useTerraFormHandler;
