FROM python:3.10

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install requests pika
RUN pip freeze > requirements.txt 

CMD python data_manipulation.py