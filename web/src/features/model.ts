import { UserType } from "./constants";

export interface Message {
  user: UserType;
  content: string;
  id: string;
}

export interface BasicGenFormData {
  minToken: number;
  maxToken: number;
  service: string;
  input: string;
}

export interface ApiRequestBasicGen {
  min_token: number;
  max_token: number;
  service: string;
  input: string;
  requestId: string;
}
