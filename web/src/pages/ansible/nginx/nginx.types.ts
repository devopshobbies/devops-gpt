import { z as zod } from 'zod';

export interface NginxAnsibleResponse {
  output: string;
}

export interface NginxAnsibleBody {
  ansible_user: string;
  ansible_port: number;
  os: string;
  hosts: string[];
  version: string;
}

export interface nginxTemplateValidationError {
  detail: [
    {
      type: string;
      loc: string[];
      msg: string;
      input: null;
    },
  ];
}

export const nginxAnsibleSchema = zod.object({
  ansible_user: zod.string().min(1, 'User is required!'),
  ansible_port: zod
    .number({ invalid_type_error: 'Port is required!' })
    .min(1, 'Port is required!'),
  os: zod.object({
    label: zod.string(),
    value: zod.string(),
  }),
  hosts: zod
    .array(
      zod.object({
        value: zod.string().min(1, 'Host is required!'),
      }),
    )
    .min(1),
  version: zod.object({
    label: zod.string(),
    value: zod.string(),
  }),
});

export type NginxAnsible = zod.infer<typeof nginxAnsibleSchema>;
