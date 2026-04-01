terraform {
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "healthcare_data" {
  bucket = "healthcare-etl-pipelin-ks"
}

resource "aws_sns_topic" "alerts" {
  name = "healthcare-etl-alerts"
}

resource "aws_glue_crawler" "fact_crawler" {
  name          = "healthcare-fact-crawler"
  database_name = "healthcare_db"
  role          = aws_iam_role.glue_role.name
  
  s3_target { path = "s3://${aws_s3_bucket.healthcare_data.bucket}/daily-visits/" }
}

resource "aws_iam_role" "glue_role" {
  name = "glue-healthcare-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "glue.amazonaws.com" }
    }]
  })
}

output "s3_bucket" { value = aws_s3_bucket.healthcare_data.bucket }
output "sns_topic" { value = aws_sns_topic.alerts.arn }
