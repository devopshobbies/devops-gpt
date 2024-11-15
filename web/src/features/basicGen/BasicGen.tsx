import { FormProvider } from "react-hook-form";
import Input from "../../components/internal-ui/Input";
import { basicGenDefaultValues, BasicGenFields, ENDPOINTS } from "../constants";
import { Button, HStack, Stack } from "@chakra-ui/react";

import useGptStore from "../../utils/store";
import ChatBox from "../../components/internal-ui/ChatBox";

import { ApiRequestBasicGen, BasicGenFormData } from "../model";

import { IoSendOutline } from "react-icons/io5";

import useFormHandler from "../../hooks/useFormHandler";
import { basicGenMapper } from "../../utils/mapperFunctions";

const BasicGen = () => {
  const { formMethods, handleSubmit, onSubmit, request } = useFormHandler<
    BasicGenFormData,
    ApiRequestBasicGen
  >(basicGenDefaultValues);

  const handleFormSubmit = handleSubmit((data) => {
    onSubmit(basicGenMapper(data), data.input);
  });

  const messages = useGptStore((s) => s.messages);

  return (
    <div>
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <Stack gap="3" justifyContent="center" alignItems="center">
            <div className="flex gap-2">
              <Input fieldName={BasicGenFields.MIN_TOKEN} label="Min token" />
              <Input fieldName={BasicGenFields.MAX_TOKEN} label="Max token" />
              <Input fieldName={BasicGenFields.SERVICE} label="Service" />
            </div>
            <ChatBox
              endpoint={ENDPOINTS.postBasic}
              request={request}
              messageData={messages}
              id={request?.requestId ?? ""}
            />
            <HStack
              mt="3"
              alignItems="center"
              alignContent="center"
              justifyContent="center"
              bottom="5"
            >
              <Input placeholder="Text" fieldName={BasicGenFields.INPUT} />
              <Button
                type="submit"
                bg="orange.800"
                disabled={
                  formMethods.getFieldState(BasicGenFields.INPUT).invalid
                }
              >
                <IoSendOutline />
              </Button>
            </HStack>
          </Stack>
        </form>
      </FormProvider>
    </div>
  );
};

export default BasicGen;
