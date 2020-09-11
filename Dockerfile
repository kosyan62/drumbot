FROM python:3.6.9

RUN apt-get update && apt-get install -y\
    lilypond

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD python3 /app/bot.py
