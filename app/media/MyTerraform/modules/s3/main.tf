
resource "aws_s3_bucket" "s3_bucket" {
  count         = var.s3_create_bucket ? 1 : 0
  bucket        = var.s3_bucket_name
  force_destroy = var.s3_bucket_force_destroy
  tags          = var.s3_bucket_tags
}

resource "aws_s3_bucket_versioning" "s3_bucket_versioning" {
  count = var.s3_create_bucket && var.s3_create_bucket_versioning ? 1 : 0
  bucket = aws_s3_bucket.s3_bucket[0].id

  versioning_configuration {
    status = var.s3_bucket_versioning_status
  }
}
