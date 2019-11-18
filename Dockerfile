FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY run.py /app
COPY config.py /app
COPY __init__.py /app
COPY ./item /app/item
COPY ./user /app/user

CMD python run.py
