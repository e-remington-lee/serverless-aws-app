import boto3
import json
import os
# from aws_xray_sdk.core import patch_all

# patch_all()

s3 = boto3.client('s3','us-east-2')
ssm = boto3.client('ssm', 'us-east-2')
bucket_name = os.environ['BUCKET_NAME']
file_name = os.environ['FILE_NAME']
# bucket_name = ssm.get_parameter( Name='erl-1482-dragon-data',WithDecryption=False)['Parameter']['Value']
# file_name = ssm.get_parameter( Name='dragon_stats_one.json',WithDecryption=False)['Parameter']['Value']

def listDragons(event, context):
    
    expression = "select * from s3object s"

    if 'queryStringParameters' in event and event['queryStringParameters'] is not None:
        if 'dragonName' in event['queryStringParameters']:
            expression = "select * from S3Object[*][*] s where s.dragon_name_str =  '" + event["queryStringParameters"]['dragonName'] + "'"
        if 'family' in event['queryStringParameters']:
            expression = "select * from S3Object[*][*] s where s.family_str =  '" + event["queryStringParameters"]['family'] + "'"

    result = s3.select_object_content(
            Bucket=bucket_name,
            Key=file_name,
            ExpressionType='SQL',
            Expression=expression,
            InputSerialization={'JSON': {'Type': 'Document'}},
            OutputSerialization={'JSON': {}}
    )
    
    records = ''
    for event in result['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
   
    return {
        "statusCode": 200,
        "body": json.dumps(records)
    }