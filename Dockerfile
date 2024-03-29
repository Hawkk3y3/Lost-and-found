FROM python:3.6

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN chmod u+x ./entrypoint.sh
RUN chmod u+x ./run_celery.sh
