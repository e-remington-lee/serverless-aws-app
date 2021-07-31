import boto3
import json

def handler(event, context):
    print(context)

    return {
        "headers":{"Context-Type": "application/json"},
        "statusCode": 200,
        "body": json.dumps({"message": "Lambda container test working",
                            "event": event})
    }
