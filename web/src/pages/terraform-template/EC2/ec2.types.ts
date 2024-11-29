export interface EC2Body {
  key_pair: boolean;
  security_group: boolean;
  aws_instance: boolean;
  ami_from_instance: boolean;
}

export interface EC2Response {
  output: string;
}
