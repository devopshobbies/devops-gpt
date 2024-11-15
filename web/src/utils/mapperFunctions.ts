import {
  BasicGenFormData,
  ApiRequestBasicGen,
  BugFixFormData,
  ApiRequestBugFix,
} from "../features/model";

export const basicGenMapper = (data: BasicGenFormData): ApiRequestBasicGen => ({
  min_token: data.minToken,
  max_token: data.maxToken,
  service: data.service,
  input: data.input,
  requestId: "",
});

export const bugFixMapper = (data: BugFixFormData): ApiRequestBugFix => ({
  min_token: data.minToken,
  max_token: data.maxToken,
  bug_description: data.bugDescription,
  service: data.service,
  version: data.version,
  requestId: "",
});
