import { HelmFields } from "../constants";
import { FieldProperties } from "./models";

export enum HelmGroupNames {
  GENERIC_SETTINGS = "Generic settings",
  PERSISTANCE = "Persistance",
  ENVIRONMENT = "Environment",
  INGRESS = "Ingress",
}

export const helmFieldProperties: FieldProperties[] = [
  {
    group: {
      name: HelmGroupNames.GENERIC_SETTINGS,
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
      name: HelmGroupNames.PERSISTANCE,
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
      name: HelmGroupNames.ENVIRONMENT,
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
      name: HelmGroupNames.INGRESS,
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
