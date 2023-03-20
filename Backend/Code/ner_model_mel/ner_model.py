import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

import pandas as pd
import spacy
from spacy.training import Example
import multiprocessing as mp
import time

pd.set_option('display.max_rows', None)
start_time = time.time()

# import labelled ner train data
train_data = pd.read_csv('train.txt', sep='\t', quoting=3)
train_data = train_data[(train_data['comp_label'] != 'O') & (train_data['word'].str.strip() != '"')]
train_x = train_data['word'].astype(str).str.strip().tolist()
train_y = train_data['comp_label'].astype(str).str.strip().tolist()

test_data = pd.read_csv('test.txt', sep='\t', quoting=3)
test_data = test_data[(test_data['comp_label'] != 'O') & (test_data['word'].str.strip() != '"')]
test_x = test_data['word'].astype(str).str.strip().tolist()
test_y = train_data['comp_label'].astype(str).str.strip().tolist()

# import job description
job_data = pd.read_csv('../../Data/jobs/mycareersfuture_query-data_science.csv')
job_desc = job_data['Description']

# Load the small English language model
nlp = spacy.load("en_core_web_sm")

# Define the function to process a chunk of data
def process_chunk(chunk):
    examples = []
    for text, label in zip(chunk[0], chunk[1]):
        examples.append(Example.from_dict(nlp.make_doc(text), {'entities': [(0, len(str(text)), label)]}))
    return examples

# Split the data into chunks
n_chunks = mp.cpu_count()
chunk_size = len(train_x) // n_chunks
chunks = [(train_x[i:i+chunk_size], train_y[i:i+chunk_size]) for i in range(0, len(train_x), chunk_size)]

# Create a pool of worker processes and process the chunks in parallel
if __name__ == '__main__':
    mp.freeze_support()

    with mp.Pool(processes=n_chunks) as pool:
        examples = pool.map(process_chunk, chunks)

        # Flatten the list of examples
        examples = [example for chunk in examples for example in chunk]

        print("examples ", examples[:100])
        end_time = time.time()
        total_time = end_time - start_time
        print("finish train data example objects:", total_time)

        # Train the NER model
        ner = nlp.get_pipe('ner')

        # Add the labels to the NER model
        for y in set(train_y):
            ner.add_label(y)

        for example in examples:
            ner.update([example], drop=0.5)
        
        end_time = time.time()
        total_time = end_time - start_time
        print("finish tuning:", total_time)

        test_pred = [nlp(x) for x in test_x]
        print("test_pred ", test_pred)
        correct = 0
        print("len of test y", len(test_y))
        print("len of test pred", len(test_pred))
        # truncate the longer list to match the shorter list
        min_len = min(len(test_y), len(test_pred))
        test_y = test_y[:min_len]
        predict_y = test_pred[:min_len]

        for i in range(len(test_y)):
            if test_y[i] == test_pred[i]:
                correct += 1

        accuracy = correct / len(test_y) if len(test_y) > 0 else 0
        print("Accuracy: ", accuracy)
        end_time = time.time()
        total_time = end_time - start_time
        print("running test data:", total_time)
        