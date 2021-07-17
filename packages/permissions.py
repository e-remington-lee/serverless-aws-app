import boto3
import os

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "erl-2021-07-17-s3site"

policy_file = open(f"{os.getcwd()}\\resources\\security_policy.json", "r")
print(policy_file)

S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("DONE")