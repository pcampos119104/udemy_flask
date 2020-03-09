
# Udemy Flask

Course that I've taken from Udemy [REST APIs with Flask and Python ](https://www.udemy.com/course/rest-api-flask-and-python/), plus Docker and deploy on Google Cloud Run.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Deployment

For running in a local machine, install the requirements.txt and run app.py
```
$ pip install requirements.txt
$ python3 app.py
```
You can deploy using Docker:
```
$ docker build -t udemy-flask .
```
Publish the image on [Google Cloud Registry](https://cloud.google.com/container-registry/docs/quickstart)
Publish on [Google Cloud Run ](https://cloud.google.com/run/docs/quickstarts/build-and-deploy)

Or even directly on Google Cloud Run
```
[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)
```

## Tests
The app can be tested with Postman, it is not automatic.
Download [Postman](https://www.postman.com/downloads/)
Import the files on folder test.
Run the different endpoints

## Built With
Python 3
Flask
Flask-JWT-Extended
Flask-RESTful
Flask-SQLAlchemy
Werkzeug
SQLite
