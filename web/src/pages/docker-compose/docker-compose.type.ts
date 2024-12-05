import { z as zod } from 'zod';

export interface DockerComposeBody {
  version: string;
  services: {
    [key: string]: {
      build: {
        args: {
          [key: string]: string;
        };
        context: string;
        dockerfile: string;
      };
      command: string;
      container_name: string;
      depends_on: string[];
      environment: {
        [key: string]: string;
      };
      image: string;
      networks: string[];
      ports: string[];
      volumes: string[];
    };
  };
}

export interface DockerComposeResponse {
  output: string;
}

export interface DockerComposeValidationError {
  detail: [
    {
      type: string;
      loc: string[];
      msg: string;
      input: null;
    },
  ];
}

const KV_Schema = zod.array(
  zod.object({
    key: zod.string(),
    value: zod.string(),
  }),
);

export const BuildSchema = zod.object({
  enabled: zod.boolean(),
  args: KV_Schema,
  context: zod.string(),
  dockerfile: zod.string(),
});

export const ServiceSchema = zod.object({
  name: zod.string(),
  build: BuildSchema,
  image: zod.string(),
  environment: KV_Schema,
  container_name: zod.string(),
  ports: zod.array(zod.string()),
  command: zod.string().optional(),
  volumes: zod.array(zod.string()),
  networks: zod.array(zod.string()),
  depends_on: zod.array(zod.string()),
});

const labelValueSchema = zod.object({
  label: zod.string(),
  value: zod.enum(['bridge', 'host', 'none', 'overlay']),
});

export const NetworkSchema = zod.object({
  default: zod.boolean(),
  app_network: zod.array(
    zod.object({
      network_name: zod.string(),
      external: zod.boolean().optional(),
      driver: labelValueSchema,
      name: zod.string(),
    }),
  ),
});

export const DockerComposeSchema = zod.object({
  version: zod.string(),
  services: zod.array(ServiceSchema),
  networks: NetworkSchema,
});

export type TDockerCompose = zod.infer<typeof DockerComposeSchema>;
