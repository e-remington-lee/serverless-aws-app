import boto3
from botocore.client import Config
import json
import os
import datetime

'''
https://github.com/boto/boto3/issues/1982
bug when not using default us-east-1 region, can be realized when the signed_url has erl-2021-08-01-s3site.s3.amazonaws.com
BUT the link was redirecting to erl-2021-08-08-s3site.s3.us-east-2.amazonaws.com, regions like that can show up in odd ways!
'''
s3 = boto3.client('s3', region_name="us-east-2", config=Config(s3={'addressing_style': 'path'}))
g_bucket_name_str = os.environ['REPORT_BUCKET_NAME']
key_name_str = "report.html"

def handler(event, context):
    print("Getting presigned url")
    presigned_url_str = get_presigned_url_str()
    print(presigned_url_str)
    message_str = f"Here is your presigned url for your report: {presigned_url_str}"
    response={"message_str": message_str}
    return response 

# print(s3.list_buckets())

def get_presigned_url_str():
    params={
        "Bucket":g_bucket_name_str,
        "Key":key_name_str
    }
    print(params)
    return s3.generate_presigned_url("get_object", Params=params, ExpiresIn=120)
