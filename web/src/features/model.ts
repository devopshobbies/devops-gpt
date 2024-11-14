import { UserType } from "./constants";

export interface Message {
  user: UserType;
  content: string;
}

export interface BasicGenFormData {
  minToken: number;
  maxToken: number;
  service: string;
  input: string;
}
