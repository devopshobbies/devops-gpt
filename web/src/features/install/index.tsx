import { FormProvider } from "react-hook-form";
import { Endpoints, installDefaultValues, InstallFields } from "../constants";
import {
  ApiRequestInstall,
  ApiResponseDownload,
  InstallFormData,
} from "../models";
import useGenerator from "../../hooks/useGenerator";
import Input from "../../components/internal-ui/Input";
import { useCallback, useEffect, useRef } from "react";

const Install = () => {
  const {
    formMethods,
    data,
    handleSubmit,
    onSubmit,
    isError,
    isSuccess,
    status,
    request,
  } = useGenerator<InstallFormData, ApiRequestInstall>(
    installDefaultValues,
    Endpoints.POST_INSTALL
  );

  const downloadRef = useRef<HTMLAnchorElement>(null);

  const downloadFile = useCallback(
    (formData: ApiRequestInstall) => {
      if (downloadRef.current) {
        const response = data as ApiResponseDownload;
        const blob = new Blob([response.data.output], {
          type: "text/x-shellscript",
        });
        const url = URL.createObjectURL(blob);
        downloadRef.current.href = url;
        downloadRef.current.download = `Installation_${formData.os}_${formData.service}.sh`;
        downloadRef.current.click();
        URL.revokeObjectURL(url);
      }
    },
    [isSuccess, data, downloadRef]
  );

  useEffect(() => {
    if (isSuccess && data && request) {
      downloadFile(request);
    }
  }, [request, isError, data]);

  return (
    <>
      <FormProvider {...formMethods}>
        <form onSubmit={(e) => handleSubmit(onSubmit)(e)}>
          <div className="flex flex-col items-center mt-5 gap-y-4">
            <Input
              fieldName={InstallFields.OS}
              label="OS"
              placeholder="ex: ubuntu"
            />
            <Input
              fieldName={InstallFields.SERVICE}
              label="Service"
              placeholder="terraform"
            />
            <button
              type="submit"
              className="bg-orange-600 w-32 h-12 rounded-sm mt-5"
              disabled={status === "pending" && !data}
            >
              {status === "pending" ? (
                <span className="loading loading-ring loading-lg "></span>
              ) : (
                <p>Generate</p>
              )}
            </button>
            {isSuccess && (
              <p className="text-green-500">Generated Successfully</p>
            )}
            {isError && <p className="text-red-600">Operation failed</p>}
          </div>
        </form>
      </FormProvider>
      <a ref={downloadRef} style={{ display: "none" }} />
    </>
  );
};
export default Install;
