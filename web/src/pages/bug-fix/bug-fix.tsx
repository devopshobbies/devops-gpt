import { FC, useEffect, useRef, useState } from 'react';
import { Send } from 'lucide-react';
import { API } from '@/enums/api.enums';
import { BugFixBody, BugFixMessage, BugFixResponse } from './bug-fix.types';
import { usePost } from '@/core/react-query';
import { toast } from 'sonner';
import { BeatLoader } from 'react-spinners';

const BugFix: FC = () => {
  const { mutateAsync } = usePost<BugFixResponse, BugFixBody>(
    API.BugFix,
    'bug-fix',
  );

  const [minToken, setMinToken] = useState('100');
  const [maxToken, setMaxToken] = useState('500');
  const [service, setService] = useState('terraform');
  const [version, setVersion] = useState('latest');
  const [bugDescription, setBugDescription] = useState('');
  const [messages, setMessages] = useState<BugFixMessage[]>([]);

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
        { role: 'user', content: bugDescription },
        { role: 'assistant', content: '', loading: true },
      ]);

      const body: BugFixBody = {
        max_tokens: parseInt(maxToken),
        min_tokens: parseInt(minToken),
        service,
        bug_description: bugDescription,
        version,
      };
      const {
        data: { output },
      } = await mutateAsync(body);
      setBugDescription('');
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
      <div className="w-full max-w-[768px]">
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
                className="dark:bg-black-1 w-full rounded-md bg-gray-200 p-3 outline-none"
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
                className="dark:bg-black-1 w-full rounded-md bg-gray-200 p-3 outline-none"
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
                className="dark:bg-black-1 w-full rounded-md bg-gray-200 p-3 outline-none"
              />
            </div>
            <div className="flex w-full flex-col">
              <label htmlFor="version" className="mb-2">
                Version
              </label>
              <input
                id="version"
                type="text"
                value={version}
                onChange={(e) => setVersion(e.target.value)}
                className="dark:bg-black-1 w-full rounded-md bg-gray-200 p-3 outline-none"
              />
            </div>
          </div>
          <div className="mt-4">
            <div
              ref={messagesRef}
              className="h-96 w-full overflow-y-auto rounded-md bg-slate-900 p-3 scrollbar-thin scrollbar-track-transparent scrollbar-corner-transparent"
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
              value={bugDescription}
              onChange={(e) => setBugDescription(e.target.value)}
              rows={2}
              className="dark:bg-black-1 w-full resize-none rounded-md bg-gray-200 p-4 pr-16 outline-none"
            />
            <button
              disabled={!bugDescription}
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

export default BugFix;
