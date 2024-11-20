import { useCallback, useRef } from "react";
import useGptStore from "../utils/store";
import apiClient from "../utils/apiClient";
import { nameGenerator } from "../utils/nameGenerator";
import { DownloadFolders } from "../features/constants";

const useDownload = (folderName: DownloadFolders) => {
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
      downloadRef.current.click();
    } catch (error) {
      console.error("Error downloading file:", error);
    }
  }, [isSuccess, endpoint]);
  return { downloadFile, isSuccess, endpoint, downloadRef };
};
export default useDownload;
