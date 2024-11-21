import { Button, HStack } from "@chakra-ui/react";
import { DefaultValues, FormProvider } from "react-hook-form";
import useGenerator from "../../hooks/useGenerator";
import CheckBox, { Checkboxprops } from "./CheckBox";
import { Endpoints } from "../../features/constants";

interface PlatformProps<FormData, RequestData> {
  serviceName: string;
  defaultValues: DefaultValues<FormData>;
  endpoint: Endpoints;
  fieldProperties: Checkboxprops[];
  mapperFunction: (data: FormData) => RequestData;
}

const PlatformBox = <FormData extends {}, RequestData extends {}>({
  serviceName,
  defaultValues,
  endpoint,
  fieldProperties,
  mapperFunction,
}: PlatformProps<FormData, RequestData>) => {
  const {
    formMethods,
    handleSubmit,
    onSubmit,
    isError,
    status,
    data,
    isSuccess,
  } = useGenerator<FormData, RequestData>(defaultValues, endpoint);
  const handleFormSubmit = handleSubmit((formData) =>
    onSubmit(mapperFunction(formData))
  );

  return (
    <div className="flex flex-col ">
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <div className="flex flex-col justify-between w-full border items-center gap-y-5 border-orange-300 p-8">
            <HStack lg={{ gap: 5 }} md={{ gap: 3 }}>
              <p className="font-bold">{serviceName}: </p>
              {fieldProperties.map((field) => (
                <CheckBox
                  key={field.fieldName}
                  fieldName={field.fieldName}
                  label={field.label}
                />
              ))}
            </HStack>
            <Button
              type="submit"
              disabled={status === "pending" && !data}
              bg="orange.600"
              color="gray.100"
              w="8rem"
              h="3rem"
            >
              {status === "pending" ? (
                <span className="loading loading-ring loading-lg "></span>
              ) : (
                <p>Generate</p>
              )}
            </Button>
          </div>
        </form>
      </FormProvider>
      {isSuccess && <p className="text-green-500">Generated Successfully</p>}
      {isError && <p className="text-red-600">Operation failed</p>}
    </div>
  );
};

export default PlatformBox;
