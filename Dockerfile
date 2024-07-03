FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /dpt

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
