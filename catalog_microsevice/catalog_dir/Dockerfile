FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python catalog_dir/manage.py runserver 0.0.0.0:8001