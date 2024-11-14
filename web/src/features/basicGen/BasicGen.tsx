import { FormProvider, useForm } from "react-hook-form";
import Input from "../../components/internal-ui/Input";
import { BasicGenFields, ENDPOINTS, UserType } from "../constants";
import { Button, HStack, Stack } from "@chakra-ui/react";

import useGptStore from "../../utils/store";
import ChatBox from "../../components/internal-ui/ChatBox";

import { BasicGenFormData } from "../model";
import { useEffect, useState } from "react";
import { IoSendOutline } from "react-icons/io5";

const BasicGen = () => {
  const formMethods = useForm<BasicGenFormData>({
    defaultValues: {
      minToken: 100,
      maxToken: 500,
      service: "terraform",
      input: undefined,
    },
    mode: "all",
  });

  const { handleSubmit } = formMethods;

  const messages = useGptStore((s) => s.messages);
  const addMessage = useGptStore((s) => s.addMessage);
  const [isDisabled, setIsDisabled] = useState(true);
  const [req, setReq] = useState<any>();

  const onSubmit = (data: BasicGenFormData) => {
    addMessage(UserType.USER, data.input);
    const request = {
      min_token: data.minToken,
      max_token: data.maxToken,
      service: data.service,
      input: data.input,
    };
    setReq(request);
  };

  useEffect(() => {
    setIsDisabled(!!formMethods.getFieldState(BasicGenFields.INPUT).isDirty);
  }, [formMethods]);

  return (
    <div>
      <FormProvider {...formMethods}>
        <form onSubmit={(e) => void handleSubmit(onSubmit)(e)}>
          <Stack gap="3" justifyContent="center" alignItems="center">
            <div className="flex gap-2">
              <Input fieldName={BasicGenFields.MIN_TOKEN} label="Min token" />
              <Input fieldName={BasicGenFields.MAX_TOKEN} label="Max token" />
              <Input fieldName={BasicGenFields.SERVICE} label="Service" />
            </div>
            <ChatBox
              endpoint={ENDPOINTS.postBasic}
              request={req}
              messageData={messages}
            />
            <HStack
              mt="3"
              alignItems="end"
              alignContent={"center"}
              justifyContent="center"
              bottom="5"
            >
              <Input placeholder="Text" fieldName={BasicGenFields.INPUT} />
              <Button type="submit" bg="orange.800" disabled={isDisabled}>
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
