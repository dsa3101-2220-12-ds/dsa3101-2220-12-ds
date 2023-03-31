FROM python:3.10.6-slim-buster

## directory on the image:
WORKDIR /app

COPY requirements.txt requirements.txt
COPY mock_API.py mock_API.py

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# RUN python mock_API.py

## Set the environment variable for the flask application here:
ENV FLASK_APP=mock_API

ENTRYPOINT [ "python", "-u", "-m", "flask", "run", "--host=0.0.0.0"]
