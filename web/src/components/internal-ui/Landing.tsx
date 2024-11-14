import Drawer from "./Drawer";

import { btnMappings } from "../../utils/routing";
import { Link } from "react-router-dom";
import { Button, Center } from "@chakra-ui/react";
import useGptStore from "../../utils/store";

const Landing = () => {
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
      <Center>
        <Button
          w="10rem"
          mt="16"
          bg="orange.700"
          disabled={isOpen}
          onClick={() => setIsOpen(true)}
        >
          Open Features
        </Button>
      </Center>
    </>
  );
};

export default Landing;
