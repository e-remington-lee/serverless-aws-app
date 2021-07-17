import boto3
import os
from packages import add

print(add(1,2))
# client = boto3.client('s3')
boto3.client
client = boto3.client("sts", aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name='us-east-2')
response=client.get_caller_identity()

# response=client.list_objects(Bucket='aws-bma-test')

print(response)