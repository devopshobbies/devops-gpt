import { Checkboxprops } from "../../components/internal-ui/CheckBox";
import {
  terraformArgocdMapper,
  terraformDockerMapper,
  terraformEC2Mapper,
  terraformIAMMapper,
  terraformS3Mapper,
} from "../../utils/mapperFunctions";
import {
  terraformDockerDefaultValues,
  Endpoints,
  terraformEc2DefaultValues,
  terraformS3DefaultValues,
  terraformIamDefaultValues,
  TerraformDockerFields,
  TerraformEC2Fields,
  TerraformS3Fields,
  TerraformIAMFields,
  TerraformArgocdFields,
  terraformArgocdDefaultValues,
} from "../constants";

const dockerFieldProperties: Checkboxprops[] = [
  {
    fieldName: TerraformDockerFields.DOCKER_IMAGE,
    label: "Docker Image",
  },
  {
    fieldName: TerraformDockerFields.DOCKER_CONTAINER,
    label: "Docker Container",
  },
];

const ec2FieldProperties: Checkboxprops[] = [
  {
    fieldName: TerraformEC2Fields.KEY_PAIR,
    label: "Key pair",
  },
  {
    fieldName: TerraformEC2Fields.SECURITY_GROUP,
    label: "Security group",
  },
  {
    fieldName: TerraformEC2Fields.AWS_INSTANCE,
    label: "AWS instance",
  },
  {
    fieldName: TerraformEC2Fields.AMI_FROM_INSTANCE,
    label: "AMI from instance",
  },
];

const s3FieldProperties: Checkboxprops[] = [
  {
    fieldName: TerraformS3Fields.S3_BUCKET,
    label: "S3 bucker",
  },
  {
    fieldName: TerraformS3Fields.BUCKET_VERSIONING,
    label: "Bucker versioning",
  },
];

const iamFieldProperties: Checkboxprops[] = [
  {
    fieldName: TerraformIAMFields.IAM_USER,
    label: "IAM user",
  },
  {
    fieldName: TerraformIAMFields.IAM_GROUP,
    label: "IAM group",
  },
];

const argocdFieldProperties: Checkboxprops[] = [
  {
    fieldName: TerraformArgocdFields.AUTO_PRUNE,
    label: "Auto prune",
  },
  {
    fieldName: TerraformArgocdFields.SELF_HEAL,
    label: "Self heal",
  },
  {
    fieldName: TerraformArgocdFields.APPLY_OUT_OF_SYNC_ONLY,
    label: "Apply out of sync only",
  },
  {
    fieldName: TerraformArgocdFields.CREATE_NAMESPACE,
    label: "Create namespace",
  },
  {
    fieldName: TerraformArgocdFields.FAIL_OR_SHARE_RESOURCE,
    label: "Fail or share resource",
  },
  {
    fieldName: TerraformArgocdFields.ARGOCD_REPOSITORY,
    label: "ARGOCD repository",
  },
  {
    fieldName: TerraformArgocdFields.ARGOCD_CLUSTER,
    label: "ARGOCD cluster",
  },
];

export const platformData = [
  {
    serviceName: "ARGOCD",
    defaultValues: terraformArgocdDefaultValues,
    endpoint: Endpoints.POST_IAC_ARGOCD,
    mapperFunction: terraformArgocdMapper,
    fieldProperties: argocdFieldProperties,
  },
  {
    serviceName: "DOCKER",
    defaultValues: terraformDockerDefaultValues,
    endpoint: Endpoints.POST_IAC_T_DOCKER,
    mapperFunction: terraformDockerMapper,
    fieldProperties: dockerFieldProperties,
  },
  {
    serviceName: "EC2",
    defaultValues: terraformEc2DefaultValues,
    endpoint: Endpoints.POST_IAC_T_EC2,
    mapperFunction: terraformEC2Mapper,
    fieldProperties: ec2FieldProperties,
  },
  {
    serviceName: "S3",
    defaultValues: terraformS3DefaultValues,
    endpoint: Endpoints.POST_IAC_T_S3,
    mapperFunction: terraformS3Mapper,
    fieldProperties: s3FieldProperties,
  },
  {
    serviceName: "IAM",
    defaultValues: terraformIamDefaultValues,
    endpoint: Endpoints.POST_IAC_T_IAM,
    mapperFunction: terraformIAMMapper,
    fieldProperties: iamFieldProperties,
  },
];
