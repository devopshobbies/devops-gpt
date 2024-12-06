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
  host: zod.string().min(1, 'Host is required'),
});

const podSchema = zod.object({
  name: zod.string().min(1, 'Name is required'),
  image: zod.string().min(1, 'Image is required'),
  target_port: zod
    .number({ invalid_type_error: 'Target Port is required!' })
    .min(1, 'Target Port is required!'),
  replicas: zod
    .number({ invalid_type_error: 'Replicas is required!' })
    .min(1, 'Replicas is required'),
  persistance: persistanceSchema,
  environment: zod
    .array(environmentSchema)
    .min(1, 'At least one environment variable is required'),
  stateless: zod.boolean(),
  ingress: ingressSchema,
});

export const helmTemplateSchema = zod.object({
  api_version: zod
    .number({ invalid_type_error: 'API version is required!' })
    .min(1, 'API version is required'),
  pods: zod.array(podSchema).min(1, 'At least one pod is required'),
});
export type THelmTemplate = zod.infer<typeof helmTemplateSchema>;
