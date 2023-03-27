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
What a College Intern - Data Science does at HP:
Attached to the "Smart Manufacturing Application and Research Center".
Work with an enterprising team of data scientists and build solutions to track, analyze and visualize the manufacturing and outbound quality of our supplies.
Generate deep insights through the analysis of data and understanding of operational processes and turn them into actionable recommendations.
Develop methodologies for optimizing our business processes through data visualization, real-time monitoring, predictive analytics etc.
Are you a high-performer? We are looking for an individual with:
Studying Bachelor’s degree in Computer Science, Business Analytics, Information Systems, Industrial Engineering, Statistics with good experience in programming.
Excellent analytical thinking, programming (using R/Python is desirable), and problem-solving skills.
Knowledge of data analytics, data warehousing, database management (preferably using SQL) and data visualization using RShiny and Plotly.
Fundamental knowledge of statistics and probability.
Good visualization skills to create real-time dashboards and/or reports to inform trends and insights.
    """)
html_output = spacy.displacy.render(doc, style='ent')

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_output)