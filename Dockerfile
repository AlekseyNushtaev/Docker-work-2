FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir  --upgrade -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000


