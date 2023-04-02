FROM python:3.10.6-slim-buster

## directory on the image:
WORKDIR /app

COPY requirements.txt requirements.txt
COPY mock_API.py mock_API.py

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

########################## Edited by Ernest ##########################

COPY modules.pkl modules.pkl
COPY ner/ ner/
COPY w2v/ w2v/
COPY skill_sch_code.csv skill_sch_code.csv
COPY All_courses_info.csv All_courses_info.csv

RUN python -c "import nltk;nltk.download('stopwords')"
RUN python -c "import nltk;nltk.download('punkt')"
RUN python -c "import nltk;nltk.download('wordnet')"

######################################################################

## Set the environment variable for the flask application here:
ENV FLASK_APP=mock_API


ENTRYPOINT [ "python", "-u", "-m", "flask", "run", "--host=0.0.0.0"]
# python -u -m flask run --host=0.0.0.0