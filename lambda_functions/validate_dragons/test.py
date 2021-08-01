import boto3
import json
import os

s3 = boto3.client('s3','us-east-2')
ssm = boto3.client('ssm', 'us-east-2')
bucket_name="erl-1482-dragon-data"
file_name="dragon_stats_one.json"

def validate():
    
    result = s3.select_object_content(
        Bucket=bucket_name,
        Key=file_name,
        ExpressionType='SQL',
        Expression=f"select * from S3Object[*][*] s where s.dragon_name_str = 'Dexler'",
        InputSerialization={'JSON': {'Type': 'Document'}},
        OutputSerialization={'JSON': {}}
    )
    
    # print(result['Payload'])
    # for x in result["Payload"]:
    #     print(x)
        
    for records in result['Payload']:
        if 'Records' in records:
            raise DragonValidationException("Duplicate dragon reported")
        return 'Dragon Validated'

class DragonValidationException(Exception):
    def __init__(self, *args, **kwargs):
        self.message=args[0] if args else None

    def __str__(self):
        if self.message:
            return f'DragonValidationException, {self.message}'
        else:
            return "DragonValidationException has been raised"
validate()