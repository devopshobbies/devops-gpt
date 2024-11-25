import { FormProvider } from "react-hook-form";
import CheckBox from "../../components/internal-ui/CheckBox";
import Input from "../../components/internal-ui/Input";
import {
  DownloadFolders,
  Endpoints,
  helmDefaultValues,
  HelmFields,
} from "../constants";
import useQueryGenerator from "../../hooks/useQueryGenerator";
import { helmFieldProperties } from "./constants";
import useDownload from "../../hooks/useDownload";
import { useEffect, useState } from "react";
import useGptStore from "../../utils/store";
import { ApiRequestHelm, HelmFormData } from "../models";
import { helmMapper } from "../../utils/mapperFunctions";

const Helm = () => {
  const [formData, setFormData] = useState<HelmFormData>();
  const [pod, setPod] = useState(0);

  const { formMethods, handleSubmit, isError, onSubmit, status } =
    useQueryGenerator<HelmFormData, ApiRequestHelm>(
      helmDefaultValues,
      Endpoints.POST_IAC_HELM
    );

  const setGeneratorQuery = useGptStore((s) => s.setGeneratorQuery);

  const { downloadFile, downloadRef, endpoint, isSuccess } = useDownload(
    DownloadFolders.MY_HELM
  );

  const handlePodsAddition = handleSubmit((submittedData) => {
    setFormData((prevData) => ({
      apiVersion: prevData?.apiVersion ?? submittedData.apiVersion ?? 2,
      pods: [...(prevData?.pods ?? [], submittedData.pods)],
    }));
    setPod((prev) => (prev !== 7 ? prev + 1 : prev + 0));
  });

  const handleFormSubmit = handleSubmit(() => {
    if (formData && formMethods.formState.isSubmitted) {
      onSubmit(helmMapper(formData));
    } else {
      console.error("Form data is invalid");
    }
  });

  useEffect(() => {
    if (isSuccess) {
      downloadFile();
      setGeneratorQuery(false, "");
    }
  }, [endpoint, isSuccess, downloadFile, downloadRef]);

  return (
    <div className="w-full ">
      <FormProvider {...formMethods}>
        <form onSubmit={handleFormSubmit}>
          <div className="grid grid-cols-1 gap-6">
            <div className="flex items-center justify-center">
              <Input
                fieldName={HelmFields.API_VERSION}
                label="Api version"
                placeholder="2.0"
              />
            </div>
            <hr className="border-t border-gray-300 mt-4" />
            {/* Render form fields for the current pod */}
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
                            fieldName={`pods[${pod}].${field.fieldName}`} // Map fields to the current pod
                            label={field.label}
                            placeholder={field.placeholder}
                          />
                        ) : (
                          <div className="mt-8">
                            <CheckBox
                              fieldName={`pods[${pod}].${field.fieldName}`} // Map checkboxes to the current pod
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
              <div className="flex flex-col py-5">
                {isSuccess && (
                  <p className="text-green-500">Generated Successfully</p>
                )}
                {formData?.pods.length && !isSuccess && (
                  <p className="text-green-700">
                    {formData.pods.length} Pod{formData.pods.length > 1 && "'s"}{" "}
                    added
                  </p>
                )}
                {formData?.pods.length === 8 && (
                  <p className="text-warning">You can add up to 8 pods</p>
                )}
                {isError && <p className="text-red-600">Operation failed</p>}
              </div>
              <div className="flex gap-x-5 justify-center items-center">
                <button
                  className="btn-success btn btn-square w-20"
                  type="button"
                  onClick={handlePodsAddition}
                >
                  Add Pod
                </button>
                <button
                  disabled={!formMethods.formState.isSubmitted}
                  type="submit"
                  className="bg-orange-600 w-32 h-12 rounded-md disabled:bg-gray-700 disabled:text-gray-400 disabled:hover:cursor-not-allowed"
                >
                  {status === "pending" ? (
                    <span className="loading loading-ring loading-lg "></span>
                  ) : (
                    <p>Generate</p>
                  )}
                </button>
              </div>
            </div>
          </div>
        </form>
      </FormProvider>
      <a ref={downloadRef} style={{ display: "none" }} />
    </div>
  );
};

export default Helm;
