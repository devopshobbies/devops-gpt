import { Image } from "@chakra-ui/react";
import useGptStore from "../utils/store";

const Header = () => {
  const setIsOpen = useGptStore((s) => s.setIsOpen);
  return (
    <>
      <div className="flex h-24 w-full px-10  bg-orange-700">
        <button onClick={() => setIsOpen(true)} className="">
          <Image
            className="w-[5.5rem] h-[5.5rem] rounded-md shadow-2xl"
            src="/IMG_20240909_212657_482-removebg.png"
          />
        </button>
      </div>
    </>
  );
};

export default Header;
