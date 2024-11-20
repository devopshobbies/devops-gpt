import { Button } from "@chakra-ui/react";
import Drawer from "../components/internal-ui/Drawer";
import { btnMappings } from "../utils/routing";
import useGptStore from "../utils/store";
import Header from "./Header";
import { Link, Outlet } from "react-router-dom";

const Layout = () => {
  const isOpen = useGptStore((s) => s.isOpen);
  const setIsOpen = useGptStore((s) => s.setIsOpen);
  return (
    <>
      <Drawer
        isOpen={isOpen}
        onClose={() => setIsOpen(false)}
        title="Devops-GPT API"
        content={btnMappings.map((route) => (
          <Link key={route.route} to={route.route}>
            <Button w="full" _hover={{ bg: "orange.600" }}>
              {route.label}
            </Button>
          </Link>
        ))}
      />
      <Header />
      <div className="w-full text-gray-200 px-28 h-full ">
        <Outlet />
      </div>
    </>
  );
};

export default Layout;
