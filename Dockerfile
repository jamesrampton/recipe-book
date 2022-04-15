# syntax=docker/dockerfile:1
FROM python:3.9.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN set -x \
    && BUILD_DEPS=" \
    build-essential \
    libpq-dev \
    git \
    " \
    && apt-get update \
    && apt-get install -y --no-install-recommends $BUILD_DEPS

WORKDIR /opt

COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
RUN mkdir -p /opt/logs
ENTRYPOINT [ "./entrypoint.sh" ]
