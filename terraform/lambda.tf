resource "aws_lambda_function" "gdpr_obfuscator" {
  function_name = var.gdpr_obfuscator
  role          = aws_iam_role.gdpr_obfuscator_lambda_role.arn
  s3_bucket     = aws_s3_bucket.gdpr_obfuscator_lambda_code_bucket.id
  s3_key        = aws_s3_object.gdpr_obfuscator_lambda_code.key
  handler       = "lambda_handler.lambda_handler"
  runtime       = "python3.11"
  timeout       = 60
  layers = [
            aws_lambda_layer_version.obfsc8_layer.arn,
            aws_lambda_layer_version.boto3_layer.arn
        ]
}


resource "aws_lambda_layer_version" "obfsc8_layer" {
  filename   = "${path.module}/../aws_lambda_layers/obfsc8_layer.zip"
  layer_name = "obfsc8_layer"

  compatible_runtimes = ["python3.11"]
}

resource "aws_lambda_layer_version" "boto3_layer" {
  filename   = "${path.module}/../aws_lambda_layers/boto3_layer.zip"
  layer_name = "boto3_layer"

  compatible_runtimes = ["python3.11"]
}