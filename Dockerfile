FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY run.py /app
COPY config.py /app
COPY __init__.py /app
COPY ./item /app
COPY ./user /app

CMD python run.py
