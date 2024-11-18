import { Button, HStack, Stack } from "@chakra-ui/react";
import { FormProvider } from "react-hook-form";
import { IoSendOutline } from "react-icons/io5";
import ChatBox from "../../components/internal-ui/ChatBox";
import Input from "../../components/internal-ui/Input";
import useFormHandler from "../../hooks/useFormHandler";
import { bugFixMapper } from "../../utils/mapperFunctions";
import useGptStore from "../../utils/store";
import { bugFixDefaultValues, BugFixFields, Endpoints } from "../constants";
import { ApiRequestBugFix, BugFixFormData } from "../model";

const BugFix = () => {
  const { request, handleSubmit, onSubmit, formMethods } = useFormHandler<
    BugFixFormData,
    ApiRequestBugFix
  >(bugFixDefaultValues);

  const messages = useGptStore((s) => s.messages);

  const handleFormSubmit = handleSubmit((data) => {
    onSubmit(bugFixMapper(data), data.bugDescription);
  });

  return (
    <FormProvider {...formMethods}>
      <form onSubmit={handleFormSubmit}>
        <Stack gap="3" justifyContent="center" alignItems="center">
          <div className="flex gap-2">
            <Input fieldName={BugFixFields.MIN_TOKEN} label="Min token" />
            <Input fieldName={BugFixFields.MAX_TOKEN} label="Max token" />
            <Input fieldName={BugFixFields.SERVICE} label="Service" />
            <Input fieldName={BugFixFields.VERSION} label="Version" />
          </div>
          <ChatBox
            endpoint={Endpoints.POST_FIX}
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
            <Input
              placeholder="Text"
              fieldName={BugFixFields.BUG_DESCRIPTION}
            />
            <Button
              type="submit"
              bg="orange.800"
              disabled={
                formMethods.getFieldState(BugFixFields.BUG_DESCRIPTION).invalid
              }
            >
              <IoSendOutline />
            </Button>
          </HStack>
        </Stack>
      </form>
    </FormProvider>
  );
};

export default BugFix;
