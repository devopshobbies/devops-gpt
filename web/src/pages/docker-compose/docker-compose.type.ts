import { z as zod } from 'zod';

interface IBuildConfig {
  args: {
    [key: string]: string;
  };
  context: string;
  dockerfile: string;
}

interface IServiceConfig {
  [key: string]: {
    build: IBuildConfig;
    image: string;
    environment: {
      [key: string]: string;
    };
    container_name: string;
    ports: string[];
    command?: string;
    volumes: string[];
    networks: string[];
    depends_on: string[];
  };
}

export interface INetworkConfig {
  [key: string]:
    | {
        driver: 'bridge' | 'host' | 'none' | 'overlay';
      }
    | {
        name: string;
        external: boolean;
      };
}

export interface DockerComposeBody {
  version: string;
  services: IServiceConfig;
  networks: INetworkConfig;
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
    key: zod
      .string()
      .min(1, { message: 'Key must be at least 1 character long' }),
    value: zod
      .string()
      .min(1, { message: 'Value must be at least 1 character long' }),
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

export const NetworkSchema = zod.union([
  zod.object({
    custom: zod.literal(false),
    app_network: zod.array(
      zod.object({
        network_name: zod.string(),
        driver: labelValueSchema,
      }),
    ),
  }),
  zod.object({
    custom: zod.literal(true),
    app_network: zod.array(
      zod.object({
        network_name: zod.string(),
        external: zod.boolean().optional(),
        name: zod.string(),
      }),
    ),
  }),
]);

export const DockerComposeSchema = zod.object({
  version: zod.string(),
  services: zod.array(ServiceSchema),
  networks: NetworkSchema,
});

export type TDockerCompose = zod.infer<typeof DockerComposeSchema>;
