export const getNestedValue = (obj: any, path: string) => {
  return path.split('.').reduce((acc, part) => acc && acc[part], obj);
};

export const convertKVtoObject = (
  kvArray: Array<{ key: string; value: string }>,
) => {
  return kvArray.reduce(
    (acc, curr) => {
      acc[curr.key] = curr.value;
      return acc;
    },
    {} as Record<string, string>,
  );
};

interface Service {
  name: string;
  [key: string]: any;
}

export const convertServicesToObject = (
  services: Service[],
): Record<string, Omit<Service, 'name'>> => {
  return services.reduce(
    (acc, service) => {
      const { name, ...serviceWithoutName } = service;
      acc[name] = serviceWithoutName;
      return acc;
    },
    {} as Record<string, Omit<Service, 'name'>>,
  );
};
