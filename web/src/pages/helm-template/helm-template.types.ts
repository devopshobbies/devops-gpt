export interface HelmTemplateBody {
  api_version: number;
  pods: Pod[];
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

export interface Pod {
  name: string;
  image: string;
  target_port: number | null;
  replicas: number | null;
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
}
