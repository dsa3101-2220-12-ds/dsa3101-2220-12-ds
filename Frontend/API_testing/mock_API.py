import random
from flask import Flask, request, jsonify

app = Flask(__name__)

def html_format(paragraph):
    return f"<p>{paragraph}</p>"

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
    scores = school_score()
    reco = mod_reco()

    response = {
        'html_paragraph': html_paragraph,
        'school_score': scores,
        'mod_reco': reco
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

