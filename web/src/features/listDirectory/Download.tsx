import { FormProvider } from "react-hook-form";
import { ApiResponseDownload, DownloadFormData } from "../model";
import { useDirectoryDownloader } from "./hooks";
import Input from "../../components/internal-ui/Input";
import { DownloadFields, Endpoints } from "../constants";
import { Button } from "@chakra-ui/react";
import { useRef } from "react";

const Download = () => {
  const { isSuccess, handleSubmit, onSubmit, formMethods, data } =
    useDirectoryDownloader<DownloadFormData, ApiResponseDownload>(
      { download: "MyTerraform" },
      (formData) => formData.download,
      (resolvedEndpoint) => Endpoints.GET_DOWNLOAD_TERRAFORM + resolvedEndpoint
    );

  const downloadRef = useRef<HTMLAnchorElement>(null);
  const handleFormSubmit = handleSubmit((data) => onSubmit(data));

  const handleDownload = () => {
    if (isSuccess && data) {
      if (downloadRef.current) {
        downloadRef.current.href = `http://localhost/download-folderMyTerraform`;
        downloadRef.current.download = "app/mediaMyTerraform_zip";
        downloadRef.current.click();
      }
    }
  };

  return (
    <>
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <div className="flex flex-col items-center gap-2">
            <Input
              fieldName={DownloadFields.DOWNLOAD}
              label="Download"
              placeholder="Folder directory"
              style={{ width: "25rem" }}
              disabled={true}
            />
            {isSuccess && (
              <p className="text-green-700">
                File generated succesfully. Proceed to download
              </p>
            )}
            <div className="flex gap-6">
              <Button type="submit" bg="orange.700" w="8rem" h="3rem">
                Generate files
              </Button>
              <Button
                onClick={handleDownload}
                bg="orange.700"
                w="8rem"
                h="3rem"
                disabled={!isSuccess || !data}
              >
                Download
              </Button>
            </div>
          </div>
        </form>
      </FormProvider>
      {/* Hidden anchor for triggering downloads */}
      <a ref={downloadRef} style={{ display: "none" }} />
    </>
  );
};
export default Download;
