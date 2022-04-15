# syntax=docker/dockerfile:1
FROM python:3.9.9
WORKDIR /opt
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
RUN mkdir -p /opt/logs
ENTRYPOINT [ "./entrypoint.sh" ]
