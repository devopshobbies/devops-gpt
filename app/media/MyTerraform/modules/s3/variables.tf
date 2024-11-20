
variable "s3_create_bucket" {
  type = bool
}

variable "s3_bucket_name" {
  type = string
}

variable "s3_bucket_force_destroy" {
  type = bool
}

variable "s3_bucket_tags" {
  type = map(string)
}

variable "s3_create_bucket_versioning" {
  type = bool
}

variable "s3_bucket_versioning_status" {
  type = string
}
