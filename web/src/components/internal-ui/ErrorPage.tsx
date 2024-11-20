import { Box, Button, Center } from "@chakra-ui/react";
import { MdOutlineNoEncryptionGmailerrorred } from "react-icons/md";
import { Link } from "react-router-dom";

const ErrorPage = () => {
  return (
    <Center>
      <Box mt="6rem" alignItems="center" className="flex flex-col">
        <div className="text-red-600 mb-5 flex items-center">
          <MdOutlineNoEncryptionGmailerrorred className="" size="2rem" />
          <p className="text-3xl">Unathorized Route</p>
        </div>
        <Link to="/">
          <Button bg="orange.600" color="gray.200" w="5rem">
            Go back
          </Button>
        </Link>
      </Box>
    </Center>
  );
};

export default ErrorPage;
