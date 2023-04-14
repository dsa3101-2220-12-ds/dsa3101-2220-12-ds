# Folder contents
1. <b>Generating Gensim Word2Vec Word Embeddings.ipynb</b> : This file consists of code to train the Word2Vec model to generate word embeddings that will be used to train the NER model. <b>WARNING: Training the Word2Vec model requires a very large dataset from Huggingface to be downloaded. If you have not downloaded it before, it can potentially take over an hour to download.</b>
2. <b>w2v.model</b> : This file stores the Word2Vec model. To improve the model or continue to train the model with more text data, you can load in this pre-trained model.
3. <b>w2v.wordvectors</b> : This file stores the word embeddings of every single word in the model's vocabulary set. You can view the contents of the file with a text editor, but do note that it is very huge.
