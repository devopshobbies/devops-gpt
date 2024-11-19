import { useCallback, useEffect, useRef, useState } from "react";
import useGptStore from "../../utils/store";
import { Endpoints } from "../constants";
import { routes, terraformBtnMapping } from "../../utils/routing";
import { Button } from "@chakra-ui/react";
import { Link, Outlet } from "react-router-dom";

const Terraform = () => {
  const { endpoint, isSuccess } = useGptStore((s) => s.generatorQuery);

  const downloadRef = useRef<HTMLAnchorElement>(null);

  const [selected, setSelected] = useState<number>();

  const downloadFile = useCallback(() => {
    if (!isSuccess) return;
    if (downloadRef.current) {
      downloadRef.current.href = Endpoints.DOWNLOAD_LINK;
      downloadRef.current.download = "media";
      downloadRef.current.click();
    }
  }, [isSuccess, endpoint]);

  useEffect(() => {
    if (isSuccess) {
      downloadFile();
    }
  }, [isSuccess, endpoint]);

  console.log(endpoint, isSuccess);

  return (
    <div>
      <div>
        {terraformBtnMapping.map((route, index) => (
          <Link to={routes.terraformTemplate + route.route} key={route.route}>
            <Button
              w="23.7rem"
              rounded={0}
              bg={selected === index ? "orange.800" : ""}
              _hover={{ bg: "orange.500" }}
              borderRight={
                index !== terraformBtnMapping.length - 1 ? "solid" : "none"
              }
              borderRightWidth={"0.5px"}
              onClick={() => setSelected(index)}
            >
              {route.label}
            </Button>
          </Link>
        ))}
      </div>
      <div className="py-9">
        <Outlet />
      </div>
      <a ref={downloadRef} style={{ display: "none" }} />
    </div>
  );
};

export default Terraform;
