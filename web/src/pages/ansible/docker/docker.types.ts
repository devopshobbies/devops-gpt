import { z as zod } from 'zod';

export interface DockerAnsibleResponse {
  output: string;
}

export interface DockerAnsibleBody {
  ansible_user?: string;
  ansible_port: number;
  os: string;
  hosts: string[];
}

export interface dockerTemplateValidationError {
  detail: [
    {
      type: string;
      loc: string[];
      msg: string;
      input: null;
    },
  ];
}

export const dockerAnsibleSchema = zod.object({
  ansible_user: zod.string().optional(),
  ansible_port: zod.number({}),
  os: zod.string().min(1, 'OS is required!'),
  hosts: zod
    .array(
      zod.object({
        value: zod.string().min(1, 'Host is required!'),
      }),
    )
    .min(1),
});

export type DockerAnsible = zod.infer<typeof dockerAnsibleSchema>;
