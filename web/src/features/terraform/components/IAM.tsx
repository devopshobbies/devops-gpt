import { Button, HStack } from "@chakra-ui/react";
import { FormProvider } from "react-hook-form";
import CheckBox from "../../../components/internal-ui/CheckBox";
import {
  Endpoints,
  terraformIamDefaultValues,
  TerraformIAMFields,
} from "../../constants";
import { ApiRequestTerraformIam, TerraformIAMFormData } from "../../model";

import { terraformIAMMapper } from "../../../utils/mapperFunctions";
import useTerraFormHandler from "../hooks";

const IAM = () => {
  const { formMethods, handleSubmit, onSubmit, isSuccess, isError } =
    useTerraFormHandler<TerraformIAMFormData, ApiRequestTerraformIam>(
      terraformIamDefaultValues,
      Endpoints.POST_IAC_T_IAM
    );

  const handleFormSubmit = handleSubmit((data) =>
    onSubmit(terraformIAMMapper(data))
  );

  return (
    <div className="flex flex-col ">
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <div className="flex justify-between w-full border md:flex-col md:items-center md:gap-y-5 border-orange-300 p-8">
            <HStack gap={5}>
              <p className="font-bold">IAM service: </p>
              <CheckBox
                fieldName={TerraformIAMFields.IAM_USER}
                label="IAM user?"
              />
              <CheckBox
                fieldName={TerraformIAMFields.IAM_GROUP}
                label="IAM group"
              />
            </HStack>
            <Button type="submit" bg="orange.700" w="8rem" h="3rem">
              Generate
            </Button>
          </div>
        </form>
      </FormProvider>
      {isSuccess && <p className="text-green-600">Generated Succesfully</p>}
      {isError && <p className="text-red-700">Operation failed</p>}
    </div>
  );
};

export default IAM;
