FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY APIStart.py /app
COPY DBhandler.py /app
COPY Items.py /app
COPY playground.py /app
COPY User.py /app

CMD python APIStart.py
