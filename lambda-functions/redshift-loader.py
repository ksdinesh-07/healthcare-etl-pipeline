import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    client = boto3.client('redshift-data')
    
    copy_sql = """
        COPY healthcare.visits
        FROM 's3://healthcare-etl-pipelin-ks/daily-visits/'
        IAM_ROLE 'arn:aws:iam::${ACCOUNT_ID}:role/redshift-s3-glue-role'
        CSV
        IGNOREHEADER 1
    """
    
    try:
        response = client.execute_statement(
            WorkgroupName='healthcare-workgroup',
            Database='healthcare_db',
            Sql=copy_sql
        )
        logger.info(f"COPY started: {response['Id']}")
        return {'statusCode': 200, 'body': json.dumps({'message': 'COPY started'})}
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
