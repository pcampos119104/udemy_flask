FROM python:3.7-slim
COPY . /app
WORKDIR /app/code

RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
