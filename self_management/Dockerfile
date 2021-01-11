FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY . /usr/src/app/

RUN pip install -r requirements.txt
# RUN python manage.py collectstatic 
WORKDIR /usr/src/app

EXPOSE 8000

CMD gunicorn config.wsgi -b 0.0.0.0:8000
# CMD ["python manage.py migrate", "gunicorn", "config.wsgi", "-b", "0.0.0.0:8000"]
