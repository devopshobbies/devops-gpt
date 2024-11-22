import { FormProvider } from "react-hook-form";
import CheckBox from "../../components/internal-ui/CheckBox";
import Input from "../../components/internal-ui/Input";
import { helmMapper } from "../../utils/mapperFunctions";
import { DownloadFolders, Endpoints, helmDefaultValues } from "../constants";
import useQueryGenerator from "../../hooks/useQueryGenerator";
import { helmFieldProperties } from "./constants";
import useDownload from "../../hooks/useDownload";
import { useEffect } from "react";
import useGptStore from "../../utils/store";
import { ApiRequestHelm, HelmFormData } from "../models";

const Helm = () => {
  const { formMethods, data, handleSubmit, isError, onSubmit, status } =
    useQueryGenerator<HelmFormData, ApiRequestHelm>(
      helmDefaultValues,
      Endpoints.POST_IAC_HELM
    );

  const handleFormSubmit = handleSubmit((data) => onSubmit(helmMapper(data)));

  const setGeneratorQuery = useGptStore((s) => s.setGeneratorQuery);

  const { downloadFile, downloadRef, endpoint, isSuccess } = useDownload(
    DownloadFolders.MY_HELM
  );

  useEffect(() => {
    if (isSuccess) {
      downloadFile();
      setGeneratorQuery(false, "");
    }
  }, [endpoint, isSuccess, downloadFile, downloadRef]);

  const formValues = formMethods.watch();

  const isAllFieldsFilled = helmFieldProperties.every(({ group }) =>
    group.fields.every(
      (field) =>
        field.fieldName in formValues &&
        formValues[field.fieldName as keyof HelmFormData] !== ""
    )
  );

  return (
    <div className=" w-full mt-6 p-6">
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <div className="grid grid-cols-1 gap-6">
            {helmFieldProperties.map((group, groupIndex) => (
              <div key={groupIndex}>
                {/* Group Container */}
                <div className="grid grid-cols-1 lg:grid-cols-[200px_1fr] gap-4 items-center pb-4">
                  {/* Group Name */}
                  <div className="font-bold text-lg flex justify-center items-center">
                    {group.group.name}
                  </div>

                  {/* Group Fields */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                    {group.group.fields.map((field, fieldIndex) => (
                      <div
                        key={fieldIndex}
                        className="flex flex-col justify-center items-center"
                      >
                        {field.type === "input" ? (
                          <Input
                            fieldName={field.fieldName}
                            label={field.label}
                            placeholder={field.placeholder}
                          />
                        ) : (
                          <div className="mt-8">
                            <CheckBox
                              fieldName={field.fieldName}
                              label={field.label}
                              variant="chunk"
                            />
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>

                {/* Divider Line */}
                {groupIndex < helmFieldProperties.length - 1 && (
                  <hr className="border-t border-gray-300 mt-4" />
                )}
              </div>
            ))}
            <div className="flex items-center flex-col justify-center">
              {isSuccess && (
                <p className="text-green-500">Generated Successfully</p>
              )}
              {isError && <p className="text-red-600">Operation failed</p>}
              <button
                type="submit"
                className="bg-orange-600 w-32 h-12 rounded-md disabled:bg-gray-700 disabled:text-gray-400 disabled:hover:cursor-not-allowed"
                disabled={(status === "pending" && !data) || !isAllFieldsFilled}
              >
                {status === "pending" ? (
                  <span className="loading loading-ring loading-lg "></span>
                ) : (
                  <p>Generate</p>
                )}
              </button>
            </div>
          </div>
        </form>
      </FormProvider>
      <a ref={downloadRef} style={{ display: "none" }} />
    </div>
  );
};

export default Helm;
