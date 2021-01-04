FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY . /usr/src/app/
# COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/src/app

EXPOSE 8000

# CMD python manage.py migrate && gunicorn config.wsgi -b 0.0.0.0:8000
# CMD python manage.py runserver 0.0.0.0:8000
# ENTRYPOINT python manage.py migrate
CMD gunicorn config.wsgi -b 0.0.0.0:8000
# CMD ["python manage.py migrate", "gunicorn", "config.wsgi", "-b", "0.0.0.0:8000"]
