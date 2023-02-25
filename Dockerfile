FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/web

COPY ./requirements.txt /usr/src/web
RUN pip install -r /usr/src/web/requirements.txt



EXPOSE 8000