import { Box } from "@chakra-ui/react";
import ChatBubble from "./ChatBubble";
import { Message } from "../../features/models";
import { Endpoints, UserType } from "../../features/constants";
import useGptStore from "../../utils/store";
import { useEffect } from "react";
import { v4 as uuid } from "uuid";
import { useLocation } from "react-router-dom";
import usePost from "../../hooks/usePost";

interface Props {
  messageData: Message[];
  endpoint: Endpoints;
  request: any;
  id: string;
}

interface BasicApiResponse {
  output: string;
}

const ChatBox = ({ messageData, endpoint, request, id }: Props) => {
  const addMessage = useGptStore((s) => s.addMessage);
  const resetMessages = useGptStore((s) => s.resetMessages);

  const location = useLocation();

  const { data, error, isLoading } = usePost<BasicApiResponse>(
    endpoint,
    request,
    id
  );

  useEffect(() => {
    if (data?.data.output) addMessage(UserType.BOT, data?.data.output!, uuid());
  }, [request, data]);

  useEffect(() => {
    return () => resetMessages();
  }, [location.pathname]);

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
