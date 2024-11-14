import { Link } from "react-router-dom";
import { Image } from "@chakra-ui/react";

const Header = () => {
  return (
    <>
      <div className="flex h-24 w-full pt-0 mt-[-6px] bg-orange-950">
        <Link to="/">
          <Image
            mt="-2"
            ml="4"
            className="w-28 h-28"
            src="/IMG_20240909_212657_482-removebg.png"
          />
        </Link>
      </div>
    </>
  );
};

export default Header;
