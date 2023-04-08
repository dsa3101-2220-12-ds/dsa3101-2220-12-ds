# import math
# import numpy as np
# from tqdm import tqdm
# import re
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# import spacy
# from gensim.models import Word2Vec
# import pandas as pd

# # import os
# # os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE' 

# # import pandas as pd
# # import numpy as np
# # import re
# # import math
# # import spacy
# # from tqdm import tqdm, trange
# # from gensim.models.phrases import Phrases, Phraser
# # from collections import defaultdict
# # import multiprocessing
# # from gensim.models import Word2Vec, KeyedVectors
# # from time import time
# # import matplotlib.pyplot as plt
# # import os
# # import string
# # import nltk
# # from nltk.stem import WordNetLemmatizer
# # from nltk.corpus import stopwords
# # import string
# # from datasets import load_dataset
# # from multiprocess import Process, cpu_count
# # import multiprocess as mp
# # import spacy
# # from spacy import displacy
# # import json
# import time

# start_time = time.time()

# # # pd.set_option('display.max_columns', None)
# # # pd.set_option('display.max_rows', None)
# # # pd.set_option('display.max_colwidth', None)

# W2V_MODEL_PATH = "../W2V Model/"
# NER_MODEL_PATH = "./model-best"

# CUSTOM_OPTIONS = {"colors" : {"SKILL" : "#78C0E0"}}

# w2v_model = Word2Vec.load(W2V_MODEL_PATH + "w2v.model")

# nlp_ner = spacy.load("model-best")

# # # with open('../../Data/skill_sch_code.json') as f:
# # #     skill_sch_code = json.load(f)

# skill_sch_code = modules_copy = pd.read_csv('../../Data/skill_sch_code.csv')
# modules_copy = pd.read_csv('../../../Data/university_courses/All_courses_info.csv')

# # # Gathering Module Database
# # # UNI_MODDESC_MAPPING = {

# # #     # Module desc ONLY - ernest original code
# # #     "nus_dsa_mods.xlsx" : "mod_desc",
# # #     "NTU_course_info.csv" : "Course Aims",
# # #     "SMU_course_info.csv" : "Description",
# # #     "SUSS_course_info.csv" : "module description",
# # #     "SUTD_course_info.csv" : "Module description",
# # #     "SIT_Module_Info.csv" : "Module Description "

# # #     #combined all topics to increase skills identified
# # #     # "nus_dsa_mods.xlsx" : "mod_desc",
# # #     # "NTU_course_info.csv" : "mod_desc",
# # #     # "SMU_course_info.csv" : "Description",
# # #     # "SUSS_course_info.csv" : "module description",
# # #     # "SUTD_course_info.csv" : "mod_desc",
# # #     # "SIT_Module_Info.csv" : "mod_desc"
# # # }

# # # UNI_MODCODE_MAPPING = {
# # #     "nus_dsa_mods.xlsx" : "mod_code",
# # #     "NTU_course_info.csv" : "Module Code",
# # #     "SMU_course_info.csv" : "Module Code",
# # #     "SUSS_course_info.csv" : "module code",
# # #     "SUTD_course_info.csv" : "Module code",
# # #     "SIT_Module_Info.csv" : "Module Code"
# # # }

# # # UNI_MODNAME_MAPPING = {
# # #     "nus_dsa_mods.xlsx" : "mod_name",
# # #     "NTU_course_info.csv" : "Module Name",
# # #     "SMU_course_info.csv" : "Module Name",
# # #     "SUSS_course_info.csv" : "module name",
# # #     "SUTD_course_info.csv" : "Module Title",
# # #     "SIT_Module_Info.csv" : "Module Title"
# # # }

# # # SKIP_ROWS = {
# # #     "nus_dsa_mods.xlsx" : 0,
# # #     "NTU_course_info.csv" : 0,
# # #     "SMU_course_info.csv" : 1,
# # #     "SUSS_course_info.csv" : 0,
# # #     "SUTD_course_info.csv" : 5,
# # #     "SIT_Module_Info.csv" : 0
# # # }

# # # MODULE_READ = "../../../Data/university_courses/"

# # # modules = pd.DataFrame([], dtype='object', columns = ["school", "code", "name", "description"])
# # # for uni, description_col in UNI_MODDESC_MAPPING.items():
# # #     school_name = uni.split("_")[0].upper()
# # #     print(f"Gathering module descriptions from {school_name}")
# # #     try:
# # #         table = pd.read_excel(MODULE_READ + uni, skiprows=SKIP_ROWS[uni])
# # #     except:
# # #         table = pd.read_csv(MODULE_READ + uni, skiprows=SKIP_ROWS[uni], encoding_errors='ignore')

# # #     table = table[[UNI_MODCODE_MAPPING[uni], UNI_MODNAME_MAPPING[uni], UNI_MODDESC_MAPPING[uni]]].dropna().reset_index(drop=True)
# # #     table.rename(columns = {
# # #         UNI_MODCODE_MAPPING[uni] : "code",
# # #         UNI_MODNAME_MAPPING[uni] : "name",
# # #         UNI_MODDESC_MAPPING[uni] : "description"
# # #     }, inplace=True)
# # #     table["school"] = school_name

# # #     modules = pd.concat([modules, table], axis = 0).reset_index(drop=True)

# # # modules.to_csv('../../../Data/university_courses/All_courses_info.csv', index=False)
# # # end_time = time.time()

# # # elapsed_time = end_time - start_time

# # # print(f"time to import libraries and files: {elapsed_time} seconds")

# # # Function for pre-processing data
# # HTML_PATTERN = re.compile('<.*?>')
# # STOP_WORDS = set(stopwords.words('english'))
# # lemmatizer = WordNetLemmatizer()

# # def cleaning(chunk): 
# #     # print(chunk)
# #     outputs = []
# #     for target_input in chunk:
# #         # convert to lower case
# #         target_input = target_input.lower()

# #         # remove websites
# #         target_input = re.sub(r'http\S+', ' ', target_input)

# #         # remove html tags
# #         target_input = re.sub(HTML_PATTERN, ' ', target_input)

# #         # remove all non-alphabets
# #         target_input = re.sub("[^A-Za-z']+", ' ', target_input)

# #         #will remove extra spaces
# #         target_input = re.sub(r'\s+',' ',target_input)

# #         # remove stopwords and lemmatize
# #         target_input_tokens = nltk.word_tokenize(target_input)
# #         target_input_tokens_wo_stopwords = [lemmatizer.lemmatize(i) for i in target_input_tokens if i not in STOP_WORDS and i]
# #         # print(target_input_tokens_wo_stopwords)
# #         outputs.append(target_input_tokens_wo_stopwords)
# #     # print(outputs)
# #     return outputs

# # # def cleaning(chunk): 
# # #     cleaned_chunk = [re.sub(r'http\S+', ' ', x.lower()) for x in chunk]
# # #     cleaned_chunk = [re.sub(HTML_PATTERN, ' ', x) for x in cleaned_chunk]
# # #     cleaned_chunk = [re.sub("[^A-Za-z']+", ' ', x) for x in cleaned_chunk]
# # #     cleaned_chunk = [re.sub(r'\s+',' ',x) for x in cleaned_chunk]
# # #     cleaned_chunk = [nltk.word_tokenize(x) for x in cleaned_chunk]
# # #     cleaned_chunk = [[lemmatizer.lemmatize(i) for i in tokens if i not in STOP_WORDS and i] for tokens in cleaned_chunk]
# # #     return cleaned_chunk


# # # OOV = []
# # # verbose = 1
# # # skill_sch_code = {} # {skill: {school : [module code 1, module code 2]}}


# # # for index, row in modules.iterrows():
# # #     school = row['school']
# # #     description = row['description']
# # #     mod_code = row['code']
# # #     mod_desc = nlp_ner(description)

# # #     for mod_ents in mod_desc.ents:
# # #         mod_ents = cleaning([mod_ents.text])[0]
# # #         for mod_ent in mod_ents:
# # #             if mod_ent not in w2v_model.wv:
# # #                 if mod_ent not in STOP_WORDS and mod_ent not in OOV:
# # #                     OOV.append(mod_ent)
# # #                 if verbose:
# # #                     print(f"MODULE: {mod_ent} not found in vocabulary")
# # #             else:
# # #                 # DICTIONARY
# # #                 if mod_ent in skill_sch_code:
# # #                     if school in skill_sch_code[mod_ent]:
# # #                         skill_sch_code[mod_ent][school].append(mod_code)
# # #                     else:
# # #                         skill_sch_code[mod_ent][school] = [mod_code]
# # #                 else:
# # #                     skill_sch_code[mod_ent] = {school: [mod_code]}

# # # # CSV FILE: Convert the nested dictionary to a DataFrame
# # # # convert nested dictionary to list of dictionaries
# # # rows = []
# # # for skill, school_codes in skill_sch_code.items():
# # #     for school, module_codes in school_codes.items():
# # #         rows.append({'skill': skill, 'school': school, 'modules': module_codes})

# # # # create DataFrame from list of dictionaries
# # # skill_sch_code_csv = pd.DataFrame(rows)

# # # skill_sch_code_csv.to_csv('../../Data/skill_sch_code.csv', index=False)
# # # end_time = time.time()

# # # elapsed_time = end_time - start_time

# # # print(f"time to make skill_sch_code dict: {elapsed_time} seconds")

# # # with open('../../Data/skill_sch_code.json', 'w') as f:
# # #     # Write the dictionary to the file in JSON format
# # #     json.dump(skill_sch_code, f)

# # # Functions for generating score
# # def calc_score(cos_sim):
# #     """
# #     Calculates a score from 0 to 100 given a cosine-similarity score that ranges from -1 to 1

# #     Details:
# #     Let A be the angle between two vectors u and v. In other words, cos_sim = cos(A)
# #     score = A/180 * 100
# #     """

# #     # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
# #     if cos_sim > 1: cos_sim = 1
# #     elif cos_sim < -1: cos_sim = -1

# #     return (math.pi - math.acos(cos_sim)) * 100 / math.pi

# # def process_job_desc(job_desc):
# #     job_desc = nlp_ner(job_desc)
# #     result = [cleaning([job_ents.text])[0] for job_ents in job_desc.ents]
# #     return result


# # # def get_doc2doc_score(job_desc, mod_desc, verbose = 1):
# # #     """
# # #     Computes the similarity score between two documents
# # #     """
# # #     # job_desc = nlp_ner(job_desc)
# # #     job_desc = process_job_desc
# # #     # mod_desc = nlp_ner(mod_desc) REMOVED
# # #     scores = []
# # #     OOV = [] # Stores out of vocabulary words

# # #     # for job_ents in job_desc.ents:
# # #     #     job_ents = cleaning([job_ents.text])[0]
# # #         # for job_ent in job_ents:
# # #     for job_ent in job_desc:
# # #         if job_ent not in w2v_model.wv: # If job_ent not found in vocabulary
# # #             if job_ent not in OOV and job_ent not in STOP_WORDS:
# # #                 OOV.append(job_ent)
# # #                 if verbose:
# # #                     print(f"JOB: {job_ent} not found in vocabulary")
# # #             scores.append(0)
# # #             continue
# # #         max_cossim = -1
# # #         best_mod_ent = None
# # #             # for mod_ents in mod_desc.ents:
# # #             #     mod_ents = cleaning([mod_ents.text])[0]
# # #             #     for mod_ent in mod_ents:
# # #             #         if mod_ent not in w2v_model.wv:
# # #             #             if mod_ent not in STOP_WORDS and mod_ent not in OOV:
# # #             #                 OOV.append(mod_ent)
# # #             #                 if verbose:
# # #             #                     print(f"MODULE: {mod_ent} not found in vocabulary")
# # #             #         else:

# # #         for mod_ent in skill_sch_code['skill'].unique():
# # #             cos_sim = w2v_model.wv.similarity(job_ent, mod_ent)

# # #             # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
# # #             if cos_sim > 1: cos_sim = 1
# # #             elif cos_sim < -1: cos_sim = -1

# # #             if cos_sim >= max_cossim:
# # #                 max_cossim = cos_sim
# # #                 best_mod_ent = mod_ent
# # #     if best_mod_ent == None:
# # #         if verbose:
# # #             print(f"No matching skills found for {job_ent} in {mod_desc}")
# # #         scores.append(0)
# # #     else:
# # #         score = calc_score(max_cossim)
# # #         scores.append(score)
# # #     return np.mean(np.array(scores))

# # def get_skill2mod_score(skill, mod_desc):
# #     """
# #     Generates a score and the skill token identified in `mod_desc` with the closest match to `skill`
# #     """
# #     # mod_desc = nlp_ner(mod_desc)
# #     max_score = 0
# #     best_ent = None
# #     if skill not in w2v_model.wv:
# #         return max_score, best_ent
# #     # for mod_ents in mod_desc.ents:
# #     #     mod_ents = cleaning([mod_ents.text])[0]
# #     #     for mod_ent in mod_ents:
# #     #         if mod_ent in w2v_model.wv:

# #     for mod_ent in skill_sch_code['skill'].unique():
# #         cos_sim = w2v_model.wv.similarity(mod_ent, skill)

# #         # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
# #         if cos_sim > 1: cos_sim = 1
# #         elif cos_sim < -1: cos_sim = -1

# #         score = calc_score(cos_sim)
# #         if max_score < score:
# #             best_ent = mod_ent
# #         max_score = max(max_score, score)
# #     else:
# #         max_score = max(max_score, 0)

# #     return max_score, best_ent

# # def get_school_scores(all_schools):
# #     """
# #     Assigns a score to every school. Score ranges from 0 to 100
# #     """
# #     all_scores = {}
# #     num_skills = len(all_schools)
# #     for skill in all_schools.keys():
# #         schools = all_schools[skill].keys()
# #         for school in schools:
# #             score = all_schools[skill][school][1]
# #             if school not in all_scores: all_scores[school] = 0
# #             all_scores[school] += score
# #     for school, total_score in all_scores.items():
# #         all_scores[school] = total_score / num_skills
# #     return all_scores


# # def get_mod_recommendations(job_desc):
# #     """
# #     WARNING: This function takes about 1-2 minutes to run
# #     Given a job description (JD), this function will identify all skills within the JD, 
# #     and recommend a module per school for each identified skill

# #     Input: Job description (str)
# #     Output: Module recommendations, School scores (dictionary D1 of the format below, dictionary D2 of the format below)

# #     Format of D1:
# #     {
# #         JD_skill_1 : {
# #             school_1 : (school_1_module, score_for_school_1_module),
# #             school_2 : (school_2_module, score_for_school_2_module),
# #             school_3 : (school_3_module, score_for_school_3_module),
# #             ...
# #         },
# #         JD_skill_2 : {
# #             school_1 : (school_1_module, score_for_school_1_module),
# #             school_2 : (school_2_module, score_for_school_2_module),
# #             school_3 : (school_3_module, score_for_school_3_module),
# #             ...
# #         },
# #         JD_skill_3 : {
# #             school_1 : (school_1_module, score_for_school_1_module),
# #             school_2 : (school_2_module, score_for_school_2_module),
# #             school_3 : (school_3_module, score_for_school_3_module),
# #             ...
# #         },
# #         ...
# #     }

# #     Format of D2:
# #     {
# #         school_1 : score,
# #         school_2 : score,
# #         school_3 : score,
# #         ...
# #     }
# #     """

# #     all_schools = {}
# #     job_desc = process_job_desc(job_desc)
# #     # for ent in tqdm(nlp_ner(job_desc).ents):
# #     for skill_words in job_desc:
# #         # skill_words = cleaning([ent.text])[0]
# #         best_mods = {}
# #         for skill_word in skill_words:
# #             # modules_copy = modules.copy()
# #             global modules_copy
# #             modules_copy['score'] = modules_copy.description.apply(lambda x: get_skill2mod_score(skill_word, x)[0])
# #             modules_copy = modules_copy.sort_values('score', ascending=False).drop_duplicates('school')
# #             for i, row in modules_copy.iterrows():
# #                 school, code, name, description, score = row
# #                 if school not in best_mods or best_mods[school][1]:
# #                     best_mods[school] = (code, score)
# #         all_schools[" ".join(skill_words)] = best_mods

# #     return all_schools, get_school_scores(all_schools)


# ###################### BACKEND TEAM ######################


# # W2V_MODEL_PATH = "/app/w2v/"
# # NER_MODEL_PATH = "/app/ner/"
# # w2v_model = Word2Vec.load(W2V_MODEL_PATH + "w2v.model")
# # nlp_ner = spacy.load(NER_MODEL_PATH)
# # skill_sch_code = modules_copy = pd.read_csv('/app/skill_sch_code.csv')
# # modules_copy = pd.read_csv('/app/All_courses_info.csv')

# # MODULES_DATASET_PATH = "/app/modules.pkl"
# # modules = pd.read_pickle(MODULES_DATASET_PATH)

# HTML_PATTERN = re.compile('<.*?>')
# STOP_WORDS = set(stopwords.words('english'))
# lemmatizer = WordNetLemmatizer()

# def cleaning(chunk):

#     # Importing libraries for parallelization later
#     import re
#     import nltk
#     from nltk.corpus import stopwords
#     from nltk.stem import WordNetLemmatizer
#     HTML_PATTERN = re.compile('<.*?>')
#     STOP_WORDS = set(stopwords.words('english'))
#     lemmatizer = WordNetLemmatizer()

#     outputs = []
#     for target_input in chunk:
#         # convert to lower case
#         target_input = target_input.lower()

#         # remove websites
#         target_input = re.sub(r'http\S+', ' ', target_input)

#         # remove html tags
#         target_input = re.sub(HTML_PATTERN, ' ', target_input)

#         # remove all non-alphabets
#         target_input = re.sub("[^A-Za-z']+", ' ', target_input)

#         #will remove extra spaces
#         target_input = re.sub(r'\s+',' ',target_input)

#         # remove stopwords and lemmatize
#         target_input_tokens = nltk.word_tokenize(target_input)
#         target_input_tokens_wo_stopwords = [lemmatizer.lemmatize(i) for i in target_input_tokens if i not in STOP_WORDS and i]

#         outputs.append(target_input_tokens_wo_stopwords)
#     return outputs

# def calc_score(cos_sim):
#     """
#     Calculates a score from 0 to 100 given a cosine-similarity score that ranges from -1 to 1

#     Details:
#     Let A be the angle between two vectors u and v. In other words, cos_sim = cos(A)
#     score = A/180 * 100
#     """

#     # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
#     if cos_sim > 1: cos_sim = 1
#     elif cos_sim < -1: cos_sim = -1

#     return (math.pi - math.acos(cos_sim)) * 100 / math.pi

# def get_doc2doc_score(job_desc, mod_desc, verbose = 1):
#     """
#     Computes the similarity score between two documents
#     """
#     job_desc = nlp_ner(job_desc)
#     mod_desc = nlp_ner(mod_desc)
#     scores = []
#     OOV = [] # Stores out of vocabulary words

#     for job_ents in job_desc.ents:
#         job_ents = cleaning([job_ents.text])[0]
#         for job_ent in job_ents:
#             if job_ent not in w2v_model.wv: # If job_ent not found in vocabulary
#                 if job_ent not in OOV and job_ent not in STOP_WORDS:
#                     OOV.append(job_ent)
#                     if verbose:
#                         print(f"JOB: {job_ent} not found in vocabulary")
#                 scores.append(0)
#                 continue
#             max_cossim = -1
#             best_mod_ent = None
#             for mod_ents in mod_desc.ents:
#                 mod_ents = cleaning([mod_ents.text])[0]
#                 for mod_ent in mod_ents:
#                     if mod_ent not in w2v_model.wv:
#                         if mod_ent not in STOP_WORDS and mod_ent not in OOV:
#                             OOV.append(mod_ent)
#                             if verbose:
#                                 print(f"MODULE: {mod_ent} not found in vocabulary")
#                     else:
#                         cos_sim = w2v_model.wv.similarity(job_ent, mod_ent)

#                         # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
#                         if cos_sim > 1: cos_sim = 1
#                         elif cos_sim < -1: cos_sim = -1

#                         if cos_sim >= max_cossim:
#                             max_cossim = cos_sim
#                             best_mod_ent = mod_ent
#                 if best_mod_ent == None:
#                     if verbose:
#                         print(f"No matching skills found for {job_ent} in {mod_desc}")
#                     scores.append(0)
#                 else:
#                     score = calc_score(max_cossim)
#                     scores.append(score)

#     return np.mean(np.array(scores))

# def get_skill2mod_score(skill, mod_skill):
#     """
#     Generates a score and the skill token identified in `mod_desc` with the closest match to `skill`
#     """
#     max_score = 0
#     best_ent = None
#     if skill not in w2v_model.wv:
#         return max_score, best_ent

#     unq_skill_sch_code = skill_sch_code['skill'].unique()
#     for mod_ent in unq_skill_sch_code:
#         cos_sim = w2v_model.wv.similarity(mod_ent, skill)

#         # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
#         if cos_sim > 1: cos_sim = 1
#         elif cos_sim < -1: cos_sim = -1

#         score = calc_score(cos_sim)
#         if max_score < score:
#             best_ent = mod_ent
#         max_score = max(max_score, score)
#     else:
#         max_score = max(max_score, 0)

#     return max_score, best_ent

# def get_mod_recommendations(job_desc):
#     """
#     WARNING: This function takes about 1-2 minutes to run
#     Given a job description (JD), this function will identify all skills within the JD, 
#     and recommend a module per school for each identified skill

#     Input: Job description (str)
#     Output: Module recommendations, School scores (dictionary D1 of the format below, dictionary D2 of the format below)

#     Format of D1:
#     {
#         JD_skill_1 : {
#             school_1 : (school_1_module, score_for_school_1_module),
#             school_2 : (school_2_module, score_for_school_2_module),
#             school_3 : (school_3_module, score_for_school_3_module),
#             ...
#         },
#         JD_skill_2 : {
#             school_1 : (school_1_module, score_for_school_1_module),
#             school_2 : (school_2_module, score_for_school_2_module),
#             school_3 : (school_3_module, score_for_school_3_module),
#             ...
#         },
#         JD_skill_3 : {
#             school_1 : (school_1_module, score_for_school_1_module),
#             school_2 : (school_2_module, score_for_school_2_module),
#             school_3 : (school_3_module, score_for_school_3_module),
#             ...
#         },
#         ...
#     }

#     Format of D2:
#     {
#         school_1 : score,
#         school_2 : score,
#         school_3 : score,
#         ...
#     }
#     """

#     global skill_sch_code
#     all_schools = {}
#     job_desc_ents = nlp_ner(job_desc).ents
#     for ent in tqdm(job_desc_ents):
#         skill_words = cleaning([ent.text])[0]
#         best_mods = {}
#         for skill_word in skill_words:
#             # modules_copy['score'] = modules_copy.description.apply(lambda x: get_skill2mod_score(skill_word)[0])
#             modules_copy['score'] = np.vectorize(lambda x: get_skill2mod_score(skill_word, x)[0])(skill_sch_code)
#             # score_list = []
#             # for x in modules_copy.description:
#             #     score_list.append(get_skill2mod_score(skill_word)[0])
#             # modules_copy['score'] = score_list
#             modules_copy = modules_copy.sort_values('score', ascending=False).drop_duplicates('school')
#             for i, row in modules_copy.iterrows():
#                 school, code, name, description, score = row
#                 if school not in best_mods or best_mods[school][1]:
#                     best_mods[school] = (code, score)
#         all_schools[" ".join(skill_words)] = best_mods

#     print("get_mod_recc", all_schools, get_school_scores(all_schools))
#     return all_schools, get_school_scores(all_schools)

# def get_school_scores(all_schools):
#     """
#     Assigns a score to every school. Score ranges from 0 to 100
#      """
#     all_scores = {}
#     num_skills = len(all_schools)
#     for skill in all_schools.keys():
#         schools = all_schools[skill].keys()
#         for school in schools:
#             score = all_schools[skill][school][1]
#             if school not in all_scores: all_scores[school] = 0
#             all_scores[school] += score
#     for school, total_score in all_scores.items():
#         all_scores[school] = total_score / num_skills
#     return all_scores

# job_desc = "SQL, Computer Vision, Database, Engineering, Linear Programming"

# mod_reco, school_scores = get_mod_recommendations(job_desc)
# print(mod_reco)
# print(school_scores)
# print(time.time() - start_time)

import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import pandas as pd
import numpy as np
import re
import math
import spacy
from tqdm import tqdm, trange
from gensim.models.phrases import Phrases, Phraser
from collections import defaultdict
import multiprocessing
from gensim.models import Word2Vec, KeyedVectors
from time import time
import matplotlib.pyplot as plt
import os
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
# from datasets import load_dataset
from multiprocess import Process, cpu_count
import multiprocess as mp
import spacy
from spacy import displacy
import time

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

start_time = time.time()

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth', None)

W2V_MODEL_PATH = "../W2V Model/"
NER_MODEL_PATH = "./model-best"

CUSTOM_OPTIONS = {"colors": {"SKILL": "#78C0E0"}}

w2v_model = Word2Vec.load(W2V_MODEL_PATH + "w2v.model")

nlp_ner = spacy.load("model-best")

# with open('../../Data/skill_sch_code.json') as f:
#     skill_sch_code = json.load(f)

skill_sch_code = modules_copy = pd.read_csv('../../Data/skill_sch_code.csv')
modules_copy = pd.read_csv('../../../Data/university_courses/All_courses_info.csv')

# Gathering Module Database
# UNI_MODDESC_MAPPING = {

#     # Module desc ONLY - ernest original code
#     "nus_dsa_mods.xlsx" : "mod_desc",
#     "NTU_course_info.csv" : "Course Aims",
#     "SMU_course_info.csv" : "Description",
#     "SUSS_course_info.csv" : "module description",
#     "SUTD_course_info.csv" : "Module description",
#     "SIT_Module_Info.csv" : "Module Description "

#     #combined all topics to increase skills identified
#     # "nus_dsa_mods.xlsx" : "mod_desc",
#     # "NTU_course_info.csv" : "mod_desc",
#     # "SMU_course_info.csv" : "Description",
#     # "SUSS_course_info.csv" : "module description",
#     # "SUTD_course_info.csv" : "mod_desc",
#     # "SIT_Module_Info.csv" : "mod_desc"
# }

# UNI_MODCODE_MAPPING = {
#     "nus_dsa_mods.xlsx" : "mod_code",
#     "NTU_course_info.csv" : "Module Code",
#     "SMU_course_info.csv" : "Module Code",
#     "SUSS_course_info.csv" : "module code",
#     "SUTD_course_info.csv" : "Module code",
#     "SIT_Module_Info.csv" : "Module Code"
# }

# UNI_MODNAME_MAPPING = {
#     "nus_dsa_mods.xlsx" : "mod_name",
#     "NTU_course_info.csv" : "Module Name",
#     "SMU_course_info.csv" : "Module Name",
#     "SUSS_course_info.csv" : "module name",
#     "SUTD_course_info.csv" : "Module Title",
#     "SIT_Module_Info.csv" : "Module Title"
# }

# SKIP_ROWS = {
#     "nus_dsa_mods.xlsx" : 0,
#     "NTU_course_info.csv" : 0,
#     "SMU_course_info.csv" : 1,
#     "SUSS_course_info.csv" : 0,
#     "SUTD_course_info.csv" : 5,
#     "SIT_Module_Info.csv" : 0
# }

# MODULE_READ = "../../../Data/university_courses/"

# modules = pd.DataFrame([], dtype='object', columns = ["school", "code", "name", "description"])
# for uni, description_col in UNI_MODDESC_MAPPING.items():
#     school_name = uni.split("_")[0].upper()
#     print(f"Gathering module descriptions from {school_name}")
#     try:
#         table = pd.read_excel(MODULE_READ + uni, skiprows=SKIP_ROWS[uni])
#     except:
#         table = pd.read_csv(MODULE_READ + uni, skiprows=SKIP_ROWS[uni], encoding_errors='ignore')

#     table = table[[UNI_MODCODE_MAPPING[uni], UNI_MODNAME_MAPPING[uni], UNI_MODDESC_MAPPING[uni]]].dropna().reset_index(drop=True)
#     table.rename(columns = {
#         UNI_MODCODE_MAPPING[uni] : "code",
#         UNI_MODNAME_MAPPING[uni] : "name",
#         UNI_MODDESC_MAPPING[uni] : "description"
#     }, inplace=True)
#     table["school"] = school_name

#     modules = pd.concat([modules, table], axis = 0).reset_index(drop=True)

# modules.to_csv('../../../Data/university_courses/All_courses_info.csv', index=False)
# end_time = time.time()

# elapsed_time = end_time - start_time

# print(f"time to import libraries and files: {elapsed_time} seconds")

# Function for pre-processing data
HTML_PATTERN = re.compile('<.*?>')
STOP_WORDS = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def cleaning(chunk):
    # print(chunk)
    outputs = []
    for target_input in chunk:
        # convert to lower case
        target_input = target_input.lower()

        # remove websites
        target_input = re.sub(r'http\S+', ' ', target_input)

        # remove html tags
        target_input = re.sub(HTML_PATTERN, ' ', target_input)

        # remove all non-alphabets
        target_input = re.sub("[^A-Za-z']+", ' ', target_input)

        # will remove extra spaces
        target_input = re.sub(r'\s+', ' ', target_input)

        # remove stopwords and lemmatize
        target_input_tokens = nltk.word_tokenize(target_input)
        target_input_tokens_wo_stopwords = [lemmatizer.lemmatize(i) for i in target_input_tokens if
                                            i not in STOP_WORDS and i]
        # print(target_input_tokens_wo_stopwords)
        outputs.append(target_input_tokens_wo_stopwords)
    # print(outputs)
    return outputs


# def cleaning(chunk):
#     cleaned_chunk = [re.sub(r'http\S+', ' ', x.lower()) for x in chunk]
#     cleaned_chunk = [re.sub(HTML_PATTERN, ' ', x) for x in cleaned_chunk]
#     cleaned_chunk = [re.sub("[^A-Za-z']+", ' ', x) for x in cleaned_chunk]
#     cleaned_chunk = [re.sub(r'\s+',' ',x) for x in cleaned_chunk]
#     cleaned_chunk = [nltk.word_tokenize(x) for x in cleaned_chunk]
#     cleaned_chunk = [[lemmatizer.lemmatize(i) for i in tokens if i not in STOP_WORDS and i] for tokens in cleaned_chunk]
#     return cleaned_chunk


# OOV = []
# verbose = 1
# skill_sch_code = {} # {skill: {school : [module code 1, module code 2]}}


# for index, row in modules.iterrows():
#     school = row['school']
#     description = row['description']
#     mod_code = row['code']
#     mod_desc = nlp_ner(description)

#     for mod_ents in mod_desc.ents:
#         mod_ents = cleaning([mod_ents.text])[0]
#         for mod_ent in mod_ents:
#             if mod_ent not in w2v_model.wv:
#                 if mod_ent not in STOP_WORDS and mod_ent not in OOV:
#                     OOV.append(mod_ent)
#                 if verbose:
#                     print(f"MODULE: {mod_ent} not found in vocabulary")
#             else:
#                 # DICTIONARY
#                 if mod_ent in skill_sch_code:
#                     if school in skill_sch_code[mod_ent]:
#                         skill_sch_code[mod_ent][school].append(mod_code)
#                     else:
#                         skill_sch_code[mod_ent][school] = [mod_code]
#                 else:
#                     skill_sch_code[mod_ent] = {school: [mod_code]}

# # CSV FILE: Convert the nested dictionary to a DataFrame
# # convert nested dictionary to list of dictionaries
# rows = []
# for skill, school_codes in skill_sch_code.items():
#     for school, module_codes in school_codes.items():
#         rows.append({'skill': skill, 'school': school, 'modules': module_codes})

# # create DataFrame from list of dictionaries
# skill_sch_code_csv = pd.DataFrame(rows)

# skill_sch_code_csv.to_csv('../../Data/skill_sch_code.csv', index=False)
# end_time = time.time()

# elapsed_time = end_time - start_time

# print(f"time to make skill_sch_code dict: {elapsed_time} seconds")

# with open('../../Data/skill_sch_code.json', 'w') as f:
#     # Write the dictionary to the file in JSON format
#     json.dump(skill_sch_code, f)

# Functions for generating score
def calc_score(cos_sim):
    """
    Calculates a score from 0 to 100 given a cosine-similarity score that ranges from -1 to 1
    
    Details:
    Let A be the angle between two vectors u and v. In other words, cos_sim = cos(A)
    score = A/180 * 100
    """

    # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
    if cos_sim > 1:
        cos_sim = 1
    elif cos_sim < -1:
        cos_sim = -1

    return (math.pi - math.acos(cos_sim)) * 100 / math.pi


def process_job_desc(job_desc):
    job_desc = nlp_ner(job_desc)
    result = [cleaning([job_ents.text])[0] for job_ents in job_desc.ents]
    return result


# def get_doc2doc_score(job_desc, mod_desc, verbose = 1):
#     """
#     Computes the similarity score between two documents
#     """
#     # job_desc = nlp_ner(job_desc)
#     job_desc = process_job_desc
#     # mod_desc = nlp_ner(mod_desc) REMOVED
#     scores = []
#     OOV = [] # Stores out of vocabulary words

#     # for job_ents in job_desc.ents:
#     #     job_ents = cleaning([job_ents.text])[0]
#         # for job_ent in job_ents:
#     for job_ent in job_desc:
#         if job_ent not in w2v_model.wv: # If job_ent not found in vocabulary
#             if job_ent not in OOV and job_ent not in STOP_WORDS:
#                 OOV.append(job_ent)
#                 if verbose:
#                     print(f"JOB: {job_ent} not found in vocabulary")
#             scores.append(0)
#             continue
#         max_cossim = -1
#         best_mod_ent = None
#             # for mod_ents in mod_desc.ents:
#             #     mod_ents = cleaning([mod_ents.text])[0]
#             #     for mod_ent in mod_ents:
#             #         if mod_ent not in w2v_model.wv:
#             #             if mod_ent not in STOP_WORDS and mod_ent not in OOV:
#             #                 OOV.append(mod_ent)
#             #                 if verbose:
#             #                     print(f"MODULE: {mod_ent} not found in vocabulary")
#             #         else:

#         for mod_ent in skill_sch_code['skill'].unique():
#             cos_sim = w2v_model.wv.similarity(job_ent, mod_ent)

#             # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
#             if cos_sim > 1: cos_sim = 1
#             elif cos_sim < -1: cos_sim = -1

#             if cos_sim >= max_cossim:
#                 max_cossim = cos_sim
#                 best_mod_ent = mod_ent
#     if best_mod_ent == None:
#         if verbose:
#             print(f"No matching skills found for {job_ent} in {mod_desc}")
#         scores.append(0)
#     else:
#         score = calc_score(max_cossim)
#         scores.append(score)
#     return np.mean(np.array(scores))

def get_skill2mod_score(skill, mod_desc):
    """
    Generates a score and the skill token identified in `mod_desc` with the closest match to `skill`
    """
    # mod_desc = nlp_ner(mod_desc)
    max_score = 0
    best_ent = None
    if skill not in w2v_model.wv:
        return max_score, best_ent
    # for mod_ents in mod_desc.ents:
    #     mod_ents = cleaning([mod_ents.text])[0]
    #     for mod_ent in mod_ents:
    #         if mod_ent in w2v_model.wv:

    for mod_ent in skill_sch_code['skill'].unique():
        cos_sim = w2v_model.wv.similarity(mod_ent, skill)

        # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
        if cos_sim > 1:
            cos_sim = 1
        elif cos_sim < -1:
            cos_sim = -1

        score = calc_score(cos_sim)
        if max_score < score:
            best_ent = mod_ent
        max_score = max(max_score, score)
    else:
        max_score = max(max_score, 0)

    return max_score, best_ent


def get_school_scores(all_schools):
    """
    Assigns a score to every school. Score ranges from 0 to 100
    """
    all_scores = {}
    num_skills = len(all_schools)
    for skill in all_schools.keys():
        schools = all_schools[skill].keys()
        for school in schools:
            score = all_schools[skill][school][1]
            if school not in all_scores: all_scores[school] = 0
            all_scores[school] += score
    for school, total_score in all_scores.items():
        all_scores[school] = total_score / num_skills
    return all_scores


def get_mod_recommendations(job_desc):
    """
    WARNING: This function takes about 1-2 minutes to run
    Given a job description (JD), this function will identify all skills within the JD, 
    and recommend a module per school for each identified skill
    
    Input: Job description (str)
    Output: Module recommendations, School scores (dictionary D1 of the format below, dictionary D2 of the format below)
    
    Format of D1:
    {
        JD_skill_1 : {
            school_1 : (school_1_module, score_for_school_1_module),
            school_2 : (school_2_module, score_for_school_2_module),
            school_3 : (school_3_module, score_for_school_3_module),
            ...
        },
        JD_skill_2 : {
            school_1 : (school_1_module, score_for_school_1_module),
            school_2 : (school_2_module, score_for_school_2_module),
            school_3 : (school_3_module, score_for_school_3_module),
            ...
        },
        JD_skill_3 : {
            school_1 : (school_1_module, score_for_school_1_module),
            school_2 : (school_2_module, score_for_school_2_module),
            school_3 : (school_3_module, score_for_school_3_module),
            ...
        },
        ...
    }
    
    Format of D2:
    {
        school_1 : score,
        school_2 : score,
        school_3 : score,
        ...
    }
    """

    all_schools = {}
    job_desc = process_job_desc(job_desc)
    global modules_copy
    # for ent in tqdm(nlp_ner(job_desc).ents):
    for skill_words in job_desc:
        # skill_words = cleaning([ent.text])[0]
        best_mods = {}
        for skill_word in skill_words:
            # modules_copy = modules.copy()
            global modules_copy
            modules_copy['score'] = modules_copy.description.apply(lambda x: get_skill2mod_score(skill_word, x)[0])
            modules_copy = modules_copy.sort_values('score', ascending=False).drop_duplicates('school')
            for i, row in modules_copy.iterrows():
                school, code, name, description, score = row
                if school not in best_mods or best_mods[school][1]:
                    best_mods[school] = (code, score)
        all_schools[" ".join(skill_words)] = best_mods

    return all_schools, get_school_scores(all_schools)


job_desc = """
SQL
"""

mod_reco, school_scores = get_mod_recommendations(job_desc)
print(mod_reco)
print(school_scores)

end_time = time.time()

elapsed_time = end_time - start_time

print(f"time to generate score: {elapsed_time} seconds")
