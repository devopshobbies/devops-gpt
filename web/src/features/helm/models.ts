import { HelmFields } from "../constants";

interface Field {
  fieldName: HelmFields;
  label: string;
  placeholder?: string;
  type: string;
}

export interface FieldProperties {
  group: {
    name: string;
    fields: Field[];
  };
}
