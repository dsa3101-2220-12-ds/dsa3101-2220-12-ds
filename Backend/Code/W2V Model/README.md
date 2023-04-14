# File contents
1. Generating Gensim Word2Vec Word Embeddings.ipynb : This file consists of code to train the Word2Vec model to generate word embeddings that will be used to train the NER model. <b>WARNING: Training the Word2Vec model requires a very large dataset from Huggingface to be downloaded. If you have not downloaded it before, it can potentially take over an hour to download.</b>
2. w2v.model : This file stores the Word2Vec model. To improve the model or continue to train the model with more text data, you can load in this pre-trained model.
3. w2v.wordvectors : This file stores the word embeddings of every single word in the model's vocabulary set. You can view the contents of the file with a text editor, but do note that it is very huge.
