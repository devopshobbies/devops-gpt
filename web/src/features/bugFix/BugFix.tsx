import { Stack, HStack, Button } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { useForm, FormProvider } from "react-hook-form";
import { IoSendOutline } from "react-icons/io5";
import ChatBox from "../../components/internal-ui/ChatBox";
import useGptStore from "../../utils/store";
import { UserType, ENDPOINTS, BugFixFields } from "../constants";
import { BugFixFormData, ApiRequestBugFix } from "../model";
import { v4 as uuid } from "uuid";
import Input from "../../components/internal-ui/Input";

const BugFix = () => {
  const formMethods = useForm<BugFixFormData>({
    defaultValues: {
      minToken: 100,
      maxToken: 500,
      service: "terraform",
      version: "latest",
      bugDescription: undefined,
    },
    mode: "onSubmit",
  });

  const { handleSubmit } = formMethods;

  const messages = useGptStore((s) => s.messages);
  const addMessage = useGptStore((s) => s.addMessage);
  const [req, setReq] = useState<ApiRequestBugFix | null>(null);

  const onSubmit = (data: BugFixFormData) => {
    addMessage(UserType.USER, data.bugDescription, uuid());
    const request: ApiRequestBugFix = {
      min_token: data.minToken,
      max_token: data.maxToken,
      service: data.service,
      bug_description: data.bugDescription,
      version: data.version,
      requestId: uuid(),
    };
    if (data.bugDescription) setReq(request);
  };

  useEffect(() => {
    return () => setReq(null);
  }, []);

  return (
    <div>
      <FormProvider {...formMethods}>
        <form onSubmit={(e) => void handleSubmit(onSubmit)(e)}>
          <Stack gap="3" justifyContent="center" alignItems="center">
            <div className="flex gap-2">
              <Input fieldName={BugFixFields.MIN_TOKEN} label="Min token" />
              <Input fieldName={BugFixFields.MAX_TOKEN} label="Max token" />
              <Input fieldName={BugFixFields.SERVICE} label="Service" />
              <Input fieldName={BugFixFields.VERSION} label="Version" />
            </div>
            <ChatBox
              endpoint={ENDPOINTS.postFix}
              request={req}
              messageData={messages}
              id={req?.requestId ?? ""}
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
                  formMethods.getFieldState(BugFixFields.BUG_DESCRIPTION)
                    .invalid
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

export default BugFix;
