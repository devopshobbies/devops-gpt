import { FC } from 'react';
import { Send } from 'lucide-react';

const BugFix: FC = () => {
  return (
    <div className="flex h-full w-full items-center justify-center">
      <div className="w-full max-w-[768px]">
        <div className="w-full rounded-md p-2">
          <div className="flex h-full w-full items-center justify-center gap-3">
            <div className="flex w-full flex-col">
              <label htmlFor="min_token" className="mb-2">
                Min Token
              </label>
              <input
                id="min_token"
                className="w-full rounded-md p-3 outline-none"
              />
            </div>
            <div className="flex w-full flex-col">
              <label htmlFor="min_token" className="mb-2">
                Max Token
              </label>
              <input
                id="min_token"
                className="w-full rounded-md p-3 outline-none"
              />
            </div>
            <div className="flex w-full flex-col">
              <label htmlFor="min_token" className="mb-2">
                Service
              </label>
              <input
                id="min_token"
                className="w-full rounded-md p-3 outline-none"
              />
            </div>
            <div className="flex w-full flex-col">
              <label htmlFor="min_token" className="mb-2">
                Version
              </label>
              <input
                id="min_token"
                className="w-full rounded-md p-3 outline-none"
              />
            </div>
          </div>
          <div className="mt-4">
            <div className="scrollbar-corner-transparent scrollbar-thin scrollbar-track-transparent h-96 w-full overflow-y-auto rounded-md bg-slate-900 p-3">
              <div className="chat chat-end max-w-full">
                <div className="chat-bubble bg-gray-600 text-white">
                  You underestimate my power!
                </div>
              </div>
              <div className="chat chat-start max-w-full">
                <div className="chat-bubble text-white">
                  You underestimate my power!
                </div>
              </div>
              <div className="chat chat-end max-w-full">
                <div className="chat-bubble bg-gray-600 text-white">
                  You underestimate my power!
                </div>
              </div>
              <div className="chat chat-start max-w-full">
                <div className="chat-bubble text-white">
                  You underestimate my power!
                </div>
              </div>
              <div className="chat chat-end max-w-full">
                <div className="chat-bubble bg-gray-600 text-white">
                  You underestimate my power!
                </div>
              </div>
              <div className="chat chat-start max-w-full">
                <div className="chat-bubble text-white">
                  You underestimate my power!
                </div>
              </div>
              <div className="chat chat-end max-w-full">
                <div className="chat-bubble bg-gray-600 text-white">
                  You underestimate my power!
                </div>
              </div>
              <div className="chat chat-start max-w-full">
                <div className="chat-bubble text-white">
                  You underestimate my power!
                </div>
              </div>
            </div>
          </div>
          <div className="relative mt-4">
            <textarea
              className="w-full resize-none rounded-md p-4 pr-16 outline-none"
              rows={2}
            />
            <button className="absolute right-3 top-5 flex items-center justify-center rounded-full bg-white p-2">
              <Send className="size-6 stroke-[#121212]" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BugFix;
