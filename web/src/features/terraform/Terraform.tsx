import { useCallback, useEffect, useRef, useState } from "react";
import useGptStore from "../../utils/store";
import { routes, terraformBtnMapping } from "../../utils/routing";
import { Button } from "@chakra-ui/react";
import { Link, Outlet } from "react-router-dom";
import { nameGenerator } from "../../utils/nameGenerator";
import apiClient from "../../utils/apiClient";

const Terraform = () => {
  const { endpoint, isSuccess } = useGptStore((s) => s.generatorQuery);
  const setGeneratorQuery = useGptStore((s) => s.setGeneratorQuery);

  const downloadRef = useRef<HTMLAnchorElement>(null);

  const [selected, setSelected] = useState<number>();

  const downloadFile = useCallback(async () => {
    if (!isSuccess) return;

    try {
      if (!downloadRef.current) return;

      const url = apiClient.defaults.baseURL + "/download-folderMyTerraform";

      downloadRef.current.href = url;
      downloadRef.current.target = "_blank";
      downloadRef.current.download = `${nameGenerator(endpoint)}`;

      downloadRef.current.click();
    } catch (error) {
      console.error("Error downloading file:", error);
    }
  }, [isSuccess, endpoint]);

  useEffect(() => {
    if (isSuccess) {
      downloadFile();
      setGeneratorQuery(false, "");
    }
  }, [isSuccess, endpoint, downloadFile, setGeneratorQuery]);

  return (
    <div>
      <div className="flex items-center justify-center">
        {terraformBtnMapping.map((route, index) => (
          <Link to={routes.terraformTemplate + route.route} key={route.route}>
            <Button
              lg={{ w: "20rem" }}
              md={{ w: "15rem" }}
              sm={{ w: "10rem" }}
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
