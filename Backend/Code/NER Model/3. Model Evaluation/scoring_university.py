import math
import numpy as np
from tqdm import tqdm
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import spacy
from gensim.models import Word2Vec
import pandas as pd
import time

start_time = time.time()

W2V_MODEL_PATH = "./../../W2V Model/"
NER_MODEL_PATH = "./../model-best"
w2v_model = Word2Vec.load(W2V_MODEL_PATH + "w2v.model")
nlp_ner = spacy.load(NER_MODEL_PATH)
modules = pd.read_csv('./../../../Data/modules/All_courses_info.csv')

HTML_PATTERN = re.compile('<.*?>')
STOP_WORDS = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def cleaning(chunk):
    
    # Importing libraries for parallelization later
    import re
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    HTML_PATTERN = re.compile('<.*?>')
    STOP_WORDS = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
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

        #will remove extra spaces
        target_input = re.sub(r'\s+',' ',target_input)

        # remove stopwords and lemmatize
        target_input_tokens = nltk.word_tokenize(target_input)
        target_input_tokens_wo_stopwords = [lemmatizer.lemmatize(i) for i in target_input_tokens if i not in STOP_WORDS and i]
        
        outputs.append(target_input_tokens_wo_stopwords)
    
    return outputs

def calc_score(cos_sim):
    """
    Calculates a score from 0 to 100 given a cosine-similarity score that ranges from -1 to 1
    
    Details:
    Let A be the angle between two vectors u and v. In other words, cos_sim = cos(A)
    score = A/180 * 100
    """
    
    # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
    if cos_sim > 1: cos_sim = 1
    elif cos_sim < -1: cos_sim = -1
    
    return (math.pi - math.acos(cos_sim)) * 100 / math.pi

def get_skill2mod_score(skill, mod_skills):
    """
    Generates a score and the skill token identified in `mod_desc` with the closest match to `skill`
    """
    # mod_desc = nlp_ner(mod_desc)
    max_score = 0
    best_ent = None
    if skill not in w2v_model.wv:
        return max_score, best_ent
    # for mod_ents in mod_desc.ents:
    mod_skills = mod_skills.strip("[]").replace("'", "").split(", ")
    for mod_ent in mod_skills:
        # mod_ents = cleaning([mod_ents.text])[0]
        # for mod_ent in mod_ents:
        #     if mod_ent in w2v_model.wv:
        if mod_ent in w2v_model.wv:
            cos_sim = w2v_model.wv.similarity(mod_ent, skill)
                    
            # To handle computational rounding errors. Sometimes cos_sim is 1.00001 or -1.00001
            if cos_sim > 1: cos_sim = 1
            elif cos_sim < -1: cos_sim = -1
                        
            score = calc_score(cos_sim)
            # skill_sch_code['skill_score'] = skill_sch_code.apply(lambda row: (skill, score) if row['skill'] == mod_ent else row['skill_score'], axis=1)
    
            # skill_sch_code['skill_score'] = np.where(skill_sch_code['skill'] == skill, [skill, score], skill_sch_code['skill_score'])

            if max_score < score:
                best_ent = mod_ent
            max_score = max(max_score, score)
        else:
            max_score = max(max_score, 0)
    # print(max_score, best_ent)
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
    global modules
    job_ents = nlp_ner(job_desc).ents
    for ent in tqdm(job_ents):
        skill_words = cleaning([ent.text])[0]
        best_mods = {}
        for skill_word in skill_words:
            modules_copy = modules.copy()
            modules_copy['score'] = modules_copy['skills'].apply(lambda x: get_skill2mod_score(skill_word, x)[0])
            modules_copy = modules_copy.sort_values('score', ascending=False).drop_duplicates('school')
            for i, row in modules_copy.iterrows():
                school, code, skills, score = row
                if school not in best_mods or best_mods[school][1]:
                    best_mods[school] = (code, score)
        all_schools[" ".join(skill_words)] = best_mods
    
    return all_schools, get_school_scores(all_schools)

job_desc = """
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
"""

mod_reco, school_scores = get_mod_recommendations(job_desc)
print(mod_reco)
print(school_scores)

end_time = time.time()

elapsed_time = end_time - start_time

print(f"time to generate score: {elapsed_time} seconds")