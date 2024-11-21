import { useFormContext } from "react-hook-form";

import { HStack } from "@chakra-ui/react";
import { CSSProperties } from "react";

export interface Checkboxprops {
  fieldName: string;
  label: string;
  style?: CSSProperties;
  variant?: "chunk" | "standard";
}

const CheckBox = ({
  fieldName,
  label,
  style,
  variant = "standard",
}: Checkboxprops) => {
  const { register } = useFormContext();
  return (
    <>
      <HStack alignItems={"center"}>
        {variant === "standard" ? (
          <>
            <p>{label}</p>
            <input
              className=" w-4 h-4 accent-orange-700"
              {...register(fieldName)}
              type="checkbox"
              style={style}
            />
          </>
        ) : (
          <div className="flex rounded-md border-[0.5px] border-orange-300 py-4 px-8 gap-x-5 items-center justify-between">
            <p>{label}</p>
            <input
              className=" w-8 h-8  accent-orange-700"
              {...register(fieldName)}
              type="checkbox"
              style={style}
            />
          </div>
        )}
      </HStack>
    </>
  );
};

export default CheckBox;
