import { z as zod } from 'zod';

export interface KuberAnsibleResponse {
  output: string;
}

export interface KuberAnsibleBody {
  ansible_user: string;
  ansible_port: number;
  os: string;
  k8s_worker_nodes: string[];
  k8s_master_nodes: string[];
  version: string;
}

export interface kuberTemplateValidationError {
  detail: [
    {
      type: string;
      loc: string[];
      msg: string;
      input: null;
    },
  ];
}

export const kuberAnsibleSchema = zod.object({
  ansible_user: zod.string().min(1, 'User is required!'),
  ansible_port: zod
    .number({ invalid_type_error: 'Port is required!' })
    .min(1, 'Port is required!'),
  os: zod.object({
    label: zod.string(),
    value: zod.string(),
  }),
  k8s_worker_nodes: zod
    .array(
      zod.object({
        value: zod.string().min(1, 'Required!').default('www.example.com'),
      }),
    )
    .min(1),
  k8s_master_nodes: zod.array(
    zod.object({
      value: zod.string().min(1, 'Required!').default('www.example.com'),
    }),
  ),
  version: zod.object({
    label: zod.string().min(1, 'Required!'),
    value: zod.string().min(1, 'Required!'),
  }),
});

export type KuberAnsible = zod.infer<typeof kuberAnsibleSchema>;
