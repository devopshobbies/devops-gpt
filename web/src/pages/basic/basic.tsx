import { FC } from 'react';
import { Send } from 'lucide-react';

const Basic: FC = () => {
  return (
    <div className="flex items-center justify-center w-full h-full">
      <div className="w-full max-w-[768px]">
        <div className="w-full p-2 rounded-md">
          <div className="flex items-center justify-center w-full h-full gap-3">
            <div className="flex flex-col w-full">
              <label htmlFor="min_token" className="mb-2">
                Min Token
              </label>
              <input
                id="min_token"
                className="w-full p-3 rounded-md outline-none"
              />
            </div>
            <div className="flex flex-col w-full">
              <label htmlFor="min_token" className="mb-2">
                Max Token
              </label>
              <input
                id="min_token"
                className="w-full p-3 rounded-md outline-none"
              />
            </div>
            <div className="flex flex-col w-full">
              <label htmlFor="min_token" className="mb-2">
                Service
              </label>
              <input
                id="min_token"
                className="w-full p-3 rounded-md outline-none"
              />
            </div>
          </div>
          <div className="mt-4">
            <div className="w-full p-3 overflow-y-auto rounded-md scrollbar-corner-transparent scrollbar-thin scrollbar-track-transparent h-96 bg-slate-900">
              <div className="max-w-full chat chat-end">
                <div className="text-white bg-gray-600 chat-bubble">
                  You underestimate my power!
                </div>
              </div>
              <div className="max-w-full chat chat-start">
                <div className="text-white chat-bubble">
                  You underestimate my power!
                </div>
              </div>
              <div className="max-w-full chat chat-end">
                <div className="text-white bg-gray-600 chat-bubble">
                  You underestimate my power!
                </div>
              </div>
              <div className="max-w-full chat chat-start">
                <div className="text-white chat-bubble">
                  You underestimate my power!
                </div>
              </div>
              <div className="max-w-full chat chat-end">
                <div className="text-white bg-gray-600 chat-bubble">
                  You underestimate my power!
                </div>
              </div>
              <div className="max-w-full chat chat-start">
                <div className="text-white chat-bubble">
                  You underestimate my power!
                </div>
              </div>
              <div className="max-w-full chat chat-end">
                <div className="text-white bg-gray-600 chat-bubble">
                  You underestimate my power!
                </div>
              </div>
              <div className="max-w-full chat chat-start">
                <div className="text-white chat-bubble">
                  You underestimate my power!
                </div>
              </div>
            </div>
          </div>
          <div className="relative mt-4">
            <textarea
              className="w-full p-4 pr-16 rounded-md outline-none resize-none"
              rows={2}
            />
            <button className="absolute flex items-center justify-center p-2 bg-white rounded-full right-3 top-5">
              <Send className="size-6 stroke-[#121212]" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Basic;
