# RUN THIS IN COMMAND LINE: bash train_NER.sh
python -m spacy train config.cfg --output ./ --paths.train ./train.spacy --paths.dev ./train.spacy

