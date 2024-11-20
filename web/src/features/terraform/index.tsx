import { useEffect, useState } from "react";
import useGptStore from "../../utils/store";
import { routes, terraformBtnMapping } from "../../utils/routing";
import { Button } from "@chakra-ui/react";
import { Link, Outlet } from "react-router-dom";
import useDownload from "../../hooks/useDownload";
import { DownloadFolders } from "../constants";

const Terraform = () => {
  const setGeneratorQuery = useGptStore((s) => s.setGeneratorQuery);

  const [selected, setSelected] = useState<number>();

  const { downloadFile, isSuccess, endpoint, downloadRef } = useDownload(
    DownloadFolders.MY_TERRAFORM
  );

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
