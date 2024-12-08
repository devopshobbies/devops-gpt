import { z as zod } from 'zod';

interface IBuildConfig {
  args: {
    [key: string]: string;
  };
  context: string;
  dockerfile: string;
}

export interface IServiceConfig {
  [key: string]: {
    build?: IBuildConfig;
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
        external_network: boolean;
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
    key: zod.string(),
    value: zod.string(),
  }),
);

export const BuildSchema = zod.object({
  enabled: zod.boolean(),
  args: KV_Schema,
  context: zod.string().optional(),
  dockerfile: zod.string().optional(),
});

export const ServiceSchema = zod
  .object({
    name: zod.string().min(1, 'Name is required!'),
    build: BuildSchema,
    image: zod.string().nullable(),
    environment: KV_Schema,
    container_name: zod.string().nullable(),
    ports: zod.array(zod.object({ value: zod.string() })).nullable(),
    command: zod.string().optional().nullable(),
    volumes: zod.array(zod.object({ value: zod.string() })).nullable(),
    networks: zod.array(zod.object({ value: zod.string() })).nullable(),
    depends_on: zod.array(zod.object({ value: zod.string() })).nullable(),
  })
  .superRefine((data, ctx) => {
    if (!data.build.enabled && !data.image) {
      ctx.addIssue({
        path: ['image'],
        message: 'Image is required.',
        code: zod.ZodIssueCode.custom,
      });
    }

    if (data.build.enabled) {
      if (!data.build.context) {
        ctx.addIssue({
          path: ['build', 'context'],
          message: 'Context is required.',
          code: zod.ZodIssueCode.custom,
        });
      }
      if (!data.build.dockerfile) {
        ctx.addIssue({
          path: ['build', 'dockerfile'],
          message: 'Dockerfile is required.',
          code: zod.ZodIssueCode.custom,
        });
      }
    }
  });

const labelValueSchema = zod.object({
  label: zod.string(),
  value: zod.enum(['bridge', 'host', 'none', 'overlay']),
});

export const NetworkSchema = zod.union([
  zod.object({
    external_network: zod.literal(false),
    app_network: zod.array(
      zod.object({
        network_name: zod.string(),
        driver: labelValueSchema,
      }),
    ),
  }),
  zod.object({
    external_network: zod.literal(true),
    app_network: zod.array(
      zod.object({
        network_name: zod.string().min(1, 'Network name is required.'),
        name: zod.string().min(1, 'Name is required.'),
      }),
    ),
  }),
]);

export const DockerComposeSchema = zod.object({
  version: zod.string().min(1, 'Version is required.'),
  services: zod.array(ServiceSchema),
  networks: NetworkSchema,
});

export type TDockerCompose = zod.infer<typeof DockerComposeSchema>;

export type DockerCompose = {
  version: string;
  services: {
    [key: string]: {
      build: IBuildConfig | null;
      image: string | null;
      environment: {
        [key: string]: string;
      } | null;
      container_name: string | null;
      ports: string[] | null;
      command: string | null;
      volumes: string[] | null;
      networks: string[] | null;
      depends_on: string[] | null;
    };
  }[];
  networks: INetworkConfig | null;
};

type AppNetwork = {
  network_name: string;
  driver: {
    label: string;
    value: 'bridge' | 'host' | 'none' | 'overlay';
  };
};

type NetworkConfig = {
  name: string;
  network_name: string;
  external?: boolean;
};

export type CombinedNetworkType = AppNetwork | NetworkConfig;
