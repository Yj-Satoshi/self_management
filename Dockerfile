FROM python:3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /var/run/gunicorn

EXPOSE 8001

CMD ["gunicorn", "config.wsgi", "--bind=unix:/run/gunicorn/gunicorn.sock"]
