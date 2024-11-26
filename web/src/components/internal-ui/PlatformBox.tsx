import { Button, HStack } from "@chakra-ui/react";
import { DefaultValues, FormProvider } from "react-hook-form";
import useTerraFormHandler from "../../features/terraform/hooks";
import CheckBox, { Checkboxprops } from "./CheckBox";
import { Endpoints } from "../../features/constants";

interface PlatformProps<FormData, RequestData> {
  serviceName: string;
  defaultValues: DefaultValues<FormData>;
  endpoint: Endpoints;
  fieldProperties: Checkboxprops[];
  mapperFunction: (data: FormData) => RequestData;
}

const PlatformBox = <FormData extends object, RequestData extends object>({
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
  } = useTerraFormHandler<FormData, RequestData>(defaultValues, endpoint);
  const handleFormSubmit = handleSubmit((formData) =>
    onSubmit(mapperFunction(formData))
  );

  return (
    <div className="flex flex-col ">
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <div className="flex flex-col items-center justify-between w-full p-8 border border-orange-300 gap-y-5">
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
