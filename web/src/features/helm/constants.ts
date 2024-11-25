import { HelmFields } from "../constants";

interface Field {
  fieldName: string;
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

export const helmFieldProperties: FieldProperties[] = [
  {
    group: {
      name: "Generic settings",
      fields: [
        {
          fieldName: HelmFields.NAME,
          label: "Name",
          type: "input",
          placeholder: "ex: web",
        },
        {
          fieldName: HelmFields.IMAGE,
          label: "Image",
          type: "input",
          placeholder: "nginx",
        },
        {
          fieldName: HelmFields.TARGET_PORT,
          label: "Target port",
          type: "input",
          placeholder: "80",
        },
        {
          fieldName: HelmFields.REPLICAS,
          label: "Replicas",
          type: "input",
          placeholder: "1",
        },
        {
          fieldName: HelmFields.STATELESS,
          label: "Stateless",
          type: "checkbox",
        },
      ],
    },
  },
  {
    group: {
      name: "Persistance",
      fields: [
        {
          fieldName: HelmFields.SIZE,
          label: "Size",
          type: "input",
          placeholder: "1Gi",
        },
        {
          fieldName: HelmFields.ACCESS_MODES,
          label: "Access modes",
          type: "input",
          placeholder: "ex: ReadWriteOnce",
        },
      ],
    },
  },
  {
    group: {
      name: "Environment",
      fields: [
        {
          fieldName: HelmFields.ENVIRONMENT_NAME,
          label: "Environment name",
          type: "input",
          placeholder: "ex: ENV1",
        },
        {
          fieldName: HelmFields.VALUE,
          label: "Value",
          type: "input",
          placeholder: "ex: Hi",
        },
      ],
    },
  },
  {
    group: {
      name: "Ingress",
      fields: [
        {
          fieldName: HelmFields.HOST,
          label: "HOST",
          type: "input",
          placeholder: "ex: www.example.com",
        },
        {
          fieldName: HelmFields.ENABLED,
          label: "Enabled",
          type: "checkbox",
        },
      ],
    },
  },
];
