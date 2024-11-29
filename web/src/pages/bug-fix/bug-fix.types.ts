export interface BugFixBody {
  max_tokens: number;
  min_tokens: number;
  service: string;
  version: string;
  bug_description: string;
}

export interface BugFixResponse {
  output: string;
}

export interface BugFixMessage {
  role: string;
  content: string;
  loading?: boolean;
}
