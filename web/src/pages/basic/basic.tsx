import { FC, useEffect, useRef, useState } from 'react';
import { Send } from 'lucide-react';
import { toast } from 'sonner';
import { usePost } from '@/core/react-query';
import { BasicBody, BasicMessage, BasicResponse } from './basic.types';
import { API } from '@/enums/api.enums';
import { BeatLoader } from 'react-spinners';

const Basic: FC = () => {
  const { mutateAsync } = usePost<BasicResponse, BasicBody>(API.Basic, 'basic');

  const [minToken, setMinToken] = useState('100');
  const [maxToken, setMaxToken] = useState('500');
  const [service, setService] = useState('terraform');
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<BasicMessage[]>([]);

  const messagesRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (messagesRef.current) {
      messagesRef.current.scrollTo({
        top: messagesRef.current.scrollHeight,
        behavior: 'smooth',
      });
    }
  }, [messages]);

  const handleSendMessage = async () => {
    try {
      setMessages((prev) => [
        ...prev,
        { role: 'user', content: input },
        { role: 'assistant', content: '', loading: true },
      ]);

      const body: BasicBody = {
        max_tokens: parseInt(maxToken),
        min_tokens: parseInt(minToken),
        service,
        input,
      };
      const {
        data: { output },
      } = await mutateAsync(body);
      setInput('');
      setMessages((prev) =>
        prev.map((message, index) =>
          index === prev.length - 1
            ? { ...message, content: output, loading: false }
            : message,
        ),
      );
    } catch (error) {
      console.log(error);
      setMessages((prev) => prev.slice(0, -1));
      toast.error('Something went wrong');
    }
  };

  return (
    <div className="flex h-[calc(100vh-56px)] w-full items-center justify-center text-black dark:text-white">
      <div className="w-full max-w-[1024px]">
        <div className="w-full rounded-md p-2">
          <div className="flex h-full w-full items-center justify-center gap-3">
            <div className="flex w-full flex-col">
              <label htmlFor="min_token" className="mb-2">
                Min Token
              </label>
              <input
                id="min_token"
                type="number"
                value={minToken}
                onChange={(e) => setMinToken(e.target.value)}
                className="w-full rounded-md bg-gray-200 p-3 outline-none dark:bg-black-1"
              />
            </div>
            <div className="flex w-full flex-col">
              <label htmlFor="max_token" className="mb-2">
                Max Token
              </label>
              <input
                id="max_token"
                type="number"
                value={maxToken}
                onChange={(e) => setMaxToken(e.target.value)}
                className="w-full rounded-md bg-gray-200 p-3 outline-none dark:bg-black-1"
              />
            </div>
            <div className="flex w-full flex-col">
              <label htmlFor="service" className="mb-2">
                Service
              </label>
              <input
                id="service"
                type="text"
                value={service}
                onChange={(e) => setService(e.target.value)}
                className="w-full rounded-md bg-gray-200 p-3 outline-none dark:bg-black-1"
              />
            </div>
          </div>
          <div className="mt-4">
            <div
              ref={messagesRef}
              className="h-[550px] w-full overflow-y-auto rounded-md bg-slate-900 p-3 scrollbar-thin scrollbar-track-transparent scrollbar-corner-transparent"
            >
              {messages.map((message) =>
                message.role === 'user' ? (
                  <div className="chat chat-end max-w-full">
                    <div className="chat-bubble bg-gray-600 text-white">
                      {message.content}
                    </div>
                  </div>
                ) : (
                  <div className="chat chat-start max-w-full">
                    <div className="chat-bubble text-white">
                      {message.loading ? (
                        <BeatLoader color="#e3e3e3" size={10} />
                      ) : (
                        message.content
                      )}
                    </div>
                  </div>
                ),
              )}
            </div>
          </div>
          <div className="relative mt-4">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              rows={2}
              className="w-full resize-none rounded-md bg-gray-200 p-4 pr-16 outline-none dark:bg-black-1"
            />
            <button
              disabled={!input}
              onClick={handleSendMessage}
              className="absolute right-3 top-5 flex items-center justify-center rounded-full bg-white p-2 transition-all disabled:opacity-50"
            >
              <Send className="size-6 stroke-[#121212]" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Basic;
