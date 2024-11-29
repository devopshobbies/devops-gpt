export interface HelmTemplateBody {
  api_version: number;
  pods: [
    {
      name: string;
      image: string;
      target_port: number;
      replicas: number;
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
    },
  ];
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
