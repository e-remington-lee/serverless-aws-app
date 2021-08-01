import boto3
import json
import base64
import os

client = boto3.client("stepfunctions")

def lambda_handler(event, context):
    token_str = ""
    ipv4_str = ""
    decoded = {}
    return_me = {}
    name_str = ""
    extract_str = ""
    cell_str = ""
    return_me["message_str"] =  "Report processing, check your phone shortly"
    if "Authorization" in json.dumps(event):
        #i.e we are at the website and have a valid Bearer token passed
        token_str = event["params"]["header"]["Authorization"]
        print(token_str)
        extract_str = token_str.replace("Bearer ", "").strip().split(".")[1]
        print(f"Extracted token string: {extract_str}")
        extract_str += '=' * (-len(extract_str) % 4)
        print(f"Extracted token string after modification: {extract_str}")
        decoded = json.loads(base64.b64decode(extract_str))
        cell_str = decoded["phone_number"]
        name_str = decoded["cognito:username"]
        ipv4_str = event["params"]["header"]["X-Forwarded-For"]
        return_me["cell_str"] = cell_str
        return_me["name_str"] = name_str
        return_me["name_str"] = decoded["cognito:username"]
        return_me["ipv4_str"] = ipv4_str
        return_me["message_str"] = "Report Processed"
        if os.environ['STEP_ARN']:
            return spawn_step_function(return_me, os.environ['STEP_ARN'])
        else:
            print("testing in the console without a STEP function")
            return return_me
    else:
        print("testing in the console without AUTH")
        return return_me
    return return_me

def spawn_step_function(return_me, step_arn):
    payload={"cell_str": return_me["cell_str"], "ipv4_str": return_me["ipv4_str"]},
    payload_str = json.dumps(payload)
    print(client.start_execution(stateMachineArn=step_arn, input=payload_str))
    return return_me