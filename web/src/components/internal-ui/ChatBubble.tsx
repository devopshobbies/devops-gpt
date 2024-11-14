import { UserType } from "../../features/constants";

interface Props {
  message: string;
  userType: UserType;
  isLoading: boolean;
}

const ChatBubble = ({ message, userType, isLoading }: Props) => {
  if (!message) return;
  return (
    <div
      className={`chat ${
        userType === UserType.USER ? "chat-end" : "chat-start"
      }`}
    >
      <div
        className={`chat-bubble  ${
          userType === UserType.USER ? "bg-stone-600" : ""
        }`}
      >
        {userType === UserType.USER
          ? message
          : userType === UserType.BOT && isLoading
          ? "Thinkin..."
          : message}
      </div>
    </div>
  );
};
export default ChatBubble;
