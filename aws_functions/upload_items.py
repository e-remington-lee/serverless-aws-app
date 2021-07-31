import boto3
import os
S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "erl-2021-07-17-s3site"
# bucket_name = "aws-dragons"

html="text/html"
jpg="image/jpg"
js="application/js"
css="text/css"
png="image/png"

files=[]
for (dirpath, dirnames, filenames) in os.walk(f"{os.getcwd()}/resources/website/"):
    files.extend(filenames)

# def put_file(filename, suffix):
#    abs_path = f"{os.getcwd()}/resources/website/{filename}"
#    print(filename)
#    print(abs_path)
#    S3API.upload_file(abs_path, bucket_name, filename, ExtraArgs={'ContentType': suffix, "CacheControl": "max-age=0"}) 

# for f in files:
#     if f.endswith(".html"):
#         put_file(f, html)
#     elif f.endswith(".jpg"):
#         put_file(f, jpg)
#     elif f.endswith(".js"):
#         put_file(f, js)
#     elif f.endswith(".css"):
#         put_file(f, css)
#     elif f.endswith(".png"):
#         put_file(f, png)

filename="config.js"
abs_path = f"{os.getcwd()}/resources/website/{filename}"
print(filename)
print(abs_path)
S3API.upload_file(abs_path, bucket_name, filename, ExtraArgs={'ContentType': "application/js", "CacheControl": "max-age=0"}) 

print ("DONE")