import Argocd from './terraform-template/ARGOCD/argocd';
import Docker from './terraform-template/Docker/docker';
import EC2 from './terraform-template/EC2/ec2';
import IAM from './terraform-template/IAM/iam';
import S3 from './terraform-template/S3/s3';
import Installation from './installation/installation';
import Basic from './basic/basic';

export { Argocd, Docker, EC2, IAM, S3, Installation, Basic };
