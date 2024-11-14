import { Box } from "@chakra-ui/react";
import ChatBubble from "./ChatBubble";
import { Message } from "../../features/model";
import usePost from "../../hooks/usePost";
import { ENDPOINTS, UserType } from "../../features/constants";
import useGptStore from "../../utils/store";
import { useEffect } from "react";

interface Props {
  messageData: Message[];
  endpoint: ENDPOINTS;
  request: any;
}

const ChatBox = ({ messageData, endpoint, request }: Props) => {
  const addMessage = useGptStore((s) => s.addMessage);
  const { data, error, isPending } = usePost(endpoint, request);

  useEffect(() => {
    addMessage(UserType.BOT, data?.data.output);
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
      {messageData.map((message, index) => (
        <ChatBubble
          isLoading={isPending}
          key={index}
          message={message.content}
          userType={message.user}
        />
      ))}
      {error && <p className="text-red-700">{error.message}</p>}
    </Box>
  );
};

export default ChatBox;
