import Argocd from './terraform-template/ARGOCD/argocd';
import Docker from './terraform-template/Docker/docker';
import EC2 from './terraform-template/EC2/ec2';
import IAM from './terraform-template/IAM/iam';
import S3 from './terraform-template/S3/s3';
import Installation from './installation/installation';
import Basic from './basic/basic';
import BugFix from './bug-fix/bug-fix';
import HelmTemplate from './helm-template/helm-template';

export {
  Argocd,
  Docker,
  EC2,
  IAM,
  S3,
  Installation,
  Basic,
  BugFix,
  HelmTemplate,
};
