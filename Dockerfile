FROM python:2.7-alpine

RUN apk add --update build-base
RUN pip install zerorpc
RUN pip install requests

COPY . /evaluator
WORKDIR /evaluator
ENTRYPOINT ["python", "evaluator.py"]