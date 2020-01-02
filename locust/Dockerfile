FROM python:3.8

WORKDIR /app/

RUN pip install locustio \
    --index-url http://mirrors.aliyun.com/pypi/simple/ \
    --trusted-host mirrors.aliyun.com

COPY locustfile.py .
