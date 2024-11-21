import { RegisterOptions } from "react-hook-form";
import {
  BasicGenFields,
  BugFixFields,
  InstallFields,
} from "../features/constants";

export const validateForm = (fieldName: string) => {
  let validationRules: RegisterOptions = {};
  switch (fieldName) {
    case BasicGenFields.MIN_TOKEN:
      validationRules = {
        min: {
          value: 100,
          message: "Min value is 100",
        },
        max: {
          value: 500,
          message: "Can not be more than 500",
        },
      };
      break;
    case BasicGenFields.MAX_TOKEN:
      validationRules = {
        min: {
          value: 100,
          message: "Can not be less than 100",
        },
        max: {
          value: 500,
          message: "Max value is 500",
        },
      };
      break;
    case BugFixFields.VERSION:
    case BugFixFields.BUG_DESCRIPTION:
    case InstallFields.OS:
    case InstallFields.SERVICE:
    case BasicGenFields.INPUT:
      validationRules = {
        required: {
          value: true,
          message: "Input can not be empty",
        },
      };
      break;
  }
  return validationRules;
};
