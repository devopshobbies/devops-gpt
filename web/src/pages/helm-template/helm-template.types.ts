import { z as zod } from 'zod';

export interface HelmTemplateBody {
  api_version: number;
  pods: Pod[];
}

export interface HelmTemplateResponse {
  output: string;
}

export interface helmTemplateValidationError {
  detail: [
    {
      type: string;
      loc: string[];
      msg: string;
      input: null;
    },
  ];
}

export interface Pod {
  name: string;
  image: string;
  target_port: string | null;
  replicas: string | null;
  persistance: {
    size: string;
    accessModes: string;
  };
  environment: {
    name: string;
    value: string;
  }[];

  stateless: boolean;
  ingress: {
    enabled: boolean;
    host: string;
  };
}

const environmentSchema = zod.object({
  name: zod.string().min(1, 'Name is required'),
  value: zod.string().min(1, 'Value is required'),
});

const labelValueSchema = zod.object({
  label: zod.string(),
  value: zod.string(),
});

const persistanceSchema = zod.object({
  mode: labelValueSchema,
  size: zod.string().min(1, 'Size is required'),
  accessModes: labelValueSchema,
});

const ingressSchema = zod.object({
  enabled: zod.boolean(),
  host: zod.string(),
});

const podSchema = zod.object({
  name: zod.string().min(1, 'Name is required'),
  image: zod.string().min(1, 'Image is required'),
  target_port: zod.string().nullable(),
  replicas: zod.string().nullable(),
  persistance: persistanceSchema,
  environment: zod
    .array(environmentSchema)
    .min(1, 'At least one environment variable is required'),
  stateless: zod.boolean(),
  ingress: ingressSchema,
});

export const helmTemplateSchema = zod.object({
  api_version: zod.string().min(1, 'API version is required'),
  pods: zod.array(podSchema).min(1, 'At least one pod is required'),
});
export type HelmTemplateSchema = zod.infer<typeof helmTemplateSchema>;
