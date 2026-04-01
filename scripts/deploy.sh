#!/bin/bash
set -e

echo "🚀 Deploying Healthcare ETL Pipeline..."

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
BUCKET="healthcare-etl-pipelin-ks"

# Create S3 bucket
aws s3 mb s3://$BUCKET --region us-east-1 || true

# Upload data
aws s3 cp data/dim/ s3://$BUCKET/dim/ --recursive
aws s3 cp data/daily-visits/ s3://$BUCKET/daily-visits/ --recursive

# Create SNS topic
aws sns create-topic --name healthcare-etl-alerts
aws sns subscribe --topic-arn arn:aws:sns:us-east-1:$ACCOUNT_ID:healthcare-etl-alerts \
    --protocol email --notification-endpoint ks.dinesh005@gmail.com

echo "✅ Deployment complete!"
