import { useCallback, useRef } from "react";
import useGptStore from "../utils/store";
import apiClient from "../utils/apiClient";
import { nameGenerator } from "../utils/nameGenerator";

const useDownload = (folderName: string) => {
  const { isSuccess, endpoint } = useGptStore((s) => s.generatorQuery);
  const downloadRef = useRef<HTMLAnchorElement>(null);
  const downloadFile = useCallback(async () => {
    if (!isSuccess) return;

    try {
      if (!downloadRef.current) return;

      const url =
        apiClient.defaults.baseURL +
        `/download-folder${folderName}/${nameGenerator(endpoint)}`;

      downloadRef.current.href = url;
      // downloadRef.current.target = "_blank";

      downloadRef.current.click();
    } catch (error) {
      console.error("Error downloading file:", error);
    }
  }, [isSuccess, endpoint]);
  return { downloadFile, isSuccess, endpoint, downloadRef };
};
export default useDownload;
