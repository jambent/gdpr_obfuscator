resource "aws_s3_bucket" "gdpr_obfuscator_lambda_code_bucket" {
  bucket_prefix = "gdpr-obfuscator-lambda-code-bucket-"
  force_destroy = true
}

resource "aws_s3_bucket" "gdpr_obfuscator_source_data_bucket" {
  bucket_prefix = "gdpr-obfuscator-source-data-bucket-"
  force_destroy = true
}

resource "aws_s3_bucket" "gdpr_obfuscator_destination_bucket" {
  bucket_prefix = "gdpr-obfuscator-destination-bucket-"
  force_destroy = true
}



resource "aws_s3_object" "gdpr_obfuscator_lambda_code" {
  key    = "gdpr_obfuscator_lambda_code.zip"
  source = "${path.module}/../aws_infrastructure_for_testing/lambda_code_zip_files/gdpr_obfuscator_lambda_code.zip"
  bucket = aws_s3_bucket.gdpr_obfuscator_lambda_code_bucket.id
}