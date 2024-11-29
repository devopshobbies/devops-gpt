export interface InstallationBody {
  os: string;
  service: string;
}

export interface InstallationResponse {
  output: string;
}

export interface InstallationValidationError {
  detail: [
    {
      type: string;
      loc: string[];
      msg: string;
      input: string;
      ctx: {
        error: {};
      };
    },
  ];
}
