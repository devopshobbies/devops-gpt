import { FC } from 'react';

const Installation: FC = () => {
  return (
    <div className="flex items-center justify-center w-full h-full">
      <div className="w-full max-w-96">
        <div className="border border-gray-500 divide-y divide-gray-500 rounded-md">
          <input
            placeholder="os (example: ubuntu)"
            className="block w-full p-2 outline-none rounded-t-md"
          />
          <input
            placeholder="tool (example: nginx)"
            className="block w-full p-2 outline-none rounded-b-md"
          />
        </div>
        <button className="w-full mt-3 text-white btn bg-orange-base hover:bg-orange-base/70">
          Submit
        </button>
      </div>
    </div>
  );
};

export default Installation;
