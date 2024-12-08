import { FC, useEffect, useRef, useState } from 'react';
import { Send } from 'lucide-react';
import { toast } from 'sonner';
import { usePost } from '@/core/react-query';
import { BasicBody, BasicMessage, BasicResponse } from './basic.types';
import { API } from '@/enums/api.enums';
import { BeatLoader } from 'react-spinners';
import { isAxiosError } from 'axios';

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
      if (isAxiosError(error)) {
        if (error.response?.data.detail) {
          toast.error(error.response.data.detail);
        } else {
          toast.error('Something went wrong');
        }
      }
    }
  };

  return (
    <div className="flex h-[calc(100vh-56px)] w-full items-center justify-center text-black dark:text-white">
      <div className="w-full max-w-[1024px]">
        <div className="w-full p-2 rounded-md">
          <div className="flex items-center justify-center w-full h-full gap-3">
            <div className="flex flex-col w-full">
              <label htmlFor="min_token" className="mb-2">
                Min Token
              </label>
              <input
                id="min_token"
                type="number"
                value={minToken}
                onChange={(e) => setMinToken(e.target.value)}
                className="w-full p-3 bg-gray-200 rounded-md outline-none dark:bg-black-1"
              />
            </div>
            <div className="flex flex-col w-full">
              <label htmlFor="max_token" className="mb-2">
                Max Token
              </label>
              <input
                id="max_token"
                type="number"
                value={maxToken}
                onChange={(e) => setMaxToken(e.target.value)}
                className="w-full p-3 bg-gray-200 rounded-md outline-none dark:bg-black-1"
              />
            </div>
            <div className="flex flex-col w-full">
              <label htmlFor="service" className="mb-2">
                Service
              </label>
              <input
                id="service"
                type="text"
                value={service}
                onChange={(e) => setService(e.target.value)}
                className="w-full p-3 bg-gray-200 rounded-md outline-none dark:bg-black-1"
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
                  <div className="max-w-full chat chat-end">
                    <div className="text-white bg-gray-600 chat-bubble">
                      {message.content}
                    </div>
                  </div>
                ) : (
                  <div className="max-w-full chat chat-start">
                    <div className="text-white chat-bubble">
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
              className="w-full p-4 pr-16 bg-gray-200 rounded-md outline-none resize-none dark:bg-black-1"
            />
            <button
              disabled={!input}
              onClick={handleSendMessage}
              className="absolute flex items-center justify-center p-2 transition-all bg-white rounded-full right-3 top-5 disabled:opacity-50"
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
