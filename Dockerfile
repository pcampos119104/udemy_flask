FROM python:3.7-slim
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

WORKDIR /app/code
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
