import { Button, HStack } from "@chakra-ui/react";
import { FormProvider } from "react-hook-form";
import CheckBox from "../../../components/internal-ui/CheckBox";
import {
  Endpoints,
  terraformS3DefaultValues,
  TerraformS3Fields,
} from "../../constants";
import { ApiRequestTerraformS3, TerraformS3FormData } from "../../model";

import { terraformS3Mapper } from "../../../utils/mapperFunctions";
import useTerraFormHandler from "../hooks";

const S3 = () => {
  const { formMethods, handleSubmit, onSubmit, isSuccess, isError } =
    useTerraFormHandler<TerraformS3FormData, ApiRequestTerraformS3>(
      terraformS3DefaultValues,
      Endpoints.POST_IAC_T_S3
    );

  const handleFormSubmit = handleSubmit((data) =>
    onSubmit(terraformS3Mapper(data))
  );

  return (
    <div className="flex flex-col">
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <div className="flex justify-between w-full border border-orange-300 p-8">
            <HStack gap={5}>
              <p className="font-bold">S3 service: </p>
              <CheckBox
                fieldName={TerraformS3Fields.S3_BUCKET}
                label="S3 bucket?"
              />
              <CheckBox
                fieldName={TerraformS3Fields.BUCKET_VERSIONING}
                label="Bucket versioning"
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

export default S3;
