import { Button, HStack } from "@chakra-ui/react";
import { FormProvider } from "react-hook-form";
import CheckBox from "../../../components/internal-ui/CheckBox";
import {
  Endpoints,
  terraformDockerDefaultValues,
  TerraformDockerFields,
} from "../../constants";
import {
  ApiRequestTerraformDocker,
  TerraformDockerFormData,
} from "../../model";

import useTerraFormHandler from "../hooks";
import { terraformDockerMapper } from "../../../utils/mapperFunctions";

const Docker = () => {
  const { formMethods, handleSubmit, onSubmit, isSuccess, isError } =
    useTerraFormHandler<TerraformDockerFormData, ApiRequestTerraformDocker>(
      terraformDockerDefaultValues,
      Endpoints.POST_IAC_T_DOCKER
    );

  const handleFormSubmit = handleSubmit((data) =>
    onSubmit(terraformDockerMapper(data))
  );

  return (
    <div className="flex flex-col ">
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <div className="flex justify-between w-full border border-orange-300 p-8">
            <HStack gap={5}>
              <p className="font-bold">Docker service: </p>
              <CheckBox
                fieldName={TerraformDockerFields.DOCKER_IMAGE}
                label="Docker image?"
              />
              <CheckBox
                fieldName={TerraformDockerFields.DOCKER_CONTAINER}
                label="Docker container?"
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

export default Docker;
