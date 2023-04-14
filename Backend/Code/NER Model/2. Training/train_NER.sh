# RUN THIS IN COMMAND LINE: bash train_NER.sh
python -m spacy train "./../Training Pipeline/config.cfg" --output ./../ --paths.train ../../../Data/NER_annotated_data/Job_Mod_Descriptions/mod_annotations.spacy --paths.dev ../../../Data/NER_annotated_data/ChatGPT/annotations.spacy --paths.vectors "./../Training Pipeline/"
