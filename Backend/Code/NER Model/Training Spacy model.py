import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

# How to resume training without starting from scratch:
# https://stackoverflow.com/questions/70772641/how-to-resume-training-in-spacy-transformers-for-ner

# Run this line to rewrite config file. DO NOT RUN
#!python -m spacy init fill-config base_config.cfg config.cfg

import spacy
from spacy import displacy

SPACY_WORD_VECTORS_PATH = "./Models/"
nlp = spacy.load(SPACY_WORD_VECTORS_PATH)

# Only run this ONCE RIGHT AFTER the output config file from the Gensim Word2Vec notebook has been produced
# nlp.add_pipe("ner")
# nlp.to_disk("./Models/")

#!python -m spacy train ./Models/config.cfg --output . --paths.train ../../Data/NER_annotated_data/Job_Mod_Descriptions/mod_annotations.spacy --paths.dev ../../Data/NER_annotated_data/ChatGPT/annotations.spacy --paths.vectors ./Models/

# Model Evaluation
nlp_ner = spacy.load("model-best")

# Example Data
doc = nlp_ner(
    """
Data Analyst duties and responsibilities of the job

Data Analysts often make recommendations about the methods and ways in which a company obtains and analyses data to improve quality and the efficiency of data systems. A Data Analyst job description should include, but not be limited to:

Collecting and interpreting data
Analysing results
Reporting the results back to the relevant members of the business
Identifying patterns and trends in data sets
Working alongside teams within the business or the management team to establish business needs
Defining new data collection and analysis processes
Data Analyst job qualifications and requirements

A degree in the following subjects is beneficial in developing a career in data analysis:

Mathematics
Computer Science
Statistics
Economics
There are also a number of qualities to expect from a candidate to flourish in a Data Analyst role:

Experience in data models and reporting packages
Ability to analyse large datasets
Ability to write comprehensive reports
Strong verbal and written communication skills as Data Analysts do communicate with the wider business
An analytical mind and inclination for problem-solving
Attention to detail as data analysis and reporting must be precise
    """)
html_output = spacy.displacy.render(doc, style='ent')

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_output)