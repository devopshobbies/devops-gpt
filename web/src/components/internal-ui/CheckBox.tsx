import { useFormContext } from "react-hook-form";

import { HStack } from "@chakra-ui/react";

export interface Checkboxprops {
  fieldName: string;
  label: string;
}

const CheckBox = ({ fieldName, label }: Checkboxprops) => {
  const { register } = useFormContext();
  return (
    <>
      <HStack alignItems={"center"} justifyContent={"center"}>
        <p>{label}</p>
        <input
          className=" w-4 h-4 accent-orange-700"
          {...register(fieldName)}
          type="checkbox"
        />
      </HStack>
    </>
  );
};

export default CheckBox;
