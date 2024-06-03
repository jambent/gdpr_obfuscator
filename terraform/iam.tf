data "aws_iam_policy_document" "assume_role_document" {
  statement {

    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }

}


data "aws_iam_policy_document" "s3_document" {
  statement {

    actions = [
      "s3:*Object",
      "s3:ListBucket"
    ]
    resources = [
      "${aws_s3_bucket.gdpr_obfuscator_lambda_code_bucket.arn}/*",
      "${aws_s3_bucket.gdpr_obfuscator_source_data_bucket.arn}/*",
      "${aws_s3_bucket.gdpr_obfuscator_destination_bucket.arn}/*",
    ]
  }
}

resource "aws_iam_policy" "s3_policy" {
  name_prefix = "s3-policy-"
  policy      = data.aws_iam_policy_document.s3_document.json
}


resource "aws_iam_role" "gdpr_obfuscator_lambda_role" {
  name_prefix        = "role-${var.gdpr_obfuscator}"
  assume_role_policy = data.aws_iam_policy_document.assume_role_document.json
}

resource "aws_iam_role_policy_attachment" "gdpr_obfuscator_s3_policy_attachment" {
  role       = aws_iam_role.gdpr_obfuscator_lambda_role.name
  policy_arn = aws_iam_policy.s3_policy.arn
}