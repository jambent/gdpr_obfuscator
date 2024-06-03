data "aws_caller_identity" "current" {}

data "archive_file" "gdpr_obfuscator_lambda" {
  type        = "zip"
  source_dir = "${path.module}/../aws_infrastructure_for_testing/src"
  output_path = "${path.module}/../aws_infrastructure_for_testing/lambda_code_zip_files/gdpr_obfuscator_lambda_code.zip"
}