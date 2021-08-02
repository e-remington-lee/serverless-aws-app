import boto3
import json
import base64
import os

safe_cellphone_str = os.environ['PHONE']
safe_ipv4_str = os.environ['IPV4']
def handler(event, context):
    print(event['cellphone_str'], event['ipv4_str'])
    if event['cellphone_str'] and event['ipv4_str']:
        if event['cellphone_str'] == safe_cellphone_str and event['ipv4_str']==safe_ipv4_str:
            response={"success": True}
            return response
    return f"Invalid {event['cellphone_str']}, {event['ipv4_str']}"