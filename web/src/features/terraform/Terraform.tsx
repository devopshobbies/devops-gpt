import { useCallback, useEffect, useRef, useState } from "react";
import useGptStore from "../../utils/store";
import { routes, terraformBtnMapping } from "../../utils/routing";
import { Button } from "@chakra-ui/react";
import { Link, Outlet } from "react-router-dom";
import { nameGenerator } from "../../utils/nameGenerator";

const Terraform = () => {
  const { endpoint, isSuccess } = useGptStore((s) => s.generatorQuery);
  const setGeneratorQuery = useGptStore((s) => s.setGeneratorQuery);

  const downloadRef = useRef<HTMLAnchorElement>(null);

  const [selected, setSelected] = useState<number>();

  const downloadFile = useCallback(async () => {
    if (!isSuccess) return;

    try {
      const response = await fetch(
        import.meta.env.VITE_PORT + "/download-folderMyTerraform"
      );
      if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        const fileName = nameGenerator(endpoint);

        const tempLink = document.createElement("a");
        tempLink.href = url;
        tempLink.target = "_blank";
        tempLink.download = `${fileName}.zip`;
        tempLink.style.display = "none";
        document.body.appendChild(tempLink);

        tempLink.click();
        document.body.removeChild(tempLink);
        URL.revokeObjectURL(url);
      }
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
