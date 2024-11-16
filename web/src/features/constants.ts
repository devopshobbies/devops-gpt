export enum BasicGenFields {
  MIN_TOKEN = "minToken",
  MAX_TOKEN = "maxToken",
  SERVICE = "service",
  INPUT = "input",
}

export enum BugFixFields {
  MIN_TOKEN = "minToken",
  MAX_TOKEN = "maxToken",
  SERVICE = "service",
  VERSION = "version",
  BUG_DESCRIPTION = "bugDescription",
}

export enum UserType {
  USER = "user",
  BOT = "bot",
}

export enum ENDPOINTS {
  postBasic = "/IaC-basic",
  postFix = "/IaC-bugfix",
  postInstall = "/IaC-install",
  PostIacTemp = "/IaC-template",
  PostIacHelm = "/Helm-template",
  getDonwload = "/download",
  getDirectory = "/list-directory",
}

export const basicGenDefaultValues = {
  minToken: 100,
  maxToken: 500,
  service: "terraform",
  input: undefined,
};

export const bugFixDefaultValues = {
  minToken: 100,
  maxToken: 500,
  service: "terraform",
  version: "latest",
  bugDescription: undefined,
};
