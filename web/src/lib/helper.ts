import { IServiceConfig } from '@/pages/docker-compose/docker-compose.type';

export const getNestedValue = (obj: any, path: string) => {
  return path.split('.').reduce((acc, part) => acc && acc[part], obj);
};

export const convertKVtoObject = (
  kvArray: Array<{ key: string; value: string } | null> | null,
) => {
  return kvArray?.reduce(
    (acc, curr) => {
      if (curr && acc) {
        acc[curr.key] = curr?.value;
      }
      return acc;
    },
    {} as { [key: string]: string } | null,
  );
};

interface Service {
  name: string;
  [key: string]: any;
}

export const convertServicesToObject = (
  services: Service[],
): IServiceConfig => {
  return services.reduce((acc, service) => {
    const { name, ...serviceWithoutName } = service;
    acc[name] = serviceWithoutName as IServiceConfig[string];
    return acc;
  }, {} as IServiceConfig);
};
