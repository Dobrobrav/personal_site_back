FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/web

#COPY ./requirements.txt /usr/src/web/requirements.txt
COPY . /usr/src/web
RUN pip install -r /usr/src/web/requirements.txt

#RUN python manage.py makemigrations
#RUN python manage.py migrate


EXPOSE 8000
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]