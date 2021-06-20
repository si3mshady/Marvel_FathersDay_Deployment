FROM public.ecr.aws/lambda/python:3.8

WORKDIR /var/task

RUN pip install requests

COPY app.py .

CMD ["app.handler"] 

