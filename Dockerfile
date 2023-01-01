FROM python:3.4
RUN mkdir /app && cd /app 

WORKDIR /app
COPY bazi.py /app

CMD python3 bazi.py
