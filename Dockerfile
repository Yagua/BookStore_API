FROM python:3.10.6-alpine3.16

WORKDIR /usr/src/bookstore_app

# avoid python create .pyc cache files
ENV PYTHONDONTWRITEBYTECODE 1
# send python logs to containers
ENV PYTHONUNBUFFERED 1

RUN apk add -u mariadb-connector-c-dev zlib-dev jpeg-dev gcc musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
