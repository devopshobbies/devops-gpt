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

export interface CompleteHelmForm {
  apiVersion: string;
  pods: {
    name: string;
    image: string;
    targetPort: number;
    replicas: number;
    environment: { name: string; value: string }[];
    size: string;
    accessModes: string;
    stateless: boolean;
    enabled: boolean;
    host: string;
  }[];
}
