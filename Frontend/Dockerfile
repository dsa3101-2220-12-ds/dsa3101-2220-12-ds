FROM python:3.10.6-slim-buster

## directory on the image:
WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
ADD files files
ADD pages pages 
ADD assets assets

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python app.py

## Set the environment variable for the flask application here:
ENV FLASK_APP=app

ENTRYPOINT [ "python", "-u", "-m", "flask", "run", "--host=0.0.0.0"]
