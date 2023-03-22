# RUN THIS IN COMMAND LINE: bash train_NER.sh
python -m spacy train config.cfg --output ./ --paths.train ./../../Data/NER_annotated_data/StackOverflow/train.spacy --paths.dev ./../../Data/NER_annotated_data/StackOverflow/dev.spacy

