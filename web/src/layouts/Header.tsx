import { Image } from "@chakra-ui/react";
import useGptStore from "../utils/store";

const Header = () => {
  const setIsOpen = useGptStore((s) => s.setIsOpen);
  return (
    <>
      <div className="flex h-24 w-full shadow-md">
        <button onClick={() => setIsOpen(true)}>
          <Image
            mt="-2"
            ml="4"
            className="w-28 h-28"
            src="/IMG_20240909_212657_482-removebg.png"
          />
        </button>
      </div>
    </>
  );
};

export default Header;
