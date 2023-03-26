import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

import spacy
from spacy.tokens import DocBin
from spacy.training import Example
from spacy.cli.train import train
import pandas as pd
import json
import warnings

train_data = pd.read_csv('../../Data/NER_annotated_data/StackOverflow/train.txt', sep='\t', quoting=3)
train_data = train_data[(train_data['comp_label'] != 'O') & (train_data['word'].str.strip() != '"')]
train_data['word'] = train_data['word'].astype(str).str.strip().tolist()
train_data['comp_label'] = train_data['comp_label'].astype(str).str.strip().tolist()


# convert the groups into a list of tuples where each tuple contains the label and a list of words
data = [(label, word) for label, word in zip(train_data['comp_label'], train_data['word'])]

# convert the data into spaCy NER format
spacy_data = {"classes": ["SKILL"], "annotations": []}
for label, word in data:
    entities = []
    entities.append((0, len(word), label))
    spacy_data["annotations"].append((word, {"entities": entities}))

# write the spacy_data dictionary to a JSON file
with open('../../Data/NER_annotated_data/StackOverflow/annotations.json', 'w') as f:
    json.dump(spacy_data, f)

# Converting JSON dataset manually into spaCy doc bin format
with open("../../Data/NER_annotated_data/StackOverflow/annotations.json", "r") as f:
    data = json.load(f)

nlp = spacy.blank("en")
doc_bin = DocBin()

for i in range(len(data['annotations'])):
    if not data['annotations'][i]: continue
    text, annotations = data['annotations'][i]
    doc = nlp.make_doc(text.strip())
    ents = []
    for start, end, label in annotations["entities"]:
        span = doc.char_span(start, end, label=label)
        if span is None:
            msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
            warnings.warn(msg)
        else:
            ents.append(span)
    doc.ents = ents
    doc_bin.add(doc)

doc_bin.to_disk("../../Data/NER_annotated_data/StackOverflow/annotations.spacy")