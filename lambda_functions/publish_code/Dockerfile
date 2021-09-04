FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py . 
# REMEMBER TO UPDATE CMD TO POINT TO APP.PY IN THE WORKDIR
CMD ["/app/app.lambda_handler"]