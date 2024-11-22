import {
  terraformArgocdMapper,
  terraformDockerMapper,
  terraformEC2Mapper,
  terraformIAMMapper,
  terraformS3Mapper,
} from "../../utils/mapperFunctions";
import {
  Endpoints,
  terraformArgocdDefaultValues,
  terraformDockerDefaultValues,
  terraformEc2DefaultValues,
  terraformIamDefaultValues,
  terraformS3DefaultValues,
  TerraformServices,
} from "../constants";
import {
  argocdFieldProperties,
  dockerFieldProperties,
  ec2FieldProperties,
  iamFieldProperties,
  s3FieldProperties,
} from "./constants";

type MapperFunction =
  | typeof terraformS3Mapper
  | typeof terraformArgocdMapper
  | typeof terraformDockerMapper
  | typeof terraformIAMMapper
  | typeof terraformEC2Mapper;

type DefaultValues =
  | typeof terraformS3DefaultValues
  | typeof terraformEc2DefaultValues
  | typeof terraformIamDefaultValues
  | typeof terraformArgocdDefaultValues
  | typeof terraformDockerDefaultValues;

type FieldProperies =
  | typeof dockerFieldProperties
  | typeof ec2FieldProperties
  | typeof argocdFieldProperties
  | typeof s3FieldProperties
  | typeof iamFieldProperties;

export interface PlatformData {
  serviceName: TerraformServices;
  defaultValues: DefaultValues;
  endpoint: Endpoints;
  mapperFunction: MapperFunction;
  fieldProperties: FieldProperies;
}
