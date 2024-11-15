import { Box } from "@chakra-ui/react";
import ChatBubble from "./ChatBubble";
import { Message } from "../../features/model";
import usePost from "../../hooks/usePost";
import { ENDPOINTS, UserType } from "../../features/constants";
import useGptStore from "../../utils/store";
import { useEffect } from "react";
import { v4 as uuid } from "uuid";

interface Props {
  messageData: Message[];
  endpoint: ENDPOINTS;
  request: any;
  id: string;
}

interface BasicApiResponse {
  output: string;
}

const ChatBox = ({ messageData, endpoint, request, id }: Props) => {
  const addMessage = useGptStore((s) => s.addMessage);

  const { data, error, isLoading } = usePost<BasicApiResponse>(
    endpoint,
    request,
    id
  );

  useEffect(() => {
    if (data?.data.output) addMessage(UserType.BOT, data?.data.output!, uuid());
  }, [request, data]);

  return (
    <Box
      w="100%"
      shadow="2xl"
      h="30rem"
      rounded="2xl"
      className="bg-transparent border border-stone-600 bg-stone-950"
      p="1rem"
      overflowY="auto"
    >
      {messageData.map((message) => (
        <ChatBubble
          isLoading={isLoading}
          key={message.id}
          message={message.content}
          userType={message.user}
        />
      ))}
      {error && <p className="text-red-700">{error.message}</p>}
    </Box>
  );
};

export default ChatBox;
