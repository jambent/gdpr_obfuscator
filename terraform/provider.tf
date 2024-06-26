provider "aws" {
  region  = "eu-west-2"
}

terraform {
  backend "s3" {
    bucket = "gdpr-obfuscator-backend"
    key    = "application.tfstate"
    region = "eu-west-2"
  }
}