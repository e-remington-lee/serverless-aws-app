import boto3
import json
import os

s3 = boto3.client('s3')
g_bucket_name_str = os.environ['REPORT_BUCKET_NAME']
key_name_str = "report.html"

def handler(event, context):
    print("Getting presigned url")
    presigned_url_str = get_presigned_url_str()
    print(presigned_url_str)
    message_str = f"Here is your presigned url for your report: {presigned_url_str}"
    return message_str 

# print(s3.list_buckets())

def get_presigned_url_str():
    params={
        "Bucket":g_bucket_name_str,
        "Key":key_name_str,
    }
    print(params)
    return s3.generate_presigned_url("get_object", params)
