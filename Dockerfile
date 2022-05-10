# syntax=docker/dockerfile:1
FROM python:3.8 AS app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

FROM python:3.8 AS celery
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install celery redis
COPY . /app/
