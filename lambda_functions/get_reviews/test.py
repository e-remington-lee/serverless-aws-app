import boto3
import json
s3 = boto3.client('s3')
S3_BUCKET = 'aws-tc-largeobjects'
S3_FILE = 'DEV-AWS-MO-Building_2.0/my_json_lines.jsonl'

r = s3.select_object_content(
    Bucket=S3_BUCKET,
    Key=S3_FILE,
    ExpressionType='SQL',
    Expression="select s.review_headline, s.review_body, s.star_rating from s3object[*] s where s.product_id = 'B00WBJGUA2'",
    InputSerialization={'JSON': {"Type": "Lines"}},
    OutputSerialization={'JSON': {}}
)

all_reviews_list = []
helper_format_str = ""
for event in r['Payload']:
    if 'Records' in event:
        helper_format_str = event['Records']['Payload'].decode('utf-8')
        helper_format_str = helper_format_str.replace("review_headline", "review_headline_str").replace("review_body", "review_body_str")
        all_reviews_list = helper_format_str.splitlines()
            
result_list = []
for review_chunk in all_reviews_list:
    result_list.append(json.loads(review_chunk))
# for x in r['Payload']:
#     print(x)
print(result_list)