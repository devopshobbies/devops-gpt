export interface BasicBody {
  max_tokens: number;
  min_tokens: number;
  service: string;
  input: string;
}

export interface BasicResponse {
  output: string;
}

export interface BasicMessage {
  role: string;
  content: string;
  loading?: boolean;
}
