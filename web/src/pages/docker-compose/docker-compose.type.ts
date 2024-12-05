import { z } from 'zod';

const BuildArgsSchema = z.record(z.string(), z.string());

export const BuildSchema = z.object({
  args: BuildArgsSchema,
  context: z.string(),
  dockerfile: z.string(),
});

export const ServiceSchema = z.object({
  build: BuildSchema,
  command: z.string().optional(),
  container_name: z.string(),
  depends_on: z.array(z.string()),
  environment: z.record(z.string(), z.string()),
  image: z.string(),
  networks: z.array(z.string()),
  ports: z.array(z.string()),
  volumes: z.array(z.string()),
});

export const NetworkSchema = z.object({
  driver: z.string(),
});

export const DockerComposeSchema = z.object({
  version: z.string(),
  services: z.record(z.string(), ServiceSchema),
  networks: z.record(z.string(), NetworkSchema),
});

export type DockerComposeSchema = z.infer<typeof DockerComposeSchema>;
export type ServiceType = z.infer<typeof ServiceSchema>;
