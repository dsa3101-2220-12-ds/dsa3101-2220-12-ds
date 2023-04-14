import random
from flask import Flask, request, jsonify

app = Flask(__name__)

###################### BACKEND TEAM ######################

import math
import numpy as np
from tqdm import tqdm
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import spacy
from gensim.models import Word2Vec
import pandas as pd

W2V_MODEL_PATH = "/app/w2v/"
NER_MODEL_PATH = "/app/ner/"
w2v_model = Word2Vec.load(W2V_MODEL_PATH + "w2v.model")
nlp_ner = spacy.load(NER_MODEL_PATH)


modules = pd.read_csv('/app/All_courses_info.csv')

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

##########################################################

CUSTOM_OPTIONS = {"colors" : {"SKILL" : "#78C0E0"}}

def html_format(paragraph):
    result = spacy.displacy.render(nlp_ner(paragraph), style = 'ent', jupyter=False, options = CUSTOM_OPTIONS)
    return result

def school_score():
    schools = ['SUTD', 'NTU', 'SMU', 'SUSS', 'SIT', 'NUS']
    scores = {school: round(random.uniform(80, 100), 1) for school in schools}
    return scores

def mod_reco():
    skills = ['data analytics', 'math']
    schools = ['SUTD', 'NTU', 'SMU', 'SUSS', 'SIT', 'NUS']
    modules = ['DSA1101', 'CZ2006', 'MKTG228', 'ANL355', 'CSC3004', 'DSA2102']
    reco = {skill: {school: (modules[schools.index(school)], round(random.uniform(1, 100), 1)) for school in schools} for skill in skills}
    return reco

@app.route('/api', methods=['GET'])
def process_input():
    paragraph = request.args.get('input')
    html_paragraph = html_format(paragraph)
    reco, scores = get_mod_recommendations(paragraph)
    #scores = school_score()
    #reco = mod_reco()

    response = {
        'html_paragraph': html_paragraph,
        'school_score': scores,
        'mod_reco': reco
    }
    return jsonify(response)

@app.route('/skills', methods=['GET'])
def get_skills():
    paragraph = request.args.get('input')
    html_paragraph = html_format(paragraph)
    return html_paragraph

if __name__ == '__main__':
    app.run(debug=True)