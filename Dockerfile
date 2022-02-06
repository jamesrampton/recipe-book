# syntax=docker/dockerfile:1
FROM python:3.9.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
WORKDIR /opt
RUN mkdir -p /opt/logs
COPY requirements.txt /opt/
RUN pip install -r requirements.txt
COPY . /opt/
